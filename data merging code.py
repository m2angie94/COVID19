#import libraries for data manipulation
import pandas as pd
import numpy as np

# import data files
df1 = pd.read_csv("covid_data.csv")
df2 = pd.read_csv("government_effectiveness.csv")
df3 = pd.read_csv("nurses_and_midwives.csv")
df4 = pd.read_csv("physicians.csv")

# replace location names in Covid dataset to match other datasets
df1['location'].replace(['Bahamas', 'Brunei', 'Congo', 'Democratic Republic of Congo', "Cote d'Ivoire", "Egypt", \
            "Hong Kong", "Iran", "Jersey", "Kyrgyzstan", "Laos", "Macedonia", \
            "Russia", "Sao Tome and Principe", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", \
            "Slovakia", "South Korea", "Syria", "Taiwan", "Timor", "United States Virgin Islands", \
            "Venezuela", "Yemen"], \
            ['Bahamas, The', 'Brunei Darussalam', 'Congo, Rep.', 'Congo, Dem. Rep.', "Côte d'Ivoire", "Egypt, Arab Rep.", \
            "Hong Kong SAR, China", "Iran, Islamic Rep.", "Jersey, Channel Islands", "Kyrgyz Republic", "Lao PDR", "Macedonia, FYR", \
            "Russian Federation", "São Tomé and Principe", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", \
            "Slovak Republic", "Korea, Rep.", "Syrian Arab Republic", "Taiwan, China", "Timor-Leste", "Virgin Islands (U.S.)", \
            "Venezuela, RB", "Yemen, Rep."], inplace=True)

# join 1st file to #2nd file on the country names
join_1 = df1.merge(df2, left_on='location', right_on='Country', how='left')

# Join first two datasets to 3rd dataset on the country names
join_1 = join_1.merge(df4, left_on='location', right_on='Country Name', how='left')

# Join previous datasets to 4th dataset on the country names
join_1 = join_1.merge(df3, left_on='location', right_on='country', how='left')

# create subsets of columns for final export on the country names
final = join_1[['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
       'new_cases_smoothed', 'total_deaths', 'new_deaths',
       'new_deaths_smoothed', 'total_cases_per_million',
       'new_cases_per_million', 'new_cases_smoothed_per_million',
       'total_deaths_per_million', 'new_deaths_per_million',
       'new_deaths_smoothed_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
       'tests_per_case', 'positive_rate', 'tests_units', 'stringency_index',
       'population', 'population_density', 'median_age', 'aged_65_older',
       'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index',
       'Governance Index','Physicians per 1000',
       'nurses_and_midwives']]

# rename some columns
final.columns = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
       'new_cases_smoothed', 'total_deaths', 'new_deaths',
       'new_deaths_smoothed', 'total_cases_per_million',
       'new_cases_per_million', 'new_cases_smoothed_per_million',
       'total_deaths_per_million', 'new_deaths_per_million',
       'new_deaths_smoothed_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
       'tests_per_case', 'positive_rate', 'tests_units', 'stringency_index',
       'population', 'population_density', 'median_age', 'aged_65_older',
       'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index', 'governance_index',
       'physicians_per thousand', 'nurses_and_midwives_per_thousand']

# Export final dataset
final.to_csv("joined.csv")