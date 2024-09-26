from sqlalchemy import select, text
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.init_database import engine

def get_all_titles():
    with engine.connect() as connection:
        query = text("SELECT * FROM Title")
        result = connection.execute(query)
        return result.fetchall()

def get_all_titles_paginated(page=1):
    # Définir les paramètres de pagination
    # page = 1  # Numéro de la page
    page_size = 10  # Nombre de résultats par page

    # Calculer l'offset
    offset = (page - 1) * page_size

    # Sélectionner toutes les lignes
    with engine.connect() as connection:
        query = text("SELECT * FROM Title LIMIT :limit OFFSET :offset")
        result = connection.execute(query, {"limit": page_size, "offset": offset})
        result_list = [row._mapping for row in result]
    return result_list


def get_movie_by_id(title_id):
    with engine.connect() as connection:
        query = text("SELECT * FROM Title WHERE Show_id = :id")
        result = connection.execute(query, {"id": title_id})
        return result.fetchone()
    
def get_movie_video_by_id(title_id):
    with engine.connect() as connection:
        query = text("SELECT Video FROM Title WHERE Show_id = :id")
        result = connection.execute(query, {"id": title_id})
        return result.fetchone()

def update_movie_by_id(title_id, title):
    with engine.connect() as connection:
        query = text("UPDATE Title SET Name = :name WHERE Show_id = :id")
        connection.execute(query, {"name": title, "id": title_id})
        return connection.execute(text("SELECT * FROM Title WHERE Show_id = :id"), {"id": title_id}).fetchone()

def get_categories():
    with engine.connect() as connection:
        query = text("SELECT Listed_in FROM Title")
        connection.execute(query)
        result = connection.execute(query).fetchall()

        #result is a list of tuples of string
        category_list = []
        for item in result:
            categories = item[0].split(',')
            for category in categories:
                category_list.append(category.strip())# strip: Remove spaces at the beginning and at the end of the string
        category_list_set = set(category_list)# set: remove duplicates because a set does not allow duplicates
        return category_list_set
    
def get_categories_movies():
     with engine.connect() as connection:
        query = text("SELECT Listed_in FROM Title WHERE Type='Movie'")
        connection.execute(query)
        result = connection.execute(query).fetchall()

        #result is a list of tuples of string
        category_list = []
        for item in result:
            categories = item[0].split(',')
            for category in categories:
                category_list.append(category.strip())# strip: Remove spaces at the beginning and at the end of the string
        category_list_set = set(category_list)# set: remove duplicates because a set does not allow duplicates
        return list(category_list_set)

def get_categories_tv_shows():
    with engine.connect() as connection:
        query = text("SELECT Listed_in FROM Title WHERE Type='TV Show'")
        connection.execute(query)
        result = connection.execute(query).fetchall()

        #result is a list of tuples of string
        category_list = []
        for item in result:
            categories = item[0].split(',')
            for category in categories:
                category_list.append(category.strip())# strip: Remove spaces at the beginning and at the end of the string
        category_list_set = set(category_list)# set: remove duplicates because a set does not allow duplicates
        return category_list_set

def get_all_tv_shows():
    with engine.connect() as connection:
        query = text("SELECT * from Title WHERE Type='TV Show'")
        result = connection.execute(query)
        result_list = [row._mapping for row in result]
    return result_list

def get_all_tv_shows_paginated(queries=None, page=1, page_size=10, ):
    # Calculer l'offset
    offset = (page - 1) * page_size

    # Sélectionner toutes les lignes
    with engine.connect() as connection:
        if queries is None or len(queries) == 0:
            request = text("SELECT * FROM Title WHERE Type='TV Show' LIMIT :limit OFFSET :offset")
            result = connection.execute(request, {"limit": page_size, "offset": offset})
            result_list = [row._mapping for row in result]
            return result_list
        else:
            conditions = []
            params = {"limit": page_size, "offset": offset}
            for i, query in enumerate(queries):
                param_name = f"query{i}"
                params[param_name] = f"%{query}%"
                conditions.append(f"""(Title LIKE :{param_name} 
                    OR Director LIKE :{param_name}
                    OR Country LIKE :{param_name}
                    OR Date_added LIKE :{param_name} 
                    OR Release_year LIKE :{param_name}
                    OR Rating LIKE :{param_name}
                    OR Listed_in LIKE :{param_name}
                    OR Description LIKE :{param_name})""")
            where_clause = " AND ".join(conditions)
            sql_query = f"""
                SELECT * FROM Title 
                WHERE Type='TV Show' 
                AND ({where_clause})  
                LIMIT :limit OFFSET :offset
            """
            request = text(sql_query)
            result = connection.execute(request, params)
            result_list = [row._mapping for row in result]
            return result_list

  
def get_tv_show_by_category_paginated(category, page=1, page_size=10):
    """
    Retrieve TV shows by category with pagination.

    Args:
        category (str): The category of the TV shows.
        page (int): The page number to retrieve.
        page_size (int): The number of items per page.

    Returns:
        list: A list of dictionaries representing the TV shows.
    """
    offset = (page - 1) * page_size
    query = text("""
        SELECT * FROM Title 
        WHERE Type='TV Show' 
        AND Listed_in LIKE :category 
        LIMIT :limit OFFSET :offset
    """)
    
    try:
        with engine.connect() as connection:
            result = connection.execute(query, {"category": f"%{category}%", "limit": page_size, "offset": offset})
            result_list = [row._mapping for row in result]
        return result_list
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return []
