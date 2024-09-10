from sqlalchemy import select, text
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.init_database import engine


# Définir les paramètres de pagination
page = 1  # Numéro de la page
page_size = 10  # Nombre de résultats par page

# Calculer l'offset
offset = (page - 1) * page_size

# Sélectionner toutes les lignes
with engine.connect() as connection:
    query = text("SELECT * FROM Title LIMIT :limit OFFSET :offset")
    result = connection.execute(query, {"limit": page_size, "offset": offset})
    
    for row in result:
        print(row)

        
