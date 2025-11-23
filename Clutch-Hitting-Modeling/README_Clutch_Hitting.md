# Clutch Hitting Modeling

This project investigates clutch hitting in Major League Baseball, with a focus on the Minnesota Twins’ struggles in high-pressure, runners-in-scoring-position (RISP) situations. Using recent player data, the notebook demonstrates analytical approaches to identify players with a “clutch gene,” explains relevant features, and explores machine learning models to predict clutch hitting performance.

## Description

The notebook presents an end-to-end analytical exercise using at-bat and player statistics from MLB (2020–2024, RISP situations). The analysis includes:
- Data exploration and visualization of batting average with RISP
- Identification of outliers and appropriate data filtering
- Year-over-year analysis for normalization insights
- Feature correlation analysis to determine which metrics best predict run expectancy in clutch situations
- Preparation for regression and unsupervised clustering models to forecast future clutch performance and discover clutch hitters

The project’s goal is to empower decision-making for player acquisition and lineup optimization by statistically distinguishing clutch hitters from average performers.

## Getting Started

### Dependencies

- Python 3.8+
- Jupyter Notebooks
- pandas
- numpy
- matplotlib
- seaborn

### Installing

Install required packages:

```bash
pip install pandas numpy matplotlib seaborn
```

### Executing Program

1. Download any required data files (such as `RISP.csv`) to your working directory.
2. Open the notebook: `Clutch Hitting Modeling.ipynb` in Jupyter.
3. Run the cells sequentially to:
   - Load, preprocess, and explore the clutch hitting dataset
   - Visualize batting average distributions & yearly trends
   - Analyze feature correlations and prepare for modeling

4. Results and graphs will be shown directly in notebook outputs.

## Authors

Matthew Heinen  
Email: matthew.heinen@my365.bellevue.edu  
GitHub: [@Matt-Heinen](https://github.com/Matt-Heinen)

## Version History

1.0 Initial Release

## Acknowledgments

- MLB Statcast and Baseball Reference for player and RISP data
- Project developed for Bellevue University DSC 550, Final Project (Milestone 1 & 2)