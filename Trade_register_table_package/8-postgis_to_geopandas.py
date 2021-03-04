import geopandas as gpd
from sqlalchemy import create_engine

engine = create_engine( 'postgresql+psycopg2://' + user + ':' + passwd + '@localhost/import_arms_db' )

sql_import = "SELECT * FROM " + name_table_import + ";"

import_variable = gpd.GeoDataFrame.from_postgis(sql_import, engine, geom_col='geometry', crs={'init': 'epsg:3857'},
                                                coerce_float=False)
