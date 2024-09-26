from sqlalchemy import select, text
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.init_database import engine

def get_all_movies():
    with engine.connect() as connection:
        query = text("SELECT * FROM Movie")
        result = connection.execute(query)
        return result.fetchall()

def get_all_movies_paginated(queries=None, page=1, page_size=10):
    # Calculer l'offset
    offset = (page - 1) * page_size

    # Sélectionner toutes les lignes
    with engine.connect() as connection:
        if queries is None or len(queries) == 0:
            request = text("SELECT * FROM Movie  LIMIT :limit OFFSET :offset")
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
                    OR release_date LIKE :{param_name}
                    OR tagline LIKE :{param_name}
                    OR genres LIKE :{param_name}
                    OR production_companies LIKE :{param_name}
                    OR production_countries LIKE :{param_name}
                    OR keywords LIKE :{param_name}
                    OR overview LIKE :{param_name})""")
            where_clause = " AND ".join(conditions)
            sql_query = f"""
                SELECT * FROM Movie 
                WHERE ({where_clause})  
                LIMIT :limit OFFSET :offset
            """
            request = text(sql_query)
            result = connection.execute(request, params)
            result_list = [row._mapping for row in result]
            return result_list

def get_movie_by_id(title_id):
    with engine.connect() as connection:
        query = text("SELECT * FROM Movie WHERE id = :id")
        result = connection.execute(query, {"id": title_id})
        return result.fetchone()

def get_categories_movies():
     with engine.connect() as connection:
        query = text("SELECT genres FROM Movie")
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

