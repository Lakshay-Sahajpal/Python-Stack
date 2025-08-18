import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r'code/owid-covid-data.csv.crdownload')
#print(df.head())
#print(df.isna().sum())

#print(df.columns)
#sns.heatmap(df.isna())
#plt.show()

#df['date'].info()
#print(df['date'].isna().sum())


#Converted Date in DateTime datatype, and setting it as index
Covid_df = df.copy()
#Covid_df.info()
Covid_df['date'] = pd.to_datetime(Covid_df['date'], errors = 'coerce')
#Covid_df['date'].info()

Covid_df.set_index('date', inplace=True)
Covid_df = Covid_df.drop(columns=['iso_code', 'continent','new_cases_smoothed','new_deaths_smoothed', 'total_cases_per_million','new_cases_per_million', 'new_cases_smoothed_per_million','total_deaths_per_million', 'new_deaths_per_million','new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients','icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions','weekly_icu_admissions_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand','new_tests_smoothed', 'new_tests_smoothed_per_thousand','positive_rate', 'tests_per_case', 'tests_units','new_vaccinations', 'new_vaccinations_smoothed','total_vaccinations_per_hundred', 'people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred','new_vaccinations_smoothed_per_million','new_people_vaccinated_smoothed','new_people_vaccinated_smoothed_per_hundred', 'stringency_index','median_age', 'aged_65_older', 'aged_70_older','gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate','diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'human_development_index','excess_mortality_cumulative_absolute', 'excess_mortality_cumulative','excess_mortality', 'excess_mortality_cumulative_per_million'])

#print(Covid_df)
India_df = Covid_df[Covid_df['location']=='India'].copy()

India_df.fillna(India_df.ffill(), inplace=True)

India_df.drop_duplicates(inplace=True)
print(India_df)

sns.heatmap(India_df.isna())
plt.show()
