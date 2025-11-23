# Weather Retrieval App

This project is a simple Python application that allows users to retrieve current weather information for a given U.S. city and state or ZIP code. The program uses the OpenWeatherMap API to obtain geolocation and current weather data, then presents it to the user in a clear, readable format with flexible unit selection.

## Description

The Weather Retrieval App prompts users to choose between searching by city/state or ZIP code. Users are then guided through the necessary input steps and provided error handling for invalid entries. The application performs two API calls:
1. Geocode API for location coordinates.
2. Current Weather API for live weather information.

Results include location, temperature (current, feels like, high/low), pressure, humidity, cloud cover, and description, all formatted for clarity and ease of use.

## Getting Started

### Dependencies

- Python 3.x
- `requests` library

### Installing

Install Python and the required `requests` package:

```bash
pip install requests
```

### Executing Program

1. Download the `.py` file to your computer.

2. Run the program in your terminal:

```bash
python "Weather Retrieval App.py"
```

3. Follow prompts to enter either a ZIP code or city and state, and select your preferred units (Fahrenheit, Celsius, Kelvin).

4. View the weather report printed in the terminal.

## Authors

Matthew Heinen: [@Matt-Heinen](https://github.com/Matt-Heinen)  
Email: matthew.heinen@my365.bellevue.edu

## Version History

1.0 Initial Release

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) API for geocoding and current weather data.
