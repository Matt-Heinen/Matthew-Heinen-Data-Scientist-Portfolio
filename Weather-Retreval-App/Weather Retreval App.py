# DSC 510
# Week 12
# Fall 2023
# Final Programming Assignment 12.1
# Created By Matthew Heinen
# 10/3/23

# Change#:1
# Change(s) Made: Created functions get_zip(), get_city() and main()
# Date of Change: 10/3/2023
# Author: Matthew Heinen

# Change#:2
# Change(s) Made: Added error handling to get_city() function.
# Date of Change: 10/24/2023
# Author: Matthew Heinen

# Change#:3
# Change(s) Made: Added functions for API call GEOcode to get geographical
# coordinates, one function gets coordinates by City, State
# and the other by ZIP.
# Date of Change: 11/6/2023
# Author: Matthew Heinen

# Change#:4
# Change(s) Made: Added functions for API call CurrentWeather to get weather
# passing in latitude and longitude from the geocode API.
# Date of Change: 11/7/2023
# Author: Matthew Heinen

# Change#:5
# Change(s) Made: Added functions to format and print the json data from the
# CurrentWeather API to the user in a readable format.
# Date of Change: 11/14/2023
# Author: Matthew Heinen

# Change#:6
# Change(s) Made: Formatted printing of weather data to improve readability.
# Added Units to the user printout.
# Date of Change: 11/16/2023
# Author: Matthew Heinen

# Change#:7
# Change(s) Made: Added error handling for invalid city input.
# Date of Change: 11/18/2023
# Author: Matthew Heinen

# Define get_zip
def get_zip():
    zip_code = str(input('Please Enter Your 5 Digit Zip Code: '))

    # Validate proper zip code formatting.
    while len(zip_code) != 5 or not zip_code.isnumeric():
        zip_code = str(input('Please Enter Your 5 Digit Zip Code: '))
    else:
        print('Searching for Zip Code:', zip_code, '\n')
        return zip_code


# Define get_city
def get_city():
    # Declare state list
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    # Ask user the city.
    city = str(input('Please Enter Your City Name:'))

    # Validate city input.
    while any(chr.isdigit() for chr in city):
        city = str(input('Error you entered an invalid city name \n '
                         'Please Enter Your City Name:'))
    else:
        # Ask user the State code.
        state = str(input('Please enter the State Code 2 letters: '))

        while len(state) != 2 or not state.upper() in states:
            state = str(input('Error, Please enter a valid State Code '
                              '(2 letters): '))
        else:

            state_valid = state.upper()

    # Print the search city to the user.
    print("You are searching for: ", city.capitalize(), ",", state_valid , "\n")
    city_search = city.capitalize() + "," + state_valid
    return city_search


# Define get_geocode_city()
# This function retrieves the latitude and longitude given a input city, state
def get_geocode_city(city_search):
    import requests

    url = ('http://api.openweathermap.org/geo/1.0/direct?q=' + city_search
           + ',US&limit=1&appid=6c19f18811336253aa2827b2ddbc6854')

    payload = {}
    headers = {}

    # Try Blocks to handle bad requests.
    try:
        response = requests.request("GET", url, headers=headers,
                                    data=payload)
    # Print error message to user if connection does not work.
    # Error handle all connection errors
    except requests.ConnectionError as error:
        print('There was a connection error please try again')
        print(error)
    # Error Handle all other errors.
    except requests.exceptions.RequestException as error:
        print(error)

    # Remove list from response.
    response_json = response.json()
    # Error handle for invalid city input.
    try:
        response_dict = response_json[0]
    except IndexError as error:
        print("You have entered an invalid city name please try again")
        print(error)
        exit()
    # Extract latitude and longitude from new dictionary.
    lat = str(response_dict['lat'])
    lon = str(response_dict['lon'])
    # Declare lat_lon_list to pass coordinates.
    lat_lon_list = [lat, lon]
    # Return list.
    return lat_lon_list


# Define get_geocode_zip()
# This function will return coordinates based on an input ZIP code.
def get_geocode_zip(zip_search):
    import requests

    url = ('http://api.openweathermap.org/geo/1.0/zip?zip=' + zip_search
    +',US&appid=6c19f18811336253aa2827b2ddbc6854')

    payload = {}
    headers = {}

    # Try Blocks to handle bad requests.
    try:
        response = requests.request("GET", url, headers=headers,
                                    data=payload)
    # Print error message to user if connection does not work.
    # Error handle all connection errors
    except requests.ConnectionError as error:
        print('There was a connection error please try again')
        print(error)
    # Error Handle all other errors.
    except requests.exceptions.RequestException as error:
        print(error)

    # Create dictionary.
    response_dict = response.json()
    # Validate that input zip has corresponding lat and lon.
    try:
        # Extract latitude and longitude from new dictionary.
        lat = str(response_dict['lat'])
        lon = str(response_dict['lon'])
    except KeyError:
        print("You have enterd a ZIP code that cannot be found, "
              "Please try again.")
        exit()
    # Declare lat_lon_list to pass coordinates.
    lat_lon_list = [lat, lon]
    # Return list.
    return lat_lon_list


# Define current_weather()
# This function will gather the current weather from input latitude and
# longitude.
def current_weather(lat_lon_list):
    unit_choice = str(input('What units would you like your weather reported'
                            ' in? \nEnter "F" for Fahrenheit, "C" for Celsius '
                            'or "K" for Kelvin: '))
    while (unit_choice.upper() != "F" and unit_choice.upper() != "C"
           and unit_choice.upper() != "K"):
        print("Please enter a valid input! \n "
              "---------------------------------------")
        unit_choice = str(
            input('What units would you like your weather reported'
                  ' in? \nEnter "F" for Fahrenheit, "C" for Celsius '
                  'or "K" for Kelvin: '))
    else:
        unit_choice = unit_choice.upper()
        if unit_choice == "F":
            unit_search = "imperial"
        elif unit_choice == "C":
            unit_search = "metric"
        elif unit_choice == "K":
            unit_search = ""
    import requests
    # Declare latitude and longitude
    lat = lat_lon_list[0]
    lon = lat_lon_list[1]

    url = ('https://api.openweathermap.org/data/2.5/weather?lat=' +
           lat + '&lon=' + lon +
           '&appid=6c19f18811336253aa2827b2ddbc6854&units=' + unit_search)

    payload = {}
    headers = {}

    # Try Blocks to handle bad requests.
    try:
        response = requests.request("GET", url, headers=headers,
                                    data=payload)
    # Print error message to user if connection does not work.
    # Error handle all connection errors
    except requests.ConnectionError as error:
        print('There was a connection error please try again')
        print(error)
    # Error Handle all other errors.
    except requests.exceptions.RequestException as error:
        print(error)

    # Return the API call data in a dictionary.
    weather_dict_return = response.json()
    weather_unit_list = [weather_dict_return, unit_choice]
    return weather_unit_list


# Define print_current_weather()
# Function will print the Location (city, state), Current temp, feels like temp,
# low temp, high temp, pressure, humidity, and a current weather description
# to the user in a readable format.
def print_current_weather(list):
    # Define dictionary and units from the list returned from current_weather.
    dictionary = list[0]
    units = list[1]

    # Determine the unit labels.
    if units == "F":
        temp_units = "°F"
    elif units == "C":
        temp_units = "°C"
    elif units == "K":
        temp_units = "°K"

    # Determine the location name.
    location_name = dictionary["name"]

    # Define main dictionary to access Current temp, feels like temp,
    # low temp, high temp, pressure, humidity
    main_dictionary = dictionary["main"]

    # Create variables for Current temp, feels like temp, low temp, high temp,
    # pressure and humidity.
    current_temp = str(main_dictionary["temp"]) + " " + temp_units
    feels_like = str(main_dictionary["feels_like"]) + " " + temp_units
    low_temp = str(main_dictionary["temp_min"]) + " " + temp_units
    high_temp = str(main_dictionary["temp_max"]) + " " + temp_units
    pressure = str(main_dictionary["pressure"]) + " hPa"
    humidity = str(main_dictionary["humidity"]) + " %"

    # Define weather_dictionary to access a weather description.
    weather_list = dictionary["weather"]
    weather_dictionary = weather_list[0]

    # Create Variable for cloud cover and description.
    cloud_cover = weather_dictionary["main"]
    cloud_description = weather_dictionary["description"]

    # Print the result to the user
    # Print Header.
    print("-------------------------------------------------------------------")
    title = "Weather for " + location_name
    print(title)
    print("-------------------------------------------------------------------")

    # Print Weather Description
    print("{:<20} {:<8} {:<1} {:<20} {:<10}".format(
        "Cloud Cover:", cloud_cover.title(), " | ",
        "Cloud Description:", cloud_description.title()))
    print("-------------------------------------------------------------------")

    # Print numeric weather data.
    # Current and Feels like Temp.
    print("{:<20} {:<5} {:<1} {:<20} {:<10}".format(
        "Current Temp:", current_temp, " | ",
        "Feels Like Temp:", feels_like))
    print("-------------------------------------------------------------------")
    # Low and High temp
    print("{:<20} {:<5} {:<1} {:<20} {:<10}".format(
        "Low Temp:", low_temp, " | ",
        "High Temp:", high_temp))
    print("-------------------------------------------------------------------")
    # Pressure and Humidity.
    print("{:<20} {:<5} {:<1} {:<20} {:<10}".format(
        "Pressure:", pressure, " | ",
        "Humidity:", humidity))
    print("-------------------------------------------------------------------")


# Define the main function

def main():

    # Print welcome message.
    print('Welcome to the Weather Retrieval Program. \n'
          '-------------------------------------------------------------------')

    # Ask User if they would like to search by Zip or City.
    search_choice = str(input('Would you like to search for weather using zip '
                              'code or city? \nInput "Z" for Zip Code, '
                              '"C" for City, or "QUIT" to Quit:'))
    # While loop to determine how to search.
    while search_choice.upper() != 'QUIT':
        if search_choice.upper() == 'Z':
            # Run Zip code retrieval.
            print_current_weather(current_weather(get_geocode_zip(get_zip())))
            # Reset search_choice to get back to input.
            search_choice = 'W'
        if search_choice.upper() == 'C':
            print_current_weather(current_weather(get_geocode_city(get_city())))
            # Reset search_choice to get back to input.
            search_choice = 'W'
        else:
            search_choice = str(
                input('Would you like to search for weather using zip '
                      'code or city? \nInput "Z" for Zip Code, '
                      '"C" for City, or "QUIT" to Quit:'))


# Call from main:
if __name__ == "__main__":
    main()
