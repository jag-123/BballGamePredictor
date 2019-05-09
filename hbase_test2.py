import happybase
import csv

fileLocation = 'small.csv'
f = open(fileLocation)
reader = csv.DictReader(f)

connection = happybase.Connection(port=9090)

connection.create_table(
    'mytable3',
    {'cf1': dict()}
)

table = connection.table('mytable3')
i = 0
for row in reader:
    table.put(str(i),
        {'cf1:gameid': row['GAME_ID'],
        'cf1:time': row['PCTIMESTRING'],
        'cf1:period': row['PERIOD'],
        'cf1:score': row['SCORE'],
        'cf1:scoremargin': row['SCOREMARGIN']
        }
        )
    i+=1

