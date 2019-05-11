import happybase
import csv
from win_list import win_list


fileLocation = '2017-18_games.csv'
connection = happybase.Connection(port=9090)

def populate_table(file_loc):
    """
    Populate HBase table with data from csv file.
    The location of csv file is given to this fuction as an argument.
    """
    table = connection.table('mytable')

    f = open(fileLocation)
    reader = csv.DictReader(f)

    cf_dict = {}
    for i in range(len(win_list)):
        name = "cf" + str(i)
        cf_dict[name] = dict()

    connection.create_table(
        'mytable',
        cf_dict
    )

    i = 0
    gameNum = 0
    look_for_one = False
    for row in reader:
        if i == 0:
            pass
        if look_for_one and row['PERIOD'] == '1':
            look_for_one = False
            gameNum+= 1
        if row['PERIOD'] != '1':
            look_for_one = True
        cfName = 'cf'+str(gameNum)
        rowid = row['SCOREMARGIN'] + '-' + str(i)
        try:
            table.put(rowid,
                {cfName+':time': row['PCTIMESTRING'],
                cfName+':period': row['PERIOD'],
                cfName+':score': row['SCORE'],
                cfName+':scoremargin': row['SCOREMARGIN'],
                cfName+':whowon': win_list[gameNum]
                }
                )
        except IndexError:
            print('gameNum: ', gameNum)
        finally:
            i+=1

margin = "20"
quarter = "4"
def run_calculator(score_margin, quarter_num):
    table = connection.table('mytable')

    for key, data in table.scan(row_prefix=score_margin):
        if data['cf1:period'] == quarter:
            print(key,data)
            print('WHO WON?: ', data['cf1:whowon'])
        print(key,data)