import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_10_1():
    pipeline = [
        {"$match": {"vencedor": True, "categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]}}},
        {"$lookup": {
            "from": "indicados",
            "let": {"ano": "$ano_cerimonia", "filme": "$nome_do_filme"},
            "pipeline": [
                {"$match": {"$expr": {
                    "$and": [
                        {"$eq": ["$ano_cerimonia", "$$ano"]},
                        {"$eq": ["$nome_do_filme", "$$filme"]},
                        {"$eq": ["$vencedor", True]},
                        {"$regexMatch": {"input": "$categoria", "regex": "DIRECTING"}}
                    ]
                }}}
            ],
            "as": "melhor_diretor"
        }},
        {"$match": {"melhor_diretor": {"$ne": []}}},
        {"$project": {"nome_do_filme": 1, "ano_cerimonia": 1, "_id": 0}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Quais filmes ganharam o Oscar de Melhor Filme e Melhor Diretor na mesma cerimônia?',
        "comando_mongo": "db.indicados.aggregate([{$match: {vencedor: true, categoria: {$in: [...]}}}, {$lookup: {...}}, ...])",
        "resultado": resultado
    }

def questao_10_2():
    pipeline = [
        {"$group": {
            "_id": {"filme": "$nome_do_filme", "ano": "$ano_cerimonia"},
            "total": {"$sum": 1}
        }},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]
    resultado = list(collection.aggregate(pipeline))[0]
    return {
        "pergunta": "Qual filme recebeu o maior número de indicações em uma única cerimônia?",
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: {filme: "$nome_do_filme", ano: "$ano_cerimonia"}, total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])',
        "resultado": resultado
    }

def questao_10_3():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_filme",
            "indicacoes": {"$sum": 1},
            "vitorias": {"$sum": {"$cond": ["$vencedor", 1, 0]}}
        }},
        {"$match": {"indicacoes": {"$gt": 0}}},
        {"$project": {
            "filme": "$_id",
            "indicacoes": 1,
            "vitorias": 1,
            "taxa": {"$multiply": [{"$divide": ["$vitorias", "$indicacoes"]}, 100]}
        }},
        {"$match": {"vitorias": {"$gt": 0}}},
        {"$sort": {"taxa": -1}},
        {"$limit": 10}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Qual filme teve a maior taxa de conversão (% de indicações que viraram vitórias)?",
        "comando_mongo": "db.indicados.aggregate([{$group: {...}}, {$project: {taxa: {$multiply: [{$divide: ['$vitorias', '$indicacoes']}, 100]}}}, {$sort: {taxa: -1}}])",
        "resultado": resultado
    }

def questao_10_4():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_indicado",
            "anos": {"$addToSet": "$ano_cerimonia"}
        }},
        {"$match": {"$expr": {"$gt": [{"$size": "$anos"}, 1]}}}
    ]
    todos = list(collection.aggregate(pipeline))
    consecutivos = []
    for item in todos:
        anos = sorted([a for a in item["anos"] if isinstance(a, int)])
        for i in range(len(anos) - 1):
            if anos[i + 1] - anos[i] == 1:
                consecutivos.append({"nome": item["_id"], "anos": anos})
                break
    consecutivos.sort(key=lambda x: x["nome"])
    return {
        "pergunta": "Encontre atores que foram indicados em anos consecutivos.",
        "comando_mongo": "db.indicados.aggregate([{$group: {_id: '$nome_do_indicado', anos: {$addToSet: '$ano_cerimonia'}}}])",
        "resultado": consecutivos
    }

def questao_10_5():
    total_indicacoes = collection.count_documents({})
    total_cerimonias = len(collection.distinct("ano_cerimonia"))
    media = round(total_indicacoes / total_cerimonias, 2)
    return {
        "pergunta": "Qual a média de indicações por cerimônia ao longo da história?",
        "comando_mongo": "db.indicados.countDocuments({}) / db.indicados.distinct('ano_cerimonia').length",
        "resultado": media
    }

def questao_10_6():
    pipeline = [
        {"$match": {"categoria": {"$in": ["ACTOR", "ACTRESS", "BEST PICTURE"]}}},
        {"$group": {
            "_id": "$nome_do_filme",
            "total_indicacoes_filme": {"$sum": 1},
            "indicados": {"$push": {"indicado": "$nome_do_indicado", "categoria": "$categoria"}}
        }},
        {"$match": {"total_indicacoes_filme": 1}},
        {"$sort": {"_id": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Identifique "surpresas" - indicados em categorias principais cujo filme só teve uma indicação.',
        "comando_mongo": "db.indicados.aggregate([{$match: {categoria: {$in: ['ACTOR', 'ACTRESS', 'BEST PICTURE']}}}, {$group: {_id: '$nome_do_filme', total: {$sum: 1}}}, {$match: {total: 1}}])",
        "resultado": resultado
    }