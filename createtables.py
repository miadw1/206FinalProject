import requests
import sqlite3

# API Keys
weatherAPIkey = 'd273c16af6834a47950201709241604'
cfbAPIkey = 'AqtJDEUZayqfsNVrstvKqfXMT7eOINWbMNMwTn7tGc/MNETi/fsFvr1UsswpBjPH'

# Fetch weather data
def fetch_weather_data(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        #print("API Response:", weather_data)
        return {
            'city': city,
            'temperature': max(0, min(50, weather_data['current']['temp_c'])),
            'humidity': weather_data['current']['humidity'],
            'precipitation': weather_data['current'].get('precip_mm', 0),
            'condition': weather_data['current']['condition']['text']
        }
    except requests.RequestException as e:
        print(f"An error occurred fetching weather data: {e}")
        return None

# Fetch all college football data for the season
def fetch_cfb_data(api_key, season, max_week=15):
    all_games = []
    headers = {'Authorization': f'Bearer {api_key}'}

    for week in range(1, max_week + 1):
        url = f"https://api.collegefootballdata.com/games?year={season}&week={week}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            games = response.json()
            all_games.extend([
                {
                    'home_team': game['home_team'],
                    'away_team': game['away_team'],
                    'home_score': max(0, min(50, game.get('home_points') or 0)),
                    'away_score': max(0, min(50, game.get('away_points') or 0)),
                    'venue': game.get('venue', 'Unknown'),
                    'city': game.get('city', 'Unknown')
                }
                for game in games
            ])
        except requests.RequestException as e:
            print(f"An error occurred fetching college football data for week {week}: {e}")
            continue

    return all_games

# Update city information
def update_city_information(db_path, mapping):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for stadium, city in mapping.items():
        # Get or create the city_id for the given city
        city_id = get_or_create_id(conn, "cities", "city_name", city)
        venue_id = get_or_create_id(conn, "venues", "venue_name", stadium)

        # Update the games table to set the city_id based on the venue
        cursor.execute('''
            UPDATE games
            SET city_id = ?
            WHERE venue_id = ?
        ''', (city_id, venue_id))

    conn.commit()
    conn.close()

# Create database
def create_database():
    conn = sqlite3.connect('sports_weather3.db')
    c = conn.cursor()

    # Cities Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            city_name TEXT UNIQUE
        )
    ''')

    # Teams Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            team_name TEXT UNIQUE
        )
    ''')

    # Venues Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY,
            venue_name TEXT UNIQUE
        )
    ''')

    # Conditions Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS conditions (
            id INTEGER PRIMARY KEY,
            condition_name TEXT UNIQUE
        )
    ''')

    # Weather Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city_id INTEGER,
            condition_id INTEGER,
            temperature REAL,
            humidity INTEGER,
            precipitation REAL,
            FOREIGN KEY (city_id) REFERENCES cities (id),
            FOREIGN KEY (condition_id) REFERENCES conditions (id)
        )
    ''')

    # Games Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            home_team_id INTEGER,
            away_team_id INTEGER,
            home_score INTEGER,
            away_score INTEGER,
            venue_id INTEGER,
            city_id INTEGER,
            FOREIGN KEY (home_team_id) REFERENCES teams (id),
            FOREIGN KEY (away_team_id) REFERENCES teams (id),
            FOREIGN KEY (venue_id) REFERENCES venues (id),
            FOREIGN KEY (city_id) REFERENCES cities (id)
        )
    ''')
    conn.commit()
    return conn

def insert_weather_data(conn, weather_data):
    city_id = get_or_create_id(conn, "cities", "city_name", weather_data['city'])
    condition_id = get_or_create_id(conn, "conditions", "condition_name", weather_data['condition'])
    c = conn.cursor()
    c.execute('''
        INSERT INTO weather (city_id, condition_id, temperature, humidity, precipitation)
        VALUES (?, ?, ?, ?, ?)
    ''', (city_id, condition_id, weather_data['temperature'], weather_data['humidity'], weather_data['precipitation']))

    conn.commit()

# Insert game data
def insert_game_data(conn, game_data):
    home_team_id = get_or_create_id(conn, "teams", "team_name", game_data['home_team'])
    away_team_id = get_or_create_id(conn, "teams", "team_name", game_data['away_team'])
    venue_id = get_or_create_id(conn, "venues", "venue_name", game_data['venue'])
    city_id = get_or_create_id(conn, "cities", "city_name", game_data['city'])
    c = conn.cursor()
    c.execute('''
        INSERT INTO games (home_team_id, away_team_id, home_score, away_score, venue_id, city_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (home_team_id, away_team_id, game_data['home_score'], game_data['away_score'], venue_id, city_id))
    conn.commit()

    def get_or_create_id(conn, table_name, column_name, value):
    c = conn.cursor()
    c.execute(f'SELECT id FROM {table_name} WHERE {column_name} = ?', (value,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        c.execute(f'INSERT INTO {table_name} ({column_name}) VALUES (?)', (value,))
        conn.commit()
        return c.lastrowid