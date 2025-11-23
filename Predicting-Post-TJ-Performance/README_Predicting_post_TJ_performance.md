# Predicting Post Tommy John Performance

This notebook investigates and models the performance and durability of MLB pitchers returning from Tommy John surgery—an increasingly common procedure affecting over a third of big-league pitchers as of 2023. The analysis leverages Statcast data and surgery records to empower front offices with predictive tools for smarter contract and roster decision-making.

## Description

Tommy John surgery is now an inescapable reality in professional baseball, with 35.3% of active MLB pitchers having undergone the procedure (up 29% from 2016). With so many careers affected, the focus for organizations has shifted from preventing injuries to forecasting a player’s effectiveness and durability after surgery. This project trains machine learning models on historical MLB pitcher data to answer:
- **Will a pitcher be effective after Tommy John surgery?**  
  *A regression model predicts post-surgery XWOBA (expected weighted on-base average against), an industry-standard metric for pitcher effectiveness.*
- **Will a pitcher be durable after Tommy John surgery?**  
  *A classification model predicts whether a pitcher will reach 500 pitches thrown in their return season, answering whether they’ll be a reliable investment.*


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
