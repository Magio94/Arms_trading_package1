import requests
#DOWNLOADS ARMS TRADE DATA FROM SOURCE
data = {
    'low_year': year_input1,
    'high_year': year_input2,
    'seller_country_code': '',
    'buyer_country_code': '',
    'armament_category_id': 'any',
    'buyers_or_sellers': 'sellers',
    'filetype': 'csv',
    'include_open_deals': 'on',
    'sum_deliveries': 'on',
    'Submit4': 'Download'
}

response = requests.post( 'http://armstrade.sipri.org/armstrade/html/export_trade_register.php', data=data )

