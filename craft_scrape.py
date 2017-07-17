from urllib.request import urlopen

from bs4 import BeautifulSoup
import pandas as pd
import re


# Determines if a table_row is a beer entry
def is_beer_entry(table_row):
    row_cells = table_row.findAll("td")
    beer_id = get_beer_id(row_cells[0].text)
    return len(row_cells) == 8 and beer_id


# Return the beer entry numerical identifier from the "Entry" column
def get_beer_id(cell_value):
    r = re.match("^(\d{1,4})\.$", cell_value)
    if r and len(r.groups()) == 1:
        beer_id = r.group(1)
        return int(beer_id)
    else:
        return None


# Store beers in a JSON formatted dictionary
def get_all_beers(html_soup):
    beers = []
    all_rows_in_html_page = html_soup.findAll("tr")
    for table_row in all_rows_in_html_page:
        if is_beer_entry(table_row):
            row_cells = table_row.findAll("td")
            beer_entry = {
                "id": get_beer_id(row_cells[0].text),
                "name": row_cells[1].text,
                "brewery_name": row_cells[2].text,
                "brewery_location": row_cells[3].text,
                "style": row_cells[4].text,
                "size": row_cells[5].text,
                "abv": row_cells[6].text,
                "ibu": row_cells[7].text
            }
            beers.append(beer_entry)
    return beers


html = urlopen("http://craftcans.com/db.php?search=all&sort=beerid&"
               "ord=desc&view=text")
html_soup = BeautifulSoup(html, 'html.parser')
beers_list = get_all_beers(html_soup)

print('done')
