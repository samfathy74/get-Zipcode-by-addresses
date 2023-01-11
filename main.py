import pandas as pd
from uszipcode import SearchEngine

#create example for addresses data 
data = {'Address': ['1600 Pennsylvania Avenue NW NW', '4301 1st Ave SE', '400 W N Avenue',
                   '100 S Main St', '400 N Tampa St', '56 W Center St', '300 W Broadway', '1000 Park Ave',
                   '100 W 5th St', '200 N Elm St', '100 W Madison St', '500 S Hope St', '100 N Los Angeles St',
                   '1000 Park Ave', '300 S Broad St', '100 S Hope St', '100 W California St', '100 N Miami St',
                   '300 W Broadway', '200 S Elm St'],
         'City': ['Washington', 'Cedar Rapids', 'Ankeny', 'San Francisco', 'Tampa', 'Provo', 'Los Angeles',
                  'New York', 'Cincinnati', 'Greensboro', 'Chicago', 'Los Angeles', 'Los Angeles', 'Philadelphia',
                  'Los Angeles', 'Los Angeles', 'San Francisco', 'Miami', 'Los Angeles', 'Greenville'],
         'State': ['DC', 'IA', 'IA', 'CA', 'FL', 'UT', 'CA', 'NY', 'OH', 'NC', 'IL', 'CA', 'CA', 'PA', 'CA', 'CA', 'CA', 'FL', 'CA', 'SC']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel('contacts.xlsx', index=False)


# Initialize the search engine
search = SearchEngine()
# Read in the Excel file
df = pd.read_excel('contacts.xlsx')
# Add a new column for the zip codes
df['zip_code'] = None


# Iterate through the rows of the DataFrame
for i, row in df.iterrows():
    address = row['Address']
    city = row['City']
    state = row['State']
    result = search.by_city_and_state(city=city, state=state)
    if len(result) > 0:
        # fill DataFrame or excel file with zip code beside to address.
        df.at[i, 'zip_code'] = result[0].zipcode
        # print(f"[{i}] County:{result[0].county}, City:{result[0].major_city}, State:{result[0].state} ==>> Zip Code:{result[0].zipcode}")


# Save the DataFrame with the new zip codes to a new Excel file
df.to_excel('contacts_with_zip.xlsx', index=False)