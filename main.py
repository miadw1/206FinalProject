import createtables
import calculations
import visualizations

# Main execution
def main():
    #Create the database and get a connection
    stadium_to_city_mapping = {
    "Aviva Stadium": "Dublin, Ireland",
    "Memorial Stadium (Stephenville, TX)": "Stephenville, TX",
    "University Stadium (NM)": "Albuquerque, NM",
    "Cramton Bowl": "Montgomery, AL",
    "Center Parc Stadium": "Atlanta, GA",
    "Mackay Stadium": "Reno, NV",
    "Clarence T.C. Ching Athletics Complex": "Honolulu, HI",
    "Jackson Field": "Alpine, TX",
    "Superior Dome": "Marquette, MI",
    "SHI Stadium": "Piscataway, NJ",
    "Villanova Stadium": "Villanova, PA",
    "Jayne Stadium": "Morehead, KY",
    "Burke-Tarr Stadium": "Jefferson City, TN",
    "Doyt L. Perry Stadium": "Bowling Green, OH",
    "Ernest W. Spangler Stadium": "Boiling Springs, NC",
    "FBC Mortgage Stadium": "Orlando, FL",
    "Kelly/Shorts Stadium": "Mount Pleasant, MI",
    "West Family Stadium": "West Liberty, WV",
    "Duvall-Rosier Field": "Fairmont, WV",
    "Bearcat Stadium": "Maryville, MO",
    "Malone Stadium": "Monroe, LA",
    "MDU Resources Community Bowl": "Bismarck, ND",
    "Herb Parker Stadium": "Minot, ND",
    "Memorial Stadium (Wayne, NE)": "Wayne, NE",
    "Delaware Stadium": "Newark, DE",
    "Sox Harrison Stadium": "Edinboro, PA",
    "Chryst Field at Biemesderfer Stadium": "Millersville, PA",
    "Zable Stadium": "Williamsburg, VA",
    "UB Stadium": "Buffalo, NY",
    "Allegacy Federal Credit Union Stadium": "Winston-Salem, NC",
    "Carter-Finley Stadium": "Raleigh, NC",
    "Five Star Stadium at the Moye Complex": "Macon, GA",
    "Gable Field at Doc Wadley Stadium": "Tahlequah, OK",
    "Chet Anderson Stadium": "Bemidji, MN",
    "Bishop Schmitt Field": "Wheeling, WV",
    "Drake Stadium": "Des Moines, IA",
    "Glass Bowl": "Toledo, OH",
    "War Memorial Stadium (AR)": "Little Rock, AR",
    "Folsom Field": "Boulder, CO",
    "Memorial Stadium": "Columbia, MO",
    "Children's Mercy Park": "Kansas City, KS",
    "Homer Bryce Stadium": "Nacogdoches, TX",
    "Huntington Bank Stadium": "Minneapolis, MN",
    "Chapman Stadium": "Tulsa, OK",
    "Yulman Stadium": "New Orleans, LA",
    "Lewis Field Stadium": "Hays, KS",
    "Francis G. Welch Stadium": "Emporia, KS",
    "O'Shaughnessy Stadium": "St. Paul, MN",
    "O'Harra Stadium": "Rapid City, SD",
    "Javelina Stadium": "Kingsville, TX",
    "Memorial Stadium (Wichita Falls, TX)": "Wichita Falls, TX",
    "Sanchez Family Stadium": "Las Vegas, NM",
    "Elliott Field at Don Beebe Stadium": "Chadron, NE",
    "AmFirst Stadium": "Jacksonville, AL",
    "Protective Stadium": "Birmingham, AL",
    "DakotaDome": "Vermillion, SD",
    "Memorial Stadium (Champaign, IL)": "Champaign, IL",
    "Roos Field": "Cheney, WA",
    "Rice-Eccles Stadium": "Salt Lake City, UT",
    "CEFCU Stadium": "San Jose, CA",
    "Michie Stadium": "West Point, NY",
    "Alfond Stadium": "Orono, ME",
    "Memorial Stadium (Norman, OK)": "Norman, OK",
    "Spartan Stadium": "East Lansing, MI",
    "Wallace Wade Stadium": "Durham, NC",
    "Camp Randall Stadium": "Madison, WI",
    "Stanford Stadium": "Stanford, CA",
    "Maverik Stadium": "Logan, UT",
    "SECU Stadium": "College Park, MD",
    "Milan Puskar Stadium": "Morgantown, WV",
    "Navy-Marine Corps Memorial Stadium": "Annapolis, MD",
    "Welcome Stadium": "Dayton, OH",
    "Wagner College Stadium": "Staten Island, NY",
    "L&N Federal Credit Union Stadium": "Louisville, KY",
    "Acrisure Stadium": "Pittsburgh, PA",
    "Kinnick Stadium": "Iowa City, IA",
    "Ross-Ade Stadium": "West Lafayette, IN",
    "Mercedes-Benz Stadium": "Atlanta, GA",
    "FirstBank Stadium": "Nashville, TN",
    "Cooper Field": "Washington, DC",
    "Neyland Stadium": "Knoxville, TN",
    "Butler Bowl": "Indianapolis, IN",
    "Municipal Stadium": "Hagerstown, MD",
    "Mitchell Stadium": "Bluefield, WV",
    "Wildcat Stadium (GA)": "Fort Valley, GA",
    "George Williams Athletic Complex": "Raleigh, NC",
    "Fred Selfe Stadium at Nicewonder Field": "Emory, VA",
    "Boone Pickens Stadium": "Stillwater, OK",
    "Nippert Stadium": "Cincinnati, OH",
    "B.T. Harvey Stadium": "Atlanta, GA",
    "Alumni Stadium (KY)": "Frankfort, KY",
    "J.W. Babb Stadium": "Due West, SC",
    "Gesa Field": "Pullman, WA",
    "Memorial Stadium (Lincoln, NE)": "Lincoln, NE",
    "Memorial Stadium (Bloomington, IN)": "Bloomington, IN",
    "Lanny and Sharon Martin Stadium": "Evanston, IL",
    "Ohio Stadium": "Columbus, OH",
    "DKR-Texas Memorial Stadium": "Austin, TX",
    "Alamodome": "San Antonio, TX",
    "Ben Hill Griffin Stadium": "Gainesville, FL",
    "Kidd Brewer Stadium": "Boone, NC",
    "Falcon Stadium": "Colorado Springs, CO",
    "JMA Wireless Dome": "Syracuse, NY",
    "Jack Trice Stadium": "Ames, IA",
    "Huskie Stadium": "DeKalb, IL",
    "Warren McGuirk Alumni Stadium": "Amherst, MA",
    "Allen E. Paulson Stadium": "Statesboro, GA",
    "Walkup Skydome": "Flagstaff, AZ",
    "Ray Dennison Memorial Field": "Durango, CO",
    "Williams-Brice Stadium": "Columbia, SC",
    "Joan C. Edwards Stadium": "Huntington, WV",
    "Hancock Whitney Stadium": "Mobile, AL",
    "California Memorial Stadium": "Berkeley, CA",
    "UNI-Dome": "Cedar Falls, IA",
    "Williams Stadium (VA)": "Lynchburg, VA",
    "Buccaneer Field": "Charleston, SC",
    "Scott Stadium": "Charlottesville, VA",
    "Dowdy-Ficklen Stadium": "Greenville, NC",
    "Davis Wade Stadium": "Starkville, MS",
    "Armstrong Stadium": "Hampton, VA",
    "University Stadium (GA)": "Carrollton, GA",
    "Campus Field": "Fairfield, CT",
    "Alumni Memorial Stadium (NC)": "Salisbury, NC",
    "Spec Martin Municipal Stadium": "DeLand, FL",
    "Grace P. Johnson Stadium": "Pembroke, NC",
    "Bragg Memorial Stadium": "Tallahassee, FL",
    "Nissan Stadium": "Nashville, TN",
    "Reser Stadium": "Corvallis, OR",
    "Bob Ford Field": "Albany, NY",
    "Bryant-Denny Stadium": "Tuscaloosa, AL",
    "Rice Stadium": "Houston, TX",
    "Ratliff Stadium": "Odessa, TX",
    "Gayle and Tom Benson Stadium": "San Antonio, TX",
    "Panther Stadium": "Prairie View, TX",
    "Bazemore-Hyder Stadium": "Valdosta, GA",
    "Tiger Stadium (AL)": "Livingston, AL",
    "Veterans Memorial Stadium (AL)": "Troy, AL",
    "Centennial Bank Stadium": "Jonesboro, AR",
    "Johnny 'Red' Floyd Stadium": "Murfreesboro, TN",
    "Simmons Bank Liberty Stadium": "Memphis, TN",
    "Raymond James Stadium": "Tampa, FL",
    "McLane Stadium": "Waco, TX",
    "Bill Snyder Family Stadium": "Manhattan, KS",
    "Vaught-Hemingway Stadium": "Oxford, MS",
    "Meade Stadium": "Kingston, RI",
    "TDECU Stadium": "Houston, TX",
    "Joe Aillet Stadium": "Ruston, LA",
    "Snapdragon Stadium": "San Diego, CA",
    "LaVell Edwards Stadium": "Provo, UT",
    "Gerald J. Ford Stadium": "Dallas, TX",
    "Bobby Dodd Stadium": "Atlanta, GA",
    "Cajun Field": "Lafayette, LA",
    "Bobcat Stadium (TX)": "San Marcos, TX",
    "Jerry Richardson Stadium": "Charlotte, NC",
    "Cowboy Stadium": "Lake Charles, LA",
    "Torero Stadium": "San Diego, CA",
    "Washington-Grizzly Stadium": "Missoula, MT",
    "Aggie Memorial Stadium": "Las Cruces, NM",
    "Greater Zion Stadium": "St. George, UT",
    "Mountain America Stadium": "Tempe, AZ",
    "Arizona Stadium": "Tucson, AZ",
    "Husky Stadium": "Seattle, WA",
    "Hard Rock Stadium": "Miami Gardens, FL",
    "Tom Benson Hall of Fame Stadium": "Canton, OH",
    "Allegiant Stadium": "Las Vegas, NV",
    "Doak Campbell Stadium": "Tallahassee, FL"
}

    conn = createtables.create_database()

    c = conn.cursor()

    results = c.execute('SELECT COUNT(*) FROM weather')
    count = results.fetchone()[0]

    if count == 0:
      data = list(stadium_to_city_mapping.values())[count : count + 12]
    else:
      data = list(stadium_to_city_mapping.values())[count - 1: count + 11]

    for city in data:
        weather_data = createtables.fetch_weather_data(createtables.weatherAPIkey, city)
        if weather_data:
          createtables.insert_weather_data(conn, weather_data)

    results = c.execute('SELECT COUNT(*) FROM games')
    count = results.fetchone()[0]

    cfb_data = createtables.fetch_cfb_data(createtables.cfbAPIkey, 2024)  

    if count == 0:
      data = cfb_data[count : count + 12]
    else:
      data = cfb_data[count - 1: count + 11]

    for game in data:
        createtables.insert_game_data(conn, game)

    # Update city information
    createtables.update_city_information('sports_weather3.db', stadium_to_city_mapping)

    # Fetch sunny games data and visualize
    sunny_data = calculations.get_sunny_games(conn)
    visualizations.visualize_sunny_scores(sunny_data)

    #city stats
    city_stats= calculations.calculate_city_stats(conn)
    calculations.write_data_to_file(city_stats, 'city_stats.txt')

    #visualize_total_games(city_stats)
    visualizations.visualize_average_scores(city_stats)
    visualizations.visualize_temp_vs_scores(conn)

    # Visualize weather conditions
    visualizations.visualize_weather_conditions(city_stats)


    #Close the database connection
    conn.close()

if __name__ == "__main__":
    main()