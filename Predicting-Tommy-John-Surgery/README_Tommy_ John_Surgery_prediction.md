# Predicting Tommy John Surgery Using MLB Statcast Data

This project analyzes MLB pitcher Statcast data to identify trends and potential predictors for Tommy John (TJ) surgery. By exploring pitch characteristics and performance metrics, the notebook seeks to develop strategies or models to help MLB teams predict injury risks and make data-driven decisions for pitcher health.

## Description

The notebook examines whether advanced Statcast metrics—such as pitch speed, spin rate, and pitch type averages—can provide insight into a player's injury risk, specifically their likelihood of undergoing Tommy John surgery. Through feature selection, exploratory data analysis, and modeling, the workflow tries to illuminate statistically significant patterns among those who have had the surgery versus those who have not.

Data workflow includes:
- Reading and cleaning MLB pitcher Statcast and injury history data
- Engineering informative subsets of pitching features
- Exploratory analysis of age, innings pitched, and pitch characteristics (fastball, breaking, and offspeed metrics)
- Developing a predictive framework for TJ surgery history based on player features

## Getting Started

### Dependencies

- Python 3.8+
- Jupyter Notebooks
- pandas
- numpy
- matplotlib (for additional data visualization, if required)
- scikit-learn (if modeling included)

### Installing

From your terminal or command prompt, run:

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Executing Program

1. Download all associated datasets, including `tj_combines_data.csv`, to the working directory.
2. Download the notebook: `Predicting_Tommy_John.ipynb`.
3. Open the notebook in Jupyter.
4. Step through the cells sequentially to execute the workflow.
   - Adjust file paths if necessary for your environment.
   - Run all cells to view the output and analysis steps.

## Authors

Matthew Heinen  
GitHub: [@Matt-Heinen](https://github.com/Matt-Heinen)  
Email: matthew.heinen@my365.bellevue.edu

## Version History

1.0 Initial Release

## Acknowledgments

 Statcast data provided by MLB and BaseballSavant
 
Simon, J. M. (2020, May 13). Let’s model! using random forest to predict UCL reconstruction. Medium. https://medium.com/analytics-vidhya/lets-model-using-random-forest-to-predict-ucl-reconstruction-6185ebdc853e 