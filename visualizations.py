import matplotlib.pyplot as plt

# Visualize the data
def visualize_sunny_scores(data):
    if not data:
        print("No data available for sunny conditions.")
        return

    # Separate data into cities and scores
    cities = [row[0] for row in data]
    scores = [row[1] for row in data]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(cities, scores, color='orange')
    plt.xlabel('City')
    plt.ylabel('Home Score')
    plt.title('Home Scores in Cities with Sunny Conditions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def visualize_temp_vs_scores(conn):
    c = conn.cursor()
    c.execute('''
        SELECT w.temperature, (g.home_score + g.away_score) AS total_score
        FROM weather w
        JOIN games g ON w.city_id = g.city_id
    ''')
    data = c.fetchall()
    temps = [row[0] for row in data]
    scores = [row[1] for row in data]
    plt.scatter(temps, scores, alpha=0.5, color='blue')
    plt.xlabel('Temperature (C)')
    plt.ylabel('Total Game Score')
    plt.title('Temperature vs Total Game Scores')
    plt.show()

def visualize_average_scores(data):
  cities= [row[0] for row in data]
  avg_home_scores= [row[1] for row in data]
  avg_away_scores= [row[2] for row in data]

  plt.figure(figsize=(10, 6))
  plt.bar(cities, avg_home_scores, label= 'Average Home Score', alpha=0.7)
  plt.bar(cities, avg_away_scores, label= 'Average Away Score', alpha=0.7, bottom= avg_home_scores)
  plt.xlabel('City')
  plt.ylabel('Average Score')
  plt.title('Average Home and Away Scores by City')
  plt.xticks(rotation=45, ha='right')
  plt.legend()
  plt.tight_layout()
  plt.show()

def visualize_weather_conditions(data):
  cities= [row[0] for row in data]
  avg_temperature= [row[4] for row in data]

  fig,ax1= plt.subplots(figsize=(12,8))
  ax1.bar(cities, avg_temperature, label= 'Average Temperature (C)', color= 'green', alpha=0.7)
  ax1.set_xlabel('City')
  ax1.set_ylabel('Average Temperature (C)')
  ax1.tick_params(axis= 'y')

  plt.title('Weather Conditions By City')
  plt.xticks(rotation=45, ha='right')
  plt.legend()
  plt.tight_layout()
  plt.show()
