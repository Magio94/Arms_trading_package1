from sqlalchemy import create_engine

engine = create_engine( 'postgresql+psycopg2://' + user + ':' + passwd + '@localhost/import_arms_db' )

