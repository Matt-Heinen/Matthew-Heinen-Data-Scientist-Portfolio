# Weather and Carlos Santana’s Effectiveness

This project investigates how weather and ballpark variables influence the hitting performance of MLB player Carlos Santana. By integrating Baseball Savant data, web-scraped ballpark characteristics, and API-sourced weather data into a single database, the analysis aims to uncover relationships between temperature, weather conditions, altitude, and Santana’s effectiveness at the plate.

## Description

The notebook demonstrates the process of loading and joining multiple data sources—flat files, web-scraped, and API-based—into an SQL database and then combining them in a single analytical DataFrame. Analyses and visualizations are provided to address questions such as:
- Does temperature affect launch speed or hitting outcomes?
- How do weather conditions (clear, rain, mist, etc.) relate to estimated batting average and hit frequency?
- What is the distribution of Santana’s hits under different weather conditions and temperatures?
- Does altitude have any measurable impact on hit distance?

The project features exploratory visualizations, regression modeling, and statistical tests to determine if weather and ballpark variables meaningfully affect Carlos Santana’s hitting performance.

## Getting Started

### Dependencies

- Python 3.8+
- Jupyter Notebooks
- pandas
- numpy
- matplotlib
- seaborn
- sqlite3
- statsmodels
- scipy

### Installing

Install required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

### Executing Program

1. Download all needed data files:  
   - `carlos_balls_in_play.csv`  
   - `carlos_weather_from_api_no_duplicates.csv`  
   - `ballpark_data_web.csv`  
   - `ab_key.csv`  

2. Open the notebook: `Carlos Santana Effectiveness.ipynb` in Jupyter.

3. Run the notebook sequentially to:
   - Load, join, and verify data in a SQLite database.
   - Execute the analysis and create visualizations.

4. Review the findings regarding how temperature, weather, and ballpark altitude affect Santana’s performance.

## Authors

Matthew Heinen  
Email: matthew.heinen@my365.bellevue.edu  
GitHub: [@Matt-Heinen](https://github.com/Matt-Heinen)

## Version History

1.0 Initial Release

## Acknowledgments

- Baseball Savant for MLB play-by-play and Statcast data.
- Steamheads for ballpark location and altitude information.
- OpenWeather API for historical game weather.
