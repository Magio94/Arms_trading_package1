import geopandas as gpd
from sqlalchemy import create_engine

engine = create_engine( 'postgresql+psycopg2://' + user + ':' + passwd + '@localhost/import_arms_db' )

gdf = gpd.read_file(str(read_geopandas))
gdf.to_postgis(name=str(table_name), con=engine)