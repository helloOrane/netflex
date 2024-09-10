import pandas as pd
import os
from random import randrange
import uuid
from sqlalchemy import create_engine

engine = create_engine('sqlite:///netflex.db', echo=False)

users_file = os.path.join('database', 'netflix_userbase.csv')
titles_file = os.path.join('database', 'netflix_titles.csv')

users_file_data = pd.read_csv(users_file)
titles_file_data = pd.read_csv(titles_file)

user_id_list = users_file_data['User_id']
show_id_list = titles_file_data['Show_id']


datas=[]
for user_id in user_id_list:
    random_iterations = randrange(1, 10)
    for i in range(random_iterations):
        random_show_id = show_id_list[randrange(0, len(show_id_list))]

        random_date = pd.to_datetime(randrange(1577836800, 1612051200), unit='s')
        random_date = random_date.strftime('%Y-%m-%d')

        random_boolean_is_liked = randrange(0, 2)
        random_boolean_is_on_my_list = randrange(0, 2)
        id = str(uuid.uuid4())
        new_row = [id, user_id, random_show_id, random_date, random_boolean_is_liked, random_boolean_is_on_my_list]
        datas.append(new_row)

user_title_dataframe = pd.DataFrame(datas, columns=['Id','User_id', 'Show_id', 'Date', 'Is_liked', 'Is_on_my_list'])

# GENERATION DU FICHIER CSV
# user_title_dataframe.to_csv('database/user_movie.csv', index=False)

# GENERATION DE LA TABLE SQL
user_title_dataframe.to_sql('User_title', con=engine, if_exists='replace', index=True)
users_file_data.to_sql('User', con=engine, if_exists='replace', index=True)
titles_file_data.to_sql('Title', con=engine, if_exists='replace', index=True)



