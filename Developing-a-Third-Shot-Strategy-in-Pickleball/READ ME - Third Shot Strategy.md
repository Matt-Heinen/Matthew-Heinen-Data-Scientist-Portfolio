# Developing a Third Shot Strategy in Pickleball

This project uses data science and predictive modeling to optimize third shot selection in pickleball. By training machine learning models on rally and shot data, this project aims to help players develop winning strategies for the critical third shot in a rally.

## Description

This project provides a data-driven approach to determining the optimal third shot selection in pickleball. The third shot is crucial in pickleball as it sets up the rally and can significantly impact the outcome. This project trains several machine learning models to predict the best shot type (Drop, Drive, or Lob) based on player characteristics, court positioning, and rally dynamics. 

The project includes:
- Connection to the PKLMart database containing professional pickleball match data
- Extraction and cleaning of rally, shot, and player data from the database
- Handling missing data through imputation strategies
- Feature engineering including player gender, dominant hand, court position (loc_x, loc_y), and ball travel time
- Training multiple models (Logistic Regression, Random Forest, XGBoost, Neural Networks) for professional and amateur play
- Model evaluation and comparison to identify the best predictive model

### Database Structure

The project uses the PKLMart PostgreSQL database with the following key tables:
- **rally**: Contains rally-level data including serving team, return team, players, third shot type, winner, and rally length
- **shot**: Contains shot-level data including shot location (loc_x, loc_y), ball travel time (btt_before), and shot type
- **player**: Contains player attributes including gender and dominant hand

## Getting Started

### Dependencies

- Python 3.9+
- Jupyter Notebooks
- psycopg2 (PostgreSQL database adapter)
- pandas
- numpy
- matplotlib
- scikit-learn
- xgboost

### Installing

```bash
pip install jupyter psycopg2-binary pandas numpy matplotlib scikit-learn xgboost
```

### Executing program

1) Download the entire repository 

2) Open the `Shot Selection Pickleball.ipynb` file from the repository

3) Note: Database connection requires credentials to the PKLMart database. Update connection parameters as needed.

4) Select Run all 


## Authors

Matthew Heinen: @Matt-Heinen
(matthew.heinen@my365.bellevue.edu)

## Version History

1.0 Initial project Release


## Acknowledgments

Pickleball + data =   . pklmart. (n.d.). https://pklmart.com/ 🤯
Pickleball market. Market.us. (2025, May 5). https://market.us/report/pickleball-market/
