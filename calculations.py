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
    file.write("City\tTotal Games\tAverage Home Score\tAverage Away Score\tAvg Temp (C)\n")
    for row in data:
      file.write(f"{row[0]}\t{row[1]}\t{row[2]:.2f}\t{row[3]:.2f}\t{row[4]:.2f}\n")