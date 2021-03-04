import pandas as pd

data = pd.read_csv( r'0-Downloaded_files/ucdp-prio-acd-201-csv/ucdp-prio-acd-201.csv' )


##SPLIT COLUMN ALONG PARENTHESES

data[['newlocation','garbage']] = data.location.str.split('\(|\)', expand=True).iloc[:,[0,1]]


##SPLIT COLUMN ALONG COMA

data[['conflict_location','garbage2']] = data.newlocation.str.split(", ",expand=True,).iloc[:,[0,1]]

print(data)

data = data.drop(labels=["location", "side_a",
    "side_a_id",
    "side_a_2nd",
    "side_b",
    "side_b_id",
    "side_b_2nd",
    "incompatibility",
    "territory_name",
    "garbage",
    "garbage2",
    "newlocation",
    "start_prec",
    "start_date2",
    "start_prec2",
    "ep_end",
    "ep_end_date",
    "ep_end_prec",
    "gwno_a",
    "gwno_a_2nd",
    "gwno_b",
    "gwno_b_2nd",
    "gwno_loc",
    "region",
    "version",
    'newlocation',
    'garbage'], axis=1, inplace= False )


#REPLACEMENTS FOR JOIN BASED ON NAME IN CENTROID TABLE

data = data.replace(['DR Congo '],'Democratic Republic of The Congo')

data = data.replace(['Hyderabad'],'India')

data = data.replace(['Myanmar ', 'Myanmar'],'Myanmar/Burma')

data = data.replace(['United States of America'],'United States')

data = data.replace(['South Vietnam'],'Vietnam')

data = data.replace(['Bosnia-Herzegovina'],'Bosnia and Herzegovina')

data = data.replace(['South Yemen'],'Yemen')

data = data.replace(['Tanzania'],'United Republic of Tanzania')

print(data)