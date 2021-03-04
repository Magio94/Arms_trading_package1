import dash, dash_table, pandas as pd, webbrowser

#Prunes columns for example
df = pd.read_csv('0-Downloaded_files/arms_trade.csv')
df = df[['buyer', 'seller', 'desig2', 'desc', 'delyears', 'nrdel', 'tivunit', 'tivorder', 'tivdel']]

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {'name': 'buyer', 'id': 'buyer', 'type': 'text'},
        {'name': 'seller', 'id': 'seller', 'type': 'text'},
        {'name': 'desig2', 'id': 'desig2', 'type': 'text'},
        {'name': 'description', 'id': 'desc', 'type': 'text'},
        {'name': 'Year of delivery', 'id': 'delyears', 'type': 'text'},
        {'name': 'number of deliveries', 'id': 'nrdel', 'type': 'numeric'},
        {'name': 'tivunit', 'id': 'tivunit', 'type': 'numeric'},
        {'name': 'tivorder', 'id': 'tivorder', 'type': 'numeric'},
        {'name': 'tivdel', 'id': 'tivdel', 'type': 'numeric'},
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
    webbrowser.open_new( 'http://127.0.0.1:8000/' )
    app.run_server(debug=True, port= 8000, use_reloader=False)

# IT HAS TO BE CALLED AS A NORMAL LINK BECAUSE THE SERVER NEVER STOPS IF IT DIFFERENT
