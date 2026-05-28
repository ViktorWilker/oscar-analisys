import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_2_1():
    pipeline = [
        {"$group": {"_id": "$categoria", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Quantas indicações existem para cada categoria? Ordene da mais frequente para a menos frequente.",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: -1}}])',
        "resultado": resultado
    }

def questao_2_2():
    pipeline = [
        {"$group": {"_id": "$categoria", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual categoria teve mais indicações ao longo da história do Oscar?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_2_3():
    pipeline = [
        {"$group": {"_id": "$categoria", "total": {"$sum": 1}}},
        {"$sort": {"total": 1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual categoria teve menos indicações ao longo da história?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: 1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_2_4():
    resultado = collection.find_one(
        {"categoria": "ACTRESS"},
        sort=[("ano_cerimonia", -1)]
    )
    return {
        "pergunta": 'A partir de que ano a categoria "ACTRESS" deixou de existir?',
        "comando_mongo": 'db.indicados.find({categoria: "ACTRESS"}).sort({ano_cerimonia: -1}).limit(1)',
        "resultado": resultado["ano_cerimonia"]
    }

def questao_2_5():
    categorias_1928 = set(collection.distinct("categoria", {"ano_cerimonia": 1928}))
    ultimo_ano = collection.find_one(
        {"ano_cerimonia": {"$ne": None}},
        sort=[("ano_cerimonia", -1)]
    )["ano_cerimonia"]
    categorias_atuais = set(collection.distinct("categoria", {"ano_cerimonia": ultimo_ano}))
    resultado = list(categorias_1928 - categorias_atuais)
    return {
        "pergunta": "Quais categorias existiam na primeira cerimônia (1928) e não existem mais hoje?",
        "comando_mongo": 'db.indicados.distinct("categoria", {ano_cerimonia: 1928})',
        "resultado": resultado
    }

def questao_2_6():
    resultado = collection.distinct("categoria", {"categoria": {"$regex": "DIRECTING"}})
    return {
        "pergunta": 'Liste todas as categorias que contêm a palavra "DIRECTING" no nome.',
        "comando_mongo": 'db.indicados.distinct("categoria", {categoria: {$regex: "DIRECTING"}})',
        "resultado": resultado
    }
    