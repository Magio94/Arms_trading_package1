import dash, dash_table, pandas as pd, webbrowser
from sqlalchemy import create_engine

engine = create_engine( 'postgresql+psycopg2://' + user + ':' + passwd + '@localhost/import_arms_db' )

df = pd.read_sql_query("SELECT * FROM join_centroids;",
                       con=engine)

#PRUNES COLUMNS FOR EXAMPLE
df = df[['conflict_location', 'year', 'intensity_level', 'cumulative_intensity', 'start_date', 'type_of_conflict']]

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {'name': 'conflict_location', 'id': 'conflict_location', 'type': 'text'},
        {'name': 'year', 'id': 'year', 'type': 'numeric'},
        {'name': 'intensity_leve', 'id': 'intensity_level', 'type': 'numeric'},
        {'name': 'cumulative_intensity', 'id': 'cumulative_intensity', 'type': 'numeric'},
        {'name': 'start_date', 'id': 'start_date', 'type': 'text'},
        {'name': 'type_of_conflict', 'id': 'type_of_conflict', 'type': 'numeric'},
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)

if __name__ == '__main__':
    webbrowser.open_new( 'http://127.0.0.1:8002/' )
    app.run_server(debug=True, port= 8002, use_reloader=False)

# IT HAS TO BE CALLED AS A NORMAL LINK BECAUSE THE SERVER NEVER STOP IF DIFFERENT
