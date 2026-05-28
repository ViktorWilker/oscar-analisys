import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_8_1():
    pipeline = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {
            "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
            "total": {"$sum": 1}
        }},
        {"$sort": {"_id": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Quantas indicações aconteceram por década?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: {$multiply: [{$floor: {$divide: ["$ano_cerimonia", 10]}}, 10]}, total: {$sum: 1}}}, {$sort: {_id: 1}}])',
        "resultado": resultado
    }

def questao_8_2():
    pipeline = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {
            "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
            "total": {"$sum": 1}
        }},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Em qual década houve o maior número de indicações?",
        "comando_mongo": 'db.indicados.aggregate([..., {$sort: {total: -1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_8_3():
    pipeline = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {
            "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
            "categorias": {"$addToSet": "$categoria"}
        }},
        {"$project": {
            "decada": "$_id",
            "total_categorias": {"$size": "$categorias"}
        }},
        {"$sort": {"decada": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Como o número de categorias evoluiu ao longo dos anos?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: decada, categorias: {$addToSet: "$categoria"}}}, {$project: {total_categorias: {$size: "$categorias"}}}])',
        "resultado": resultado
    }

def questao_8_4():
    pipeline = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {"_id": "$ano_cerimonia", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual foi o ano com o maior número de indicações registradas?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$ano_cerimonia", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_8_5():
    pipeline_primeira = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {
            "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
            "total": {"$sum": 1}
        }},
        {"$sort": {"_id": 1}},
        {"$limit": 1}
    ]
    pipeline_ultima = [
        {"$match": {"ano_cerimonia": {"$ne": None}}},
        {"$group": {
            "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
            "total": {"$sum": 1}
        }},
        {"$sort": {"_id": -1}},
        {"$limit": 1}
    ]
    primeira = list(collection.aggregate(pipeline_primeira))[0]
    ultima = list(collection.aggregate(pipeline_ultima))[0]
    crescimento = round(((ultima["total"] - primeira["total"]) / primeira["total"]) * 100, 2)
    return {
        "pergunta": "Calcule a taxa de crescimento de indicações comparando a primeira década com a última.",
        "comando_mongo": "duas aggregations separadas para primeira e última década",
        "resultado": {
            "primeira_decada": primeira,
            "ultima_decada": ultima,
            "crescimento_percentual": f"{crescimento}%"
        }
    }