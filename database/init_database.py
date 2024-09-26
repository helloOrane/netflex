import pandas as pd
import os
from random import randrange, choice
import uuid
from sqlalchemy import create_engine

engine = create_engine('sqlite:///netflex.db', echo=False)

users_file = os.path.join('database', 'netflix_userbase.csv')
titles_file = os.path.join('database', 'netflix_titles.csv')

users_file_data = pd.read_csv(users_file)
titles_file_data = pd.read_csv(titles_file)
tmdb_movie_file = pd.read_csv('database/TMDB_movie.csv')
tmdb_tv_file = pd.read_csv('database/TMDB_tv.csv')

user_id_list = users_file_data['User_id']
tv_show_id_list = tmdb_tv_file['id'].head(2000)
movie_id_list = tmdb_movie_file['id'].head(2000)


user_tv_show_random_data=[]
user_movie_random_data=[]
# Génération de données pour la table User_title
for user_id in user_id_list:
    random_iterations = randrange(10, 30)
    #generate random data for tv show watched by user
    for i in range(random_iterations):
        random_tv_show_id = tv_show_id_list[randrange(0, len(tv_show_id_list))]

        random_date = pd.to_datetime(randrange(1577836800, 1612051200), unit='s')
        random_date = random_date.strftime('%Y-%m-%d')

        random_boolean_is_liked = randrange(0, 2)
        random_boolean_is_on_my_list = randrange(0, 2)
        id = str(uuid.uuid4())
        new_row = [id, user_id, random_tv_show_id, random_date, random_boolean_is_liked, random_boolean_is_on_my_list]
        user_tv_show_random_data.append(new_row)
    #generate random data for movie watched by user
    random_iterations = randrange(10, 30)
    for i in range(random_iterations):
        random_movie_id = movie_id_list[randrange(0, len(movie_id_list))]

        random_date = pd.to_datetime(randrange(1577836800, 1612051200), unit='s')
        random_date = random_date.strftime('%Y-%m-%d')

        random_boolean_is_liked = randrange(0, 2)
        random_boolean_is_on_my_list = randrange(0, 2)
        id = str(uuid.uuid4())
        new_row = [id, user_id, random_movie_id, random_date, random_boolean_is_liked, random_boolean_is_on_my_list]
        user_movie_random_data.append(new_row)


user_tv_show_dataframe = pd.DataFrame(user_tv_show_random_data, columns=['Id','User_id', 'Tv_show_id', 'Date', 'Is_liked', 'Is_on_my_list'])
user_movie_dataframe = pd.DataFrame(user_movie_random_data, columns=['Id','User_id', 'Movie_id', 'Date', 'Is_liked', 'Is_on_my_list'])

# GENERATION DU FICHIER CSV
user_tv_show_dataframe.to_csv('database/user_movie.csv', index=False)
user_movie_dataframe.to_csv('database/user_tv_show.csv', index=False)
tmdb_movie_file.head(2000).to_csv('database/TMDB_movie.csv', index=False)
tmdb_tv_file.head(2000).to_csv('database/TMDB_tv.csv', index=False)


# GENERATION DES TABLES SQL
user_tv_show_dataframe.to_sql('User_tv_show', con=engine, if_exists='replace', index=False)
user_movie_dataframe.to_sql('User_movie', con=engine, if_exists='append', index=False)
users_file_data.to_sql('User', con=engine, if_exists='replace', index=True, index_label='Id')
tmdb_tv_file.head(2000).to_sql('Tv_show', con=engine, if_exists='replace', index=False)
tmdb_movie_file.head(2000).to_sql('Movie', con=engine, if_exists='replace', index=False)


# CREATION DE LA TABLE User_account AVEC DES DONNEES TEST
user_account_test = [['01', 'John Doe', 'jdoe@gmail.com','password', 'United States', 'M', 28], ['02', 'Jane Doe', 'jadoe@gmail.com', 'password', 'Canada', 'F', 35]]
pd.DataFrame(columns=['User_id', 'Name', 'Email', 'Password', 'Country','Gender', 'Age'], data=user_account_test).to_sql('User_account', con=engine, if_exists='replace', index=True, index_label='Id')


# # RECUPERATION DES NOMS ET DES PATHS DES IMAGES
# name_img_movie_path = tmdb_movie_file[['Title', 'Backdrop_path']]
# # Remove duplicates in the 'Title' column of name_img_movie_path
# name_imgpath_unique = name_img_movie_path.drop_duplicates(subset=['Title'])

# #CREATION D UN DATAFRAME OU JE MERGE TITLE ET name_img_movie_path
# title_df = titles_file_data.merge(name_imgpath_unique, on='Title', how='left')

# #CREATION DE LA TABLE TITLE
# title_df.to_sql('Title', con=engine, if_exists='replace', index=True, index_label='Id')

# 






