# Fetch combined data
def get_combined_data(conn):
    c = conn.cursor()
    c.execute('''
        SELECT c.city_name, t1.team_name AS home_team, t2.team_name AS away_team,
               g.home_score, g.away_score, v.venue_name, w.temperature, con.condition_name
        FROM games g
        JOIN cities c ON g.city_id = c.id
        JOIN teams t1 ON g.home_team_id = t1.id
        JOIN teams t2 ON g.away_team_id = t2.id
        JOIN venues v ON g.venue_id = v.id
        JOIN weather w ON g.city_id = w.city_id
        JOIN conditions con ON w.condition_id = con.id
    ''')
    return c.fetchall()

# Fetch combined data filtered for sunny weather
def get_sunny_games(conn):
    c = conn.cursor()
    c.execute('''
        SELECT c.city_name, g.home_score
        FROM games g
        JOIN weather w ON g.city_id = w.city_id
        JOIN conditions con ON w.condition_id = con.id
        JOIN cities c ON g.city_id = c.id
        WHERE con.condition_name = 'Sunny'
    ''')
    sunny_games = c.fetchall()
    return sunny_games

def calculate_city_stats(conn):
    c = conn.cursor()
    c.execute('''
        SELECT c.city_name, COUNT(g.id) AS total_games,
               AVG(g.home_score) AS avg_home_score,
               AVG(g.away_score) AS avg_away_score,
               AVG(w.temperature) AS avg_temperature
        FROM games g
        JOIN cities c ON g.city_id = c.id
        JOIN weather w ON g.city_id = w.city_id
        GROUP BY c.city_name
    ''')
    return c.fetchall()

#write to a file
def write_data_to_file(data, filename):
  with open(filename, 'w') as file:
    #<number is the width of the column->makes the text file look more clean 
    file.write(f"{'City':<20}{'Total Games':<20}{'Average Home Score':<20}{'Average Away Score':<20}{'Avg Temp (C)':<15}\n")
    for row in data:
       file.write(f"{row[0]:<20}{row[1]:<20}{row[2]:<20.2f}{row[3]:<20.2f}{row[4]:<15.2f}\n")
