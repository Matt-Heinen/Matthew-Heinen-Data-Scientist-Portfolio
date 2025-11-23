# Effects of Social Media on Emotional Wellbeing

This project explores the impact of social media and technology use on happiness, mental health, and productivity by analyzing public datasets and building statistical and machine learning models. The study seeks to quantify the relationships, both positive and negative, between social media engagement and emotional wellbeing.

## Description

The RMarkdown file presents a comprehensive analysis using data science techniques to address the following questions:
- Does increased social media use correlate with depression?
- In what ways does social media contribute to feelings of connectedness?
- How do different platforms affect productivity?
- Is there a relationship between social media usage and antidepressant use?
- How does screen time influence mental health and productivity?
- What are the effects of deleting social media platforms on user wellbeing?

Several datasets are combined, cleaned, and transformed to create quarterly, annual, and biannual analytic views. These are then used to run correlation, regression, and T-tests, as well as to visualize findings using heatmaps, scatter plots, and box plots.

## Getting Started

### Dependencies

- R (>= 4.0 recommended)
- RStudio (for best experience)
- The following R packages:
  - readxl
  - ggplot2
  - dplyr
  - ggthemes
  - reshape2
  - scales
  - purrr
  - stringr
  - plyr
  - car

### Installing

Install R packages in your R console:

```r
install.packages(c("readxl", "ggplot2", "dplyr", "ggthemes", "reshape2", "scales", "purrr", "stringr", "plyr", "car"))
```

### Executing Program

1. Download all data files referenced in the RMarkdown (Excel, CSV) to the working directory.
2. Open `Effects of Social Media on Emotional Wellbeing.Rmd` in RStudio.
3. Update any file paths in the R code chunks as needed for your local setup.
4. Click "Knit" to produce the PDF output with all analysis, code, and results.

## Authors

Matthew Heinen  
Email: matthew.heinen@my365.bellevue.edu

## Version History

1.0 Initial Release

## Acknowledgments


Braghieri, Luca, Levy, Ro’ee, and Makarin, Alexey. Data and Code for: Social Media and Mental Health. Nashville, TN: American Economic Association [publisher], 2022. Ann Arbor, MI: Inter-university Con- sortium for Political and Social Research [distributor], 2022-10-19. https://doi.org/10.3886/E175582V1
Centers for Disease Control and Prevention. (2024, February 1). CDC - NCHS - National Center for Health Statistics. Antidepressant Use Among Adults: United States, 2015-2018. https://www.cdc.gov/nchs/ data/databriefs/db377-tables-508.pdf#page=4
Google Trends. (n.d.). connected+friends+fellowship+companion. Google Trends. https://trends. google.com/trends/explore?date=2009-01-01%202023-06-30&geo=US&q=connected%2Bfriends% 2Bfellowship%2Bcompanion,%22Feel%20connected%20with%20friends%22&hl=en-US
Google Trends. (n.d.). “Social Media” Depression Term Interest in the US. Google trends. https: //trends.google.com/trends/explore?date=2008-09-01%202023-06-15&geo=US&q=%22Social% 20Media%22%20depression&hl=en-US
Google Trends. (n.d.). Vine, Mental Health, Suicide+Depression+Anxious+Anxiety. https://trends.google. com/trends/explore?date=2017-01-10%202017-01-24&geo=US&q=Vine,Mental%20Health,Happy, Suicide%2BDepression%2BAnxiety%2BAnxious
Howarth, J. (2023, December 4). Alarming average screen time statistics (2024). Exploding Topics. https: //explodingtopics.com/blog/screen-time-stats#us-average-screen-time
Sharma, A. (2021, August 28). Monthly active users of Facebook. Kaggle. https://www.kaggle.com/ datasets/adityasharmaop/monthly-active-users-of-facebook?resource=download
Tiktok revenue and Usage Statistics (2023). Business of Apps. (2023, May 3). https://www.businessofapps. com/data/tik-tok-statistics/
U.S. Bureau of Labor Statistics. (2023, March 23). Tables. U.S. Bureau of Labor Statistics. https: //www.bls.gov/productivity/tables/
Wikimedia Foundation. (2023, June 13). Vine (service). Wikipedia. https://en.wikipedia.org/wiki/Vine_ (service)#:~:text=Bought%20by%20Twitter%2C%20Inc.,discontinued%20a%20few%20months%20later.&text=Developer ,Vine%20Labs%2C%20Inc,(Twitter%2C%20Inc.)