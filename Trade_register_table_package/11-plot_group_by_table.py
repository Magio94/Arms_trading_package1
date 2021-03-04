import dash, dash_table, pandas as pd, webbrowser
from sqlalchemy import create_engine

engine = create_engine( 'postgresql+psycopg2://' + user + ':' + passwd + '@localhost/import_arms_db' )

#CALLS THE GEOMETRICAL FILES

df = pd.read_sql_query("SELECT * FROM by_group_sellers_buyers;",
                       con=engine)
list_print = df['buyers']
df['buyers'] = [str( i ) for i in df['buyers']]

print("Plotting in progress..... Two maps will be created shortly, one for the\n"
      "sellers and one for the buyers. Thank you for your patience")

#Prunes columns for example

by_group_sellers_buyers = df[['seller', 'buyers', 'n_arms']]

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {'name': 'seller', 'id': 'seller', 'type': 'text'},
        {'name': 'buyers', 'id': 'buyers', 'type': 'text'},
        {'name': 'number of deliveries', 'id': 'n_arms', 'type': 'numeric'},
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={'overflowX': 'auto'},

    style_cell={
        'height': 'auto',
        'width': 'auto',
    },
)


if __name__ == '__main__':
    webbrowser.open_new( 'http://127.0.0.1:8001/' )
    app.run_server(debug=True, port= 8001, use_reloader=False)

# IT HAS TO BE CALLED AS A NORMAL LINK BECAUSE THE SERVER NEVER STOP IF IT IS DIFFERENT