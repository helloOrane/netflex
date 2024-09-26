from sqlalchemy import select, text
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.init_database import engine

def get_all_tv_show():
    with engine.connect() as connection:
        query = text("SELECT * FROM Tv_show")
        result = connection.execute(query)
        return result.fetchall()

def get_all_tv_show_paginated(queries=None, page=1, page_size=10):
    # Calculer l'offset
    offset = (page - 1) * page_size

    # Sélectionner toutes les lignes
    with engine.connect() as connection:
        if queries is None or len(queries) == 0:
            request = text("SELECT * FROM Tv_show   LIMIT :limit OFFSET :offset")
            result = connection.execute(request, {"limit": page_size, "offset": offset})
            result_list = [row._mapping for row in result]
            return result_list
        else:
            conditions = []
            params = {"limit": page_size, "offset": offset}
            for i, query in enumerate(queries):
                param_name = f"query{i}"
                params[param_name] = f"%{query}%"
                conditions.append(f"""(name LIKE :{param_name} 
                    OR tagline LIKE :{param_name}
                    OR genres LIKE :{param_name}
                    OR created_by LIKE :{param_name}
                    OR origin_country LIKE :{param_name}
                    OR production_companies LIKE :{param_name}
                    OR production_countries LIKE :{param_name}               
                    OR overview LIKE :{param_name})""")
            where_clause = " AND ".join(conditions)
            sql_query = f"""
                SELECT * FROM Tv_show 
                WHERE ({where_clause})  
                LIMIT :limit OFFSET :offset
            """
            request = text(sql_query)
            result = connection.execute(request, params)
            result_list = [row._mapping for row in result]
            return result_list

def get_tv_show_by_id(title_id):
    with engine.connect() as connection:
        query = text("SELECT * FROM Tv_show WHERE id = :id")
        result = connection.execute(query, {"id": title_id})
        return result.fetchone()

def get_categories_tv_show():
     with engine.connect() as connection:
        query = text("SELECT genres FROM Tv_show")
        connection.execute(query)
        result = connection.execute(query)
        genres = [row._mapping for row in result]
        # print('result', result)

        #result is a list of tuples of string
        category_list = []
        # print('genres', genres)
        for item in genres:
            # print('item !', item['genres'])
            genre_list = item['genres']
            if genre_list is not None:
                categories = genre_list.split(',')
            for category in categories:
                category_list.append(category.strip())# strip: Remove spaces at the beginning and at the end of the string
        category_list_set = set(category_list)# set: remove duplicates because a set does not allow duplicates
        return list(category_list_set)
     
# test = get_all_tv_show_paginated('Sci-Fi & Fantasy')
# print(test)