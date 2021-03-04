import csv

with open(str(save_csv), 'w' ) as f:
    writer = csv.writer( f )
    for line in response.iter_lines():
        writer.writerow( line.decode( 'utf-8', errors='replace' ).split( ',' ) )