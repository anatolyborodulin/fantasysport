from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import json
from import_requests import get_html
from database_connection import db_session, GoalkeeperStats, PlayersStats

timestamp = datetime.now()

html = get_html('http://www.khl.ru/stat/players/468/')

soup = BeautifulSoup(html, 'html.parser')

# Import goalkeeper table header

# raw_table_header = soup.find(id='goalies_dataTable').find_all('th')
# table_header = []
# for record in raw_table_header:
#     record = record.get('title')
#     if record == None:
#         record = 0
#     table_header.append(record)
# print(table_header)

# Import table body

script = soup.find_all('script')[17].string
pattern = re.compile('var goalies_Data = (.+);\n')
script_search = pattern.search(script)

raw_player_data = json.loads(script_search.groups()[0])
player_data = {}

for record in raw_player_data:
    for i, a in enumerate(record):
        if i == 0:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            # player_id = data.find('a').get('href')
            player_name = data.find(class_='e-player_name').text
            player_data[player_name] = []
            player_data[player_name].append(player_name)

        elif i == 2:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            data = data.find('a').text
            player_data[player_name].append(data)

        else:
            if a == '-':
                a = '0'
            player_data[player_name].append(a)


for i, record in enumerate(player_data):
    player_up = {
    'player_name' : player_data[record][0],
    'shirt_num' : player_data[record][1],
    'player_club' : player_data[record][2],
    'games_played' : player_data[record][3],
    'games_won' : player_data[record][4],
    'games_lost' : player_data[record][5],
    'games_bullit' : player_data[record][6],
    'shots_on_goal' : player_data[record][7],
    'goals' : player_data[record][8],
    'goals_denied' : player_data[record][9],
    'percent_of_denied' : player_data[record][10],
    'quality_coef' : player_data[record][11],
    'goals_scored' : player_data[record][12],
    'pass_with_goal' : player_data[record][13],
    'games_no_goal' : player_data[record][14],
    'penaly_time' : player_data[record][15],
    'time_on_ice' : player_data[record][16],
    'version_datetime' : timestamp
    }
    
    player_up = GoalkeeperStats(player_up['player_name'], int(player_up['shirt_num']), player_up['player_club'], int(player_up['games_played']),
        int(player_up['games_won']), int(player_up['games_lost']), int(player_up['games_bullit']), int(player_up['shots_on_goal']), int(player_up['goals']), 
        int(player_up['goals_denied']), float(player_up['percent_of_denied']), float(player_up['quality_coef']), int(player_up['goals_scored']), 
        int(player_up['pass_with_goal']), int(player_up['games_no_goal']), int(player_up['penaly_time']), player_up['time_on_ice'], player_up['version_datetime']) 
    
    db_session.add(player_up)

# defencemen_data collection
script = soup.find_all('script')[18].string
pattern = re.compile('var defenses_Data = (.+);\n')
script_search = pattern.search(script)

raw_player_data = json.loads(script_search.groups()[0])
player_data = {}

for record in raw_player_data:
    for i, a in enumerate(record):
        if i == 0:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            # player_id = data.find('a').get('href')
            player_name = data.find(class_='e-player_name').text
            player_data[player_name] = []
            player_data[player_name].append(player_name)

        elif i == 2:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            data = data.find('a').text
            player_data[player_name].append(data)

        else:
            if a == '-':
                a = '0'
            player_data[player_name].append(a)

for i, record in enumerate(player_data):
    player_up = {
    'player_name' : player_data[record][0],
    'shirt_num' : player_data[record][1],
    'player_club' : player_data[record][2],
    'games_played' : player_data[record][3],
    'goals_scored' : player_data[record][4],
    'passes_on_goal' : player_data[record][5],
    'gp_points' : player_data[record][6],
    'plus_minus' : player_data[record][7],
    'penaly_time' : player_data[record][8],
    'goals_equal_teams' : player_data[record][9],
    'goals_advantage' : player_data[record][10],
    'goals_disadvantage' : player_data[record][11],
    'goals_overtime' : player_data[record][12],
    'goals_decisive' : player_data[record][13],
    'bullit_decisive' : player_data[record][14],
    'shots_on_goal' : player_data[record][15],
    'percent_of_shots_scored' : player_data[record][16],
    'average_shots' : player_data[record][17],
    'faceoffs_taken' : player_data[record][18],
    'faceoff_won' : player_data[record][19],
    'faceoff_percentage' : player_data[record][20],
    'average_time_on_ice' : player_data[record][21],
    'average_substitutes' : player_data[record][22],
    'opponent_hits' : player_data[record][23],
    'blocked_shots' : player_data[record][24],
    'fouls_accepted' : player_data[record][25],
    'version_datetime' : timestamp,
    'player_position' : 'Защитник'
    }
    
    player_up = PlayersStats(player_up['player_name'], int(player_up['shirt_num']), player_up['player_club'], int(player_up['games_played']),
        int(player_up['goals_scored']), int(player_up['passes_on_goal']), int(player_up['gp_points']), int(player_up['plus_minus']),
        int(player_up['penaly_time']), int(player_up['goals_equal_teams']), int(player_up['goals_advantage']), int(player_up['goals_disadvantage']),
        int(player_up['goals_overtime']), int(player_up['goals_decisive']), int(player_up['bullit_decisive']), int(player_up['shots_on_goal']),
        float(player_up['percent_of_shots_scored']), float(player_up['average_shots']), int(player_up['faceoffs_taken']), int(player_up['faceoff_won']),
        float(player_up['faceoff_percentage']), player_up['average_time_on_ice'], float(player_up['average_substitutes']), int(player_up['opponent_hits']),
        int(player_up['blocked_shots']), int(player_up['fouls_accepted']), player_up['version_datetime'], player_up['player_position']) 
    
    db_session.add(player_up)

# forwards_data collection
script = soup.find_all('script')[19].string
pattern = re.compile('var forwards_Data = (.+);\n')
script_search = pattern.search(script)

raw_player_data = json.loads(script_search.groups()[0])
player_data = {}

for record in raw_player_data:
    for i, a in enumerate(record):
        if i == 0:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            # player_id = data.find('a').get('href')
            player_name = data.find(class_='e-player_name').text
            player_data[player_name] = []
            player_data[player_name].append(player_name)

        elif i == 2:
            a = str(a)
            data = BeautifulSoup(a, 'html.parser')
            data = data.find('a').text
            player_data[player_name].append(data)

        else:
            if a == '-':
                a = '0'
            player_data[player_name].append(a)

for i, record in enumerate(player_data):
    player_up = {
    'player_name' : player_data[record][0],
    'shirt_num' : player_data[record][1],
    'player_club' : player_data[record][2],
    'games_played' : player_data[record][3],
    'goals_scored' : player_data[record][4],
    'passes_on_goal' : player_data[record][5],
    'gp_points' : player_data[record][6],
    'plus_minus' : player_data[record][7],
    'penaly_time' : player_data[record][8],
    'goals_equal_teams' : player_data[record][9],
    'goals_advantage' : player_data[record][10],
    'goals_disadvantage' : player_data[record][11],
    'goals_overtime' : player_data[record][12],
    'goals_decisive' : player_data[record][13],
    'bullit_decisive' : player_data[record][14],
    'shots_on_goal' : player_data[record][15],
    'percent_of_shots_scored' : player_data[record][16],
    'average_shots' : player_data[record][17],
    'faceoffs_taken' : player_data[record][18],
    'faceoff_won' : player_data[record][19],
    'faceoff_percentage' : player_data[record][20],
    'average_time_on_ice' : player_data[record][21],
    'average_substitutes' : player_data[record][22],
    'opponent_hits' : player_data[record][23],
    'blocked_shots' : player_data[record][24],
    'fouls_accepted' : player_data[record][25],
    'version_datetime' : timestamp,
    'player_position' : 'Нападающий'
    }
    
    player_up = PlayersStats(player_up['player_name'], int(player_up['shirt_num']), player_up['player_club'], int(player_up['games_played']),
        int(player_up['goals_scored']), int(player_up['passes_on_goal']), int(player_up['gp_points']), int(player_up['plus_minus']),
        int(player_up['penaly_time']), int(player_up['goals_equal_teams']), int(player_up['goals_advantage']), int(player_up['goals_disadvantage']),
        int(player_up['goals_overtime']), int(player_up['goals_decisive']), int(player_up['bullit_decisive']), int(player_up['shots_on_goal']),
        float(player_up['percent_of_shots_scored']), float(player_up['average_shots']), int(player_up['faceoffs_taken']), int(player_up['faceoff_won']),
        float(player_up['faceoff_percentage']), player_up['average_time_on_ice'], float(player_up['average_substitutes']), int(player_up['opponent_hits']),
        int(player_up['blocked_shots']), int(player_up['fouls_accepted']), player_up['version_datetime'], player_up['player_position']) 
    
    db_session.add(player_up)

# db commit
db_session.commit()


# goalkeeper = 17
# forwards = 18