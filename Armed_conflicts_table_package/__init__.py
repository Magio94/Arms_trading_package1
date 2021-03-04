
# DOWNLOADS ARMED CONFLICTS TABLE
exec(open('Armed_conflicts_table_package/1_download_armed_conflicts_table.py').read())
print("Table with armed conflicts data downloaded")

# PROCESSES TABLE ON CONFLICTS TO FIT IN POSTGRES
exec(open('Armed_conflicts_table_package/2-process_armed_conflicts_table.py').read())
print("Table with armed conflicts data downloaded")

# CREATES THE TABLE TO UPLOAD ARMED CONFLICTS
input_command_database = """DROP TABLE IF EXISTS armed_conflicts;
                         CREATE TABLE IF NOT EXISTS armed_conflicts (id serial NOT NULL PRIMARY KEY,
                         index integer,
                         conflict_id integer,
                         year integer,
                         conflict_location varchar(50))"""

exec(open('Trade_register_table_package/5-execute_engine_command.py').read())
data.to_sql('armed_conflicts', engine, if_exists='replace')
print("The armed conflicts data table has been exported to SQL")

# CREATES THE JOIN FOR THE ARMS CONFLICT TABLE WITH THE SHP
input_command_database = """DROP TABLE IF EXISTS join_centroids;
                         CREATE TABLE join_centroids AS
                         (SELECT armed_conflicts.conflict_location, armed_conflicts.year,  
                         armed_conflicts.intensity_level, armed_conflicts.cumulative_intensity, 
                         armed_conflicts.start_date, armed_conflicts.type_of_conflict, centroids_states.geometry
                         FROM armed_conflicts
                         INNER JOIN centroids_states
                         ON centroids_states.\"NAME_ENGL\" = armed_conflicts.Conflict_location
                         GROUP BY centroids_states.\"NAME_ENGL\", armed_conflicts.Conflict_location,  
                         centroids_states.\"NAME_ENGL\", armed_conflicts.year, armed_conflicts.intensity_level, 
                         armed_conflicts.cumulative_intensity, armed_conflicts.start_date, 
                         armed_conflicts.type_of_conflict, centroids_states.geometry
                         ORDER BY centroids_states.\"NAME_ENGL\" ASC);"""
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())
print(
    "join_centroids table has been created by joining the world centroids shapefile and the armed conflicts table")

input_command_database = """DROP TABLE IF EXISTS agg_year_conflicts; 
                         CREATE TABLE agg_year_conflicts AS
                         (SELECT conflict_location, array_agg(DISTINCT(year)) as list_of_conflict_years, COUNT(year) 
                         as total_conflicts, COUNT ( DISTINCT year ) AS \"years_in_conflict\", geometry, ST_X(geometry) as lat, ST_Y(geometry) as lon
                         FROM join_centroids
                         GROUP BY conflict_location, geometry); """
exec(open('Trade_register_table_package/5-execute_engine_command.py').read())
