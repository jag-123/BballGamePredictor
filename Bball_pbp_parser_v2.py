import csv

with open('2017-18_pbp.csv') as read_file:
    csv_reader = csv.reader(read_file, delimiter=',')
    line_number = 0
    for row in csv_reader:
        if line_number == 0:
            pass
            line_number+=1
        elif line_number == 1:
            current_game_id = row[4]
            line_number+=1
            break
        else:
            break

print(current_game_id)
with open('2017-18_pbp.csv') as read_file:
    csv_reader = csv.reader(read_file, delimiter=',')
    time_strings = []
    periods = []
    scores = []
    score_margins = []

    line_number = 0
    look_for_one = False
    last_rows = []
    for row in csv_reader:
        if line_number == 0:
            first_row = [row[7],row[8],row[30],row[31]]
            line_number+=1
        else:
            game_id = row[4]
            if game_id != current_game_id:
                with open('2017-18_games/{}.csv'.format(current_game_id),'w') as write_file:
                    writer = csv.writer(write_file)
                    writer.writerow(first_row)
                    rows = zip(time_strings,periods,scores,score_margins)
                    for row2 in rows:
                        if row2[2] == '':
                            pass
                        else:
                            writer.writerow(row2)
                    current_game_id = game_id
                    time_strings = [row[7]]
                    periods = [row[8]]
                    scores = [row[30]]
                    score_margins = [row[31]]
            else:
                time_string = row[7]
                period = row[8]
                if int(period) != 1:
                    look_for_one = True
                if int(period) == 1 and look_for_one:
                    last_rows.append(line_number)
                    look_for_one = False
                score = row[30]
                score_margin = row[31]

                time_strings.append(time_string)
                periods.append(period)
                scores.append(score)
                score_margins.append(score_margin)
                line_number+=1

# final_scores = []
# with open('2017-18_pbp.csv') as read_file:
#     csv_reader = csv.reader(read_file, delimiter=',')
#     for i, row in enumerate(csv_reader):
#         if i+1 in last_rows:
#             final_scores.append(row[30])

# win_list = []
# for score in final_scores:
#     if len(score) != 0:
#         score_list = list(score.split())

#         if int(score_list[0]) > int(score_list[-1]):
#             win_list.append('AWAY')
#         elif int(score_list[-1]) > int(score_list[0]):
#             win_list.append('HOME')
#         else:
#             raise ValueError('theres a problem')

# print(win_list)
# print(len(win_list))

# with open('2017-18_games.csv','w') as write_file:
#     writer = csv.writer(write_file)
#     writer.writerow(first_row)
#     rows = zip(time_strings,periods,scores,score_margins)
#     for row in rows:
#         if row[2] == '':
#             pass
#         else:
#             writer.writerow(row)