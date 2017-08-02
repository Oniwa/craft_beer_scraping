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


