import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_1_1():
    resultado = collection.count_documents({})
    return {
        "pergunta": "Quantos registros existem na coleção de indicados ao Oscar?",
        "comando_mongo": "db.indicados.countDocuments({})",
        "resultado": resultado
    }

def questao_1_2():
    resultado = collection.distinct("categoria")
    return {
        "pergunta": "Quais são as diferentes categorias de premiação que existem no banco de dados?",
        "comando_mongo": 'db.indicados.distinct("categoria")',
        "resultado": resultado
    }

def questao_1_3():
    resultado = collection.find_one(
        {"ano_cerimonia": {"$ne": None}},
        sort=[("ano_cerimonia", 1)]
    )
    return {
        "pergunta": "Qual foi o primeiro ano de cerimônia do Oscar registrado na base?",
        "comando_mongo": 'db.indicados.find({ano_cerimonia: {$ne: null}}).sort({ano_cerimonia: 1}).limit(1)',
        "resultado": resultado["ano_cerimonia"]
    }

def questao_1_4():
    resultado = collection.find_one(
        {"ano_cerimonia": {"$ne": None}},
        sort=[("ano_cerimonia", -1)]
    )
    return {
        "pergunta": "Qual foi o último ano de cerimônia registrado na base?",
        "comando_mongo": 'db.indicados.find({ano_cerimonia: {$ne: null}}).sort({ano_cerimonia: -1}).limit(1)',
        "resultado": resultado["ano_cerimonia"]
    }

def questao_1_5():
    resultado = len(collection.distinct("ano_cerimonia"))
    return {
        "pergunta": "Quantas cerimônias do Oscar estão registradas no total?",
        "comando_mongo": 'db.indicados.distinct("ano_cerimonia").length',
        "resultado": resultado
    }
    
    