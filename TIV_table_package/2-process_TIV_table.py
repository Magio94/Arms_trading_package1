import pandas as pd

# Adds "r" for windows compatibility for back slash "\"
table_downloaded = pd.read_csv( r'' + str( csv_table ) + '', sep=',' )

# Changes all "NaN" values into "0" for entire dataframe
# Uses the downcast to convert the datatype from float to integer
table_downloaded.fillna( value=0, axis=1, inplace=True, downcast='infer' )

# Drops first 8 rows in dataframe. The raw SIPRI table includes metadata in these first 8 rows
table_downloaded.drop( table_downloaded.head( 9 ).index, inplace=True )

# Drops last 2 empty columns
table_downloaded = table_downloaded.iloc[:, :-2]

# Sets the first row of the "cleaned" csv as the table header
new_header = table_downloaded.iloc[0]
table_downloaded = table_downloaded[1:]
table_downloaded.columns = new_header

# Changes the first column name from "0" to "Country"
table_downloaded.rename( columns={0: 'Country'}, inplace=True )

# Converts the "1950" column to an integer datatype
table_downloaded['1950'] = table_downloaded['1950'].astype( 'int64' )

# Converts the "Total" column from object to integer
table_downloaded['Total'] = pd.to_numeric( table_downloaded['Total'], errors='coerce' )

# Converts column names to strings so they can be used as user input
table_downloaded.columns = table_downloaded.columns.astype( "str" )

# Erases rows where "Country" reads "0"
index_names = table_downloaded[table_downloaded['Country'] == 0].index
table_downloaded.drop( index_names, inplace=True )

# Erases rows where "Country" reads "Total" so it doesn't display in the tree map
index_names = table_downloaded[table_downloaded['Country'] == 'Total'].index
table_downloaded.drop( index_names, inplace=True )


# Use "melt" to re-organize data frame variables and format
table_to_process = pd.melt( table_downloaded, id_vars=["1950", "1951", "1952", "1953", "1954", "1955", "1956",
                                                       "1957", "1958", "1959","1960","1961","1962","1963","1964",
                                                       "1965","1966","1967","1968","1969","1970","1971","1972","1973",
                                                       "1974","1975","1976","1977","1978","1979","1980","1981","1982",
                                                       "1983","1984","1985","1986","1987","1988","1989","1990","1991",
                                                       "1992","1993","1994","1995","1996","1997","1998","1999","2000",
                                                       "2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018",
                                                       "2019"
                                       ,"Total"],
                            value_vars=["Country"] )

# Drops the second to last column as it is randomly generated data
table_to_process = table_to_process.drop( table_to_process.columns[-2], axis=1 )

# Changes the first column name from "0" to "Country"
table_to_process.rename( columns={'value': 'Country'}, inplace=True )

table_to_process.to_csv( str( file_name ), sep=',', encoding='utf-8' )

# Prints tables to confirm edits
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print( table_to_process )

