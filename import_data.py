import json
from db.connection import get_collection

def import_data():
    collection = get_collection()
    
    with open("data/oscar_clean.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    collection.drop()
    collection.insert_many(data)
    print(f"{len(data)} documentos importados!")
    

import_data()