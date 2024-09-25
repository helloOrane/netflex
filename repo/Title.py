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
        print(result)
        return result.fetchall()

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
