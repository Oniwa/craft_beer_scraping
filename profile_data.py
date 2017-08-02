from multiprocessing import freeze_support

import pandas as pd
import pandas_profiling
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

# Load CSV data sets
beers = pd.DataFrame.from_csv('d:\\code\\craft_scraping\\data\\processed\\'
                              'beers.csv', encoding='latin1')
breweries = pd.DataFrame.from_csv('d:\\code\\craft_scraping\\data\\processed\\'
                                  'breweries.csv', encoding='latin1')

# Merge the beer and breweries into one dataset
beers_and_breweries = pd.merge(beers,
                               breweries,
                               how='inner',
                               left_on="brewery_id",
                               right_on='id',
                               sort=True,
                               suffixes=('_beer', '_brewery')
                               )


# Function to determine custom categories of data
def get_var_category(series):
    unique_count = series.nunique(dropna=False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count == total_count:
        return 'Text (Unique)'
    else:
        return 'Categorical'


# Print the custom categories for a data frame
def print_categories(df):
    for column_name in df.columns:
        print(column_name, ": ", get_var_category(df[column_name]))

# print_categories(beers)
# print_categories(breweries)

# Return number of observations in a series regardless if data is
# missing or null
length = len(beers['ibu'])
# print(length)

# Return number of non-NA/non-Null observations in a series
count = beers['ibu'].count()
# print(count)

# Find percentage of missing values
number_of_missing_values = length - count
pct_of_missing_values = float(number_of_missing_values / length)
pct_of_missing_values = "{0:.1f}%".format(pct_of_missing_values*100)
# print(pct_of_missing_values)

# Find Min and Max value of IBU
# print("Minimum value: ", beers['ibu'].min())
# print("Maximum value: ", beers['ibu'].max())

# Find the most frequent IBU
# print(beers['ibu'].mode())

# Find the mean of the IBU
# print(beers['ibu'].mean())

# Find the IBU in the middle of the dataset
# print(beers['ibu'].median())

# Find the standard deviation of the IBU
# print(beers['ibu'].std())

# Split the data into a quartile
# print(beers['ibu'].quantile([.25, .5, .75]))

# Create a distribution plot
# should display in an ipython notebook
sns.distplot(beers["ibu"].dropna())

# Perform the Pearson correlation on the dataset
# print(beers[['abv', 'ibu', 'ounces']].corr())

# Summarize the categorical data
# print(beers[["name", "style"]].describe())

if __name__ == "__main__":
    freeze_support()
    # Use an out of the box data profiling tool
    # Looks like this is another thing that only works in ipython notebooks
    pandas_profiling.ProfileReport(beers_and_breweries)
