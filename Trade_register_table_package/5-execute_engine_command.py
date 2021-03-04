#Here engine is utilized to refer directly to the database

#Here psycopg2.connect is utilized to save the changes in the server and database


engine.execute(str(input_command_database))
mydb.commit()
print( "\nEngine executed" )