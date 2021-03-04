from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#UPGRADES THE SQL DATABASE  -upgrade the SQL Database after

mydb.set_isolation_level( ISOLATION_LEVEL_AUTOCOMMIT )
con = mydb.cursor()

con.execute(str(command_input1))
exists = con.fetchone()
if not exists:
    con.execute(str(command_input2))
    print( "\nimport_arms_db database already exists or it has been created successfully" )
if exists:
    print("\nimport_arms_db database already exists" )
mydb.commit()  # IMPORTANT TO SAVE THE CHANG

