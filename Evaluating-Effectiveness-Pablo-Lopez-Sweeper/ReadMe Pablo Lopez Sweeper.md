# Evaluating Effectiveness of Pablo Lopez's Sweeper

This project analyzes the effectiveness of Pablo Lopez's sweeper pitch in the 2023 and 2024 MLB seasons, using detailed Statcast data to understand performance trends, key pitch metrics, and correlations with run prevention. The goal is to assess how pitch characteristics and year-over-year changes have impacted Lopez's success and to quantify the impact of his sweeper on game outcomes.

## Description

The notebook explores several key questions:
1. Has Lopez’s sweeper remained effective over time?
2. How do pitch metrics such as spin rate, axis, and velocity relate to run prevention?
3. Which pitch attributes correlate most with successful results for Lopez?

Using bar charts and scatter plots, the workflow visualizes year-over-year effectiveness (run expectancy and win expectancy) and the impact of spin rate on pitching outcomes.

## Getting Started

### Dependencies

- Python 3.8+
- Jupyter Notebook
- pandas
- numpy
- matplotlib

### Installing

Install required packages:
```bash
pip install pandas numpy matplotlib
```

### Executing Program

1. Place the dataset (`Pablo_Home_Sweeper.csv`) in your working directory.
2. Open the notebook: `Pablo_lopes_sweeper_evaluation.ipynb` in Jupyter.
3. Run notebook cells to:
   - Load and filter data for relevant pitch metrics
   - Perform analysis and generate graphs for effectiveness and feature relationships

Graphs and analysis will be displayed in notebook output.

## Authors

Matthew Heinen  
Email: matthew.heinen@my365.bellevue.edu  
GitHub: [@Matt-Heinen](https://github.com/Matt-Heinen)

## Version History

1.0 Initial Release

## Acknowledgments

- MLB Statcast and Baseball Savant for pitch-level data
