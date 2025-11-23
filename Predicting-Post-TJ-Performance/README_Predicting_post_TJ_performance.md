# Predicting Post Tommy John Performance

This notebook investigates and models the performance and durability of MLB pitchers returning from Tommy John surgery—an increasingly common procedure affecting over a third of big-league pitchers as of 2023. The analysis leverages Statcast data and surgery records to empower front offices with predictive tools for smarter contract and roster decision-making.

## Description

Tommy John surgery is now an inescapable reality in professional baseball, with 35.3% of active MLB pitchers having undergone the procedure (up 29% from 2016). With so many careers affected, the focus for organizations has shifted from preventing injuries to forecasting a player’s effectiveness and durability after surgery. This project trains machine learning models on historical MLB pitcher data to answer:
- **Will a pitcher be effective after Tommy John surgery?**  
  *A regression model predicts post-surgery XWOBA (expected weighted on-base average against), an industry-standard metric for pitcher effectiveness.*
- **Will a pitcher be durable after Tommy John surgery?**  
  *A classification model predicts whether a pitcher will reach 500 pitches thrown in their return season, answering whether they’ll be a reliable investment.*

### Data

- **Performance metrics:** 71 features for every MLB pitcher (2019–present) from Statcast (baseballsavant.mlb.com).
- **Surgery/demographics:** 42 features for all MLB-drafted players who have undergone Tommy John surgery in the modern era (from @MLBPlayerAnalysis).

The data is merged and carefully summarized so each pitcher is represented by a pre- and post-surgery record, with appropriate aggregation and realistic target assignments.

### Methods

- **Regression (Predicting XWOBA):**  
  Three models built, including:
  - Backwards stepwise regression (with/without demographic data)
  - Recursive feature elimination

  The recursive feature elimination model performed best on test data, though all suffered from overfitting due to limited sample size (n=91).

- **Classification (Predicting Durability):**  
  Grid search cross-validation compared logistic regression, random forest, decision tree, bagging, boosting, and gradient boosting.
  - Gradient boosting showed the highest accuracy (63%) predicting pitchers who would throw ≥500 pitches in their return season.

### Key Findings

- **Performance:**  
  Pitchers average a statistically significant increase in XWOBA after Tommy John surgery (p=0.01), meaning they suppress fewer opponent runs. No significant difference was found in average pitches thrown (p=0.56).
- **Model Utility:**  
  The regression and classification models provide insights to front offices for contract and trade decision-making. However, overfitting and bias (especially toward false positives in durability prediction) should be considered before full-scale adoption.

- **Ethical Implications:**  
  While models are built with public data, inclusion of demographics (e.g. high school, hometown) could enable unintended bias or discrimination. Such features were not selected in the final models, but this risk increases with dataset expansion.

## Getting Started

### Dependencies

- Python 3.8+
- Jupyter Notebooks
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### Installing

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Executing Program

1. Place the required dataset(s) such as `tj_combines_data.csv` in your working directory.
2. Open the notebook: `Predicting_Tommy_John.ipynb` in Jupyter.
3. Run all cells, following sections on data preparation, exploration, modeling, and results.

## Authors

Matthew Heinen  
Bellevue University  
Email: matthew.heinen@my365.bellevue.edu  
GitHub: [@Matt-Heinen](https://github.com/Matt-Heinen)

## Version History

1.0 Initial Release

## Acknowledgments

- Statcast, baseballsavant.mlb.com
- Tommy John Surgery data from @MLBPlayerAnalysis
- American Medical Association statistical reports
- MLB for public player performance records
- Nick Hanhan’s analytics insights on Tommy John surgery
- Bellevue University DSC 630, Professor Hua

**Resources**
- [AMA: Tommy John Surgery Trends](https://www.ama-assn.org/delivering-care/public-health/what-doctors-wish-patients-knew-about-tommy-john-surgery)
- [Statcast Search Portal](https://baseballsavant.mlb.com/statcast_search)
- [Tommy John Surgery List (@MLBPlayerAnalys)](https://docs.google.com/spreadsheets/d/1gQujXQQGOVNaiuwSN680Hq-FDVsCwvN-3AazykOBON0/edit?gid=0#gid=0)
- [Hanhan, N. (2021), Medium: Analytical Study](https://medium.com/@nhanhan2/an-analytical-study-of-tommy-john-surgery-8a396b4509ef)