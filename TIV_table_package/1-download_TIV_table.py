import requests

tivdataimp = {
    'import_or_export': choose_import_or_export,
    'country_code': '',
    'low_year': '1950',
    'high_year': '2019',
    'summarize': 'country',
    'filetype': 'csv',
    'Action': 'Download'
}

response = requests.post( 'http://armstrade.sipri.org/armstrade/html/export_values.php', data=tivdataimp )
