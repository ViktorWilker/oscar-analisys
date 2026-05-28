import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_5_1():
    pipeline = [
        {"$group": {"_id": "$nome_do_indicado", "indicacoes": {"$sum": 1}}},
        {"$match": {"indicacoes": {"$gt": 1}}},
        {"$sort": {"indicacoes": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Quais atores/atrizes foram indicados mais de uma vez?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$match: {indicacoes: {$gt: 1}}}, {$sort: {indicacoes: -1}}])',
        "resultado": resultado
    }

def questao_5_2():
    pipeline = [
        {"$group": {"_id": "$nome_do_indicado", "indicacoes": {"$sum": 1}}},
        {"$sort": {"indicacoes": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual ator ou atriz tem o maior número de indicações na história do Oscar?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$sort: {indicacoes: -1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_5_3():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_indicado",
            "indicacoes": {"$sum": 1},
            "vitorias": {"$sum": {"$cond": ["$vencedor", 1, 0]}}
        }},
        {"$match": {"indicacoes": {"$gt": 3}, "vitorias": 0}},
        {"$sort": {"indicacoes": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Quais atores foram indicados mais de 3 vezes, mas nunca ganharam?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gt: 3}, vitorias: 0}}])',
        "resultado": resultado
    }

def questao_5_4():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_indicado",
            "categorias": {"$addToSet": "$categoria"}
        }},
        {"$match": {"$expr": {"$gt": [{"$size": "$categorias"}, 1]}}},
        {"$sort": {"_id": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Encontre todos os artistas que foram indicados em categorias diferentes.",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", categorias: {$addToSet: "$categoria"}}}, {$match: {$expr: {$gt: [{$size: "$categorias"}, 1]}}}])',
        "resultado": resultado
    }

def questao_5_5():
    pipeline = [
        {"$group": {"_id": "$nome_do_indicado", "indicacoes": {"$sum": 1}}},
        {"$match": {"indicacoes": 1}},
        {"$count": "total"}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Quantos indicados têm exatamente 1 indicação na história?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$match: {indicacoes: 1}}, {$count: "total"}])',
        "resultado": resultado[0]["total"] if resultado else 0
    }

def questao_5_6():
    pipeline = [
        {"$group": {"_id": "$ano_cerimonia", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual o maior número de indicados em um único ano?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$ano_cerimonia", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])',
        "resultado": resultado
    }