import psycopg2, os
from time import sleep
from threading import Thread

# CHOOSES TO INVESTIGATE AN YEAR OR AN INTERVAL
choose_function = input(
     "Would you like to investigate a single year or an interval of several years?"
    "\n - Choose (y) if you would like to investigate a SINGLE year"
    "\n - Choose (i) if you would like to investigate an INTERVAL of several years\n\nWrite your input: ")

while True:
    if choose_function == 'I' or choose_function == 'i':
        print( "You selected to investigate an interval of several years" )

        # SELECTS THE INTERVAL OF INTEREST
        exec(open("common_actions/2b-if_user_select_interval.py").read())

        # DOWNLOADS THE TABLE ON ARMS TRADING FOR THE INTERVAL
        print( "\nThe table is being downloaded: \n" )
        exec(open("Trade_register_table_package/1-trade_register_table_download.py").read())
        break

    elif choose_function == 'Y' or choose_function == 'y':
        print( "You selected to investigate a single year" )

        # SELECTS THE YEAR OF INTEREST
        exec(open('common_actions/2a-if_user_select_year.py').read())
        year_input1 = year_input
        year_input2 = year_input

        # DOWNLOADS THE TABLE ON ARMS TRADING FOR SINGLE YEAR
        print( "\nThe table is being downloaded: \n" )
        exec(open("Trade_register_table_package/1-trade_register_table_download.py").read())
        break

    else:
        print( "Not a valid selection! Try again!:" )
        choose_function = input(
            "Would you like to investigate a single year or an interval of several years?"
            "\n - Choose (y) if you would like to investigate a SINGLE year"
            "\n - Choose (i) if you would like to investigate an INTERVAL of several years\n\nWrite your input: ")

# SAVES THE FILE ON ARMS TRADING AS CSV FOR REFERENCE
save_csv = "0-Downloaded_files/arms_trade.csv"
exec(open('common_actions/1-save_csv_tables.py').read())
print(
    "The arms trading file has been saved as a CSV in the folder where you are running this code for your reference.\n"
    "A preview will be printed below:\n " )

# CLEANS THE CSV TABLE FROM NOT NECESSARY PARTS AND SET IT TO BE IMPORTED TO SQL
exec(open('Trade_register_table_package/2-process_trade_register_table.py').read())
print( "\nThe CSV has been modified to be compatible with PostgreSQL." )

# PLOTS DOWNLOADED TABLE

while True:
    plot_table = input("\nWould you like to display the downloaded arms trading CSV data in a Dash table? "
                       "It will give you the opportunity to query the data. "
                       "\nChoose (y) if you would like to display the table, select any other character to "
                       "continue without displaying the table: ")
    if plot_table == "y" or  plot_table == "Y":
        snooziness = 4
        def some_task ():
            while True:
                exec(open('Trade_register_table_package/10-plot_total_table.py').read())
                pass
        t = Thread( target=some_task )
        t.daemon = True
        t.start()
        sleep( snooziness )
        break
    else:
        break

# INPUTS PASSWORD AND USER FOR POSTGRES. THE HOST AND PORT HAVE BEEN LEFT BY DEFAULT,
# IN CASE IT IS DIFFERENT, USER NEEDS TO CHANGE THEM INSIDE THE CODE
# BELOW:CHECKING IF CONFIG FILE EXISTS. THIS FILE IS STORING THE USER AND THE PASSWORD THE FIRST TIME THE CODE RUN
# SO THE USER DOES NOT NEED TO PUT THEM A SECOND TIME
try:
    if os.path.exists( 'config.py' ):
        from config import user, passwd

        mydb = psycopg2.connect( user=user, password=passwd, host="127.0.0.1", port="5432" )
        print("\nUser and password are already stored\n")
        pass
    else:
        while True:
            try:
                user = str( input(
                    "\nTo load the table in the SQL server PostgreSQL must be activated. Enter your username here: " ) )
                passwd = str( input( "Enter your password here: " ) )
                mydb = psycopg2.connect( user=user, password=passwd, host="127.0.0.1", port="5432" )
                # save input
                with open( "config.py", "w+" ) as file:
                    file.write( f"user = '{user}'\npasswd = '{passwd}'"
                                )
                break
            except:
                print( '\n**The username and/or password you entered are incorrect.  Please try again!**\n' )
except:
    print("The username and/or password stored are incorrect. Please input them again. ")
    while True:
        try:
            user = str( input(
                "\nTo load the table in the SQL server PostgreSQL must be activated. Please enter your username here: " ) )
            passwd = str( input( "Enter your password here:" ) )
            mydb = psycopg2.connect( user=user, password=passwd, host="127.0.0.1", port="5432" )
            # save input
            with open( "config.py", "w+" ) as file:
                file.write( f"user = '{user}'\npasswd = '{passwd}'"
                            )
            break
        except:
            print( '\n**The username and/or password you entered are incorrect.  Please try again!**\n' )

print( "Python is now connected to SQL" )

# CREATES THE DATABASE INSIDE SQL IF IT DOES NOT ALREADY EXIST
command_input1 = "SELECT datname FROM pg_catalog.pg_database WHERE datname = 'import_arms_db';"
command_input2 = 'CREATE DATABASE import_arms_db'
exec(open('Trade_register_table_package/3-create_database_in_SQL_server.py').read())

# EXPORTS THE ARMS TRADING TABLE INSIDE SQL CONNECTING FIRST TO THE DATABASE
exec(open('Trade_register_table_package/4-connection_SQL_database.py').read())
print( "Python is now connected to the SQL database" )

input_command_database = """DROP TABLE IF EXISTS arms_trade;
                         CREATE TABLE IF NOT EXISTS arms_trade (id serial NOT NULL PRIMARY KEY, 
                         tidn integer, 
                         buyercod varchar(50), 
                         sellercod varchar(50), 
                         dat integer,
                         odai varchar(10), 
                         onum integer, 
                         onai varchar(10),
                         ldat integer, 
                         term varchar(10), 
                         desig2 varchar(50),
                         wcat varchar(10), 
                         descr varchar(50), 
                         coprod varchar(10),
                         nrdel integer,
                         nrdelai varchar(10),
                         delyears varchar(50), 
                         buyer varchar(50), 
                         seller varchar(50), 
                         status varchar(10), 
                         tivunit double precision, 
                         tivorder double precision, 
                         tivdel double precision)"""

# THE MODULE 5 AND 6 HAVE BEEN LEFT DIVIDED BECAUSE MODULE 6
# IS ACTIVATED MULTIPLE TIMES IN THE PROGRAM WHILE MODULE 5 IS
# ACTIVATED ONLY ONCE BECAUSE IT HAS A SPECIALIZED PURPOSE
exec(open(
    'Trade_register_table_package/5-execute_engine_command.py').read())
data.to_sql( 'arms_trade', engine, if_exists='replace' )
print( "The arms trading data table has been successfully exported to SQL" )

# CREATE THE POSTGIS EXTENSION TO WORK WITH GEO FILES
input_command_database = """CREATE EXTENSION IF NOT EXISTS postgis; 
                         CREATE EXTENSION IF NOT EXISTS postgis_topology;"""
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())
print( "The PostGIS extension has been created in PostGreSQL if it was not already there" )

# DOWNLOAD THE SHP ON WORLD STATES
if os.path.exists('0-Downloaded_files/borders_world') is False or os.path.exists('0-Downloaded_files/centroid_by_world_state') is False:
    exec(open('Trade_register_table_package/6-download_geo_data.py').read())
    print(
        "\nThe shp on world states has been extracted and inserted in the "
        "borders_world and centroid_by_world_state folders" )
else:
    print("Shapefiles already downloaded")
    pass

# EXPORT THE SHP FILES INSIDE SQL
input_command_database = "DROP TABLE IF EXISTS borders_world;"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

read_geopandas = "0-Downloaded_files/borders_world/CNTR_RG_01M_2020_3857.shp"
table_name = "borders_world"
countries_gdf = exec(open('Trade_register_table_package/7-geopandas_to_postgis.py').read())

input_command_database = "DROP TABLE IF EXISTS centroids_states;"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

read_geopandas = "0-Downloaded_files/centroid_by_world_state/CNTR_LB_2020_3857.shp"
table_name = "centroids_states"
point_countries_gdf = exec(open('Trade_register_table_package/7-geopandas_to_postgis.py').read())

print( "The world states shapefile has been successfully exported to SQL" )

# RUNS COMMANDS INSIDE SQL TO ERASE ANTARCTICA FROM THE FINAL MAP LAYOUT
input_command_database = "ALTER TABLE borders_world ADD id serial NOT NULL PRIMARY KEY;"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

input_command_database = "ALTER TABLE centroids_states ADD id serial NOT NULL PRIMARY KEY;"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

input_command_database = "DELETE FROM borders_world WHERE \"NAME_ENGL\" = 'Antarctica';"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

input_command_database = "DELETE FROM centroids_states WHERE \"NAME_ENGL\" = 'Antarctica';"
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())
print( "The Antarctica feature was deleted to better fit the final intended map layout" )

# JOINS THE ARMS TRADING TABLE WITH THE SHP, ONE TIME FOR SELLERS, ONE TIME FOR BUYERS
input_command_database = """DROP TABLE IF EXISTS seller_borders_world; 
                         CREATE TABLE seller_borders_world as 
                         (SELECT seller, sellercod, (array_agg(DISTINCT(buyer))) as buyers, SUM(nrdel) as n_arms 
                         FROM arms_trade 
                         GROUP BY seller, sellercod); 

                         DROP TABLE IF EXISTS join_seller; 
                         CREATE TABLE join_seller as 
                         (SELECT borders_world.\"ISO3_CODE\", seller_borders_world.sellercod, 
                         borders_world.\"NAME_ENGL\", seller_borders_world.buyers, seller_borders_world.n_arms,
                         borders_world.\"geometry\" 
                         FROM borders_world 
                         INNER JOIN seller_borders_world 
                         ON borders_world.\"ISO3_CODE\" = seller_borders_world.sellercod 
                         OR borders_world.\"NAME_ENGL\" = seller_borders_world.seller 
                         GROUP BY borders_world.\"ISO3_CODE\", borders_world.\"NAME_ENGL\", 
                         seller_borders_world.sellercod, borders_world.\"NAME_ENGL\", seller_borders_world.buyers, 
                         seller_borders_world.n_arms, borders_world.\"geometry\" 
                         ORDER BY borders_world.\"NAME_ENGL\" ASC); """
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

input_command_database = """DROP TABLE IF EXISTS buyer_borders_world; 
                         CREATE TABLE buyer_borders_world as 
                         (SELECT buyer, buyercod, (array_agg(DISTINCT(seller))) as sellers, SUM(nrdel) as n_arms 
                         FROM arms_trade 
                         GROUP BY buyer, buyercod); 

                         DROP TABLE IF EXISTS join_buyer; 
                         CREATE TABLE join_buyer as 
                         (SELECT borders_world.\"ISO3_CODE\", buyer_borders_world.buyercod,
                         borders_world.\"NAME_ENGL\", buyer_borders_world.sellers, buyer_borders_world.n_arms, 
                         borders_world.\"geometry\" 
                         FROM borders_world 
                         INNER JOIN buyer_borders_world 
                         ON borders_world.\"ISO3_CODE\" = buyer_borders_world.buyercod 
                         OR borders_world.\"NAME_ENGL\" = buyer_borders_world.buyer 
                         GROUP BY borders_world.\"ISO3_CODE\", borders_world.\"NAME_ENGL\", 
                         buyer_borders_world.buyercod, borders_world.\"NAME_ENGL\", buyer_borders_world.sellers, 
                         buyer_borders_world.n_arms, borders_world.\"geometry\" 
                         ORDER BY borders_world.\"NAME_ENGL\" ASC); """
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

print(
    "Two new tables have been created.  These tables will be used to join the"
    " world states shp file with the arms trade data table."
    "\nOne table was joined based on sellers, the other based on buyers\n" )

input_command_database = """DROP TABLE IF EXISTS by_group_sellers_buyers; 
                         CREATE TABLE by_group_sellers_buyers as 
                         (SELECT seller, (array_agg(DISTINCT(buyer))) as buyers, SUM(nrdel) as n_arms  
                         FROM arms_trade 
                         GROUP BY seller); """
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())

print( "A table has been created grouping buyers and sellers in SQL" )

# EXECUTES MODULE ON CONFLICTS
print("Now the module on conflicts will be run")
exec(open('Armed_conflicts_table_package/__init__.py').read())

# IMPORTS THE FILE IN PYTHON
name_table_import = "borders_world"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
borders_world = import_variable

name_table_import = "join_seller"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
state_sellers = import_variable

name_table_import = "join_buyer"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
state_buyers = import_variable

name_table_import = "centroids_states"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
centroids_states = import_variable

name_table_import = "agg_year_conflicts"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
agg_year_conflicts = import_variable

name_table_import = "join_centroids"
exec(open('Trade_register_table_package/8-postgis_to_geopandas.py').read())
join_centroids = import_variable

state_sellers['n_arms'] = state_sellers['n_arms'].astype(float)
state_buyers['n_arms'] = state_buyers['n_arms'].astype(float)
agg_year_conflicts['lat'] = agg_year_conflicts['lat'].astype(float)
agg_year_conflicts['lon'] = agg_year_conflicts['lon'].astype(float)
agg_year_conflicts['years_in_conflict'] = agg_year_conflicts['years_in_conflict'].astype(float)

print( "\nAfter processing the data in PostgreSQL, the tables have been imported into Python to be plotted.\n " )

# PLOTS THE FILES IMPORTED IN PYTHON WITH PLOTLY OR MATPLOTLIB DEPENDING ON COMPATIBILITY
# THE PROGRAM FIRST ATTEMPTS TO PLOT WITH PLOTLY, BUT THIS ONE CAN MANAGE EMPTY SPACE IN THE TABLE,
# SO IF IT FIND MISTAKE IT PLOT WITH MATPLOTLIB

while True:
    try:
        choose_function = input(
            "Would you like to plot with Folium or matplotlib?\nThe first one is a Choropleth, "
            "while the second is saved as pdf and shows also the conflicts table as layer?"
            "\n - Choose (f) if you would like to plot with folium"
            "\n - Choose (m) if you would like to plot with matplotlib\n\nWrite your input: ")
        if choose_function == 'F' or choose_function == 'f':
            exec(open('Trade_register_table_package/9a-plot_with_Folium.py').read())
            break
        elif choose_function == 'M' or choose_function == 'm':
            exec(open('Trade_register_table_package/9b-plot_with_matplotlib.py').read())
            break
        else:
            print("Not a valid selection! Try again!:")
    except:
        print("Your choice had a problem! Try to plot with the other one\n")

# PLOTS TABLE BY GROUP
snooziness = 4
def some_task ():
    while True:
        exec(open('Trade_register_table_package/11-plot_group_by_table.py').read())
        pass
t = Thread( target=some_task )
t.daemon = True
t.start()
sleep( snooziness )

snooziness = 4
def some_task ():
    while True:
        exec(open('Armed_conflicts_table_package/3-plot_conflicts_table.py').read())
        pass
t = Thread( target=some_task )
t.daemon = True
t.start()
sleep( snooziness )

# CLOSES CONNECTIONS TO THE DATABASE AND SERVER
engine.execute( "REVOKE CONNECT ON DATABASE import_arms_db FROM public;" )
engine.dispose()
mydb.close()
