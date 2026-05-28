import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_11_1():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {"_id": "$nome_do_filme", "oscars": {"$sum": 1}}},
        {"$sort": {"oscars": -1}},
        {"$limit": 10}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Crie um ranking dos 10 filmes mais premiados da história.",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$nome_do_filme", oscars: {$sum: 1}}}, {$sort: {oscars: -1}}, {$limit: 10}])',
        "resultado": resultado
    }

def questao_11_2():
    pipeline = [
        {"$group": {"_id": "$nome_do_indicado", "indicacoes": {"$sum": 1}}},
        {"$sort": {"indicacoes": -1}},
        {"$limit": 10}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Crie um ranking dos 10 artistas mais indicados da história, independente da categoria.",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$sort: {indicacoes: -1}}, {$limit: 10}])',
        "resultado": resultado
    }

def questao_11_3():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_indicado",
            "indicacoes": {"$sum": 1},
            "vitorias": {"$sum": {"$cond": ["$vencedor", 1, 0]}}
        }},
        {"$match": {"indicacoes": {"$gt": 5}, "vitorias": 0}},
        {"$sort": {"indicacoes": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Encontre "azarões" - artistas com mais de 5 indicações e 0 vitórias.',
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gt: 5}, vitorias: 0}}])',
        "resultado": resultado
    }

def questao_11_4():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {
            "_id": "$categoria",
            "vencedores_unicos": {"$addToSet": "$nome_do_indicado"}
        }},
        {"$project": {
            "categoria": "$_id",
            "total_vencedores_unicos": {"$size": "$vencedores_unicos"}
        }},
        {"$sort": {"total_vencedores_unicos": 1}},
        {"$limit": 5}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Qual categoria tem a maior concentração de vitórias (menos vencedores diferentes)?",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$categoria", vencedores_unicos: {$addToSet: "$nome_do_indicado"}}}, {$project: {total: {$size: "$vencedores_unicos"}}}, {$sort: {total: 1}}])',
        "resultado": resultado
    }

def questao_11_5():
    pipeline = [
        {"$group": {
            "_id": {"categoria": "$categoria", "ano": "$ano_cerimonia"},
            "indicados": {"$sum": 1}
        }},
        {"$group": {
            "_id": "$_id.categoria",
            "media_indicados": {"$avg": "$indicados"}
        }},
        {"$sort": {"media_indicados": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Calcule a "competitividade" de cada categoria (média de indicados por cerimônia).',
        "comando_mongo": "db.indicados.aggregate([{$group: {_id: {categoria, ano}, indicados: {$sum: 1}}}, {$group: {_id: '$_id.categoria', media: {$avg: '$indicados'}}}])",
        "resultado": resultado
    }

def questao_11_6():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_filme",
            "anos": {"$addToSet": "$ano_cerimonia"},
            "categorias_vencidas": {
                "$push": {
                    "$cond": [
                        {"$eq": ["$vencedor", True]},
                        {"categoria": "$categoria", "ano": "$ano_cerimonia"},
                        None
                    ]
                }
            }
        }},
        {"$match": {"$expr": {"$gt": [{"$size": "$anos"}, 1]}}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Encontre filmes que foram indicados em uma categoria em um ano e ganharam em outra categoria em outro ano.",
        "comando_mongo": "db.indicados.aggregate([{$group: {_id: '$nome_do_filme', anos: {$addToSet: '$ano_cerimonia'}, ...}}])",
        "resultado": resultado[:20]
    }