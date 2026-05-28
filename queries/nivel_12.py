import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_12_1():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {"_id": "$nome_do_filme", "oscars": {"$sum": 1}}},
        {"$sort": {"oscars": -1}},
        {"$limit": 20}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Liste os 20 filmes mais premiados do Oscar para sua mostra.",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$nome_do_filme", oscars: {$sum: 1}}}, {$sort: {oscars: -1}}, {$limit: 20}])',
        "resultado": resultado
    }

def questao_12_2():
    decadas = range(1930, 2030, 10)
    resultado = {}
    for decada in decadas:
        pipeline = [
            {"$match": {
                "vencedor": True,
                "ano_cerimonia": {"$gte": decada, "$lt": decada + 10}
            }},
            {"$group": {"_id": "$nome_do_filme", "oscars": {"$sum": 1}}},
            {"$sort": {"oscars": -1}},
            {"$limit": 5}
        ]
        filmes = list(collection.aggregate(pipeline))
        if filmes:
            resultado[f"{decada}s"] = filmes
    return {
        "pergunta": "Selecione 5 filmes de cada década (1930s até 2020s) que ganharam pelo menos um Oscar.",
        "comando_mongo": "múltiplas queries por década com $match no ano_cerimonia",
        "resultado": resultado
    }

def questao_12_3():
    pipeline = [
        {"$match": {"vencedor": True, "ano_filmagem": {"$lt": 1975}}},
        {"$group": {"_id": "$nome_do_filme", "ano": {"$first": "$ano_filmagem"}, "oscars": {"$sum": 1}}},
        {"$sort": {"ano": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Crie uma lista de "clássicos esquecidos" - filmes que ganharam Oscars, mas são de mais de 50 anos atrás.',
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true, ano_filmagem: {$lt: 1975}}}, {$group: {_id: "$nome_do_filme", ano: {$first: "$ano_filmagem"}}}, {$sort: {ano: 1}}])',
        "resultado": resultado
    }

def questao_12_4():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {"_id": "$ano_cerimonia", "premiações": {"$sum": 1}}},
        {"$sort": {"premiações": -1}},
        {"$limit": 5}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Identifique os 5 momentos mais importantes (cerimônias com mais premiações).",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$ano_cerimonia", premiações: {$sum: 1}}}, {$sort: {premiações: -1}}, {$limit: 5}])',
        "resultado": resultado
    }

def questao_12_5():
    marcos = {}
    primeira_diretora = collection.find_one(
        {"categoria": {"$regex": "DIRECTING"}, "vencedor": True, "nome_do_indicado": {"$regex": " "}},
        sort=[("ano_cerimonia", 1)]
    )
    if primeira_diretora:
        marcos["primeira_vitoria_direcao"] = {
            "nome": primeira_diretora["nome_do_indicado"],
            "ano": primeira_diretora["ano_cerimonia"],
            "filme": primeira_diretora["nome_do_filme"]
        }
    primeiro_ator_negro = collection.find_one(
        {"nome_do_indicado": "Sidney Poitier"},
        sort=[("ano_cerimonia", 1)]
    )
    if primeiro_ator_negro:
        marcos["primeiro_ator_negro_indicado"] = {
            "nome": primeiro_ator_negro["nome_do_indicado"],
            "ano": primeiro_ator_negro["ano_cerimonia"],
            "filme": primeiro_ator_negro["nome_do_filme"]
        }
    return {
        "pergunta": 'Liste todos os "primeiros" históricos.',
        "comando_mongo": "múltiplas queries com sort por ano_cerimonia",
        "resultado": marcos
    }

def questao_12_6():
    pipeline = [
        {"$group": {
            "_id": "$nome_do_indicado",
            "indicacoes": {"$sum": 1},
            "vitorias": {"$sum": {"$cond": ["$vencedor", 1, 0]}}
        }},
        {"$match": {"indicacoes": {"$gte": 4}, "vitorias": 0}},
        {"$sort": {"indicacoes": -1}},
        {"$limit": 20}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Encontre casos de "injustiça" - filmes/atores muito indicados, mas que nunca ganharam.',
        "comando_mongo": 'db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gte: 4}, vitorias: 0}}])',
        "resultado": resultado
    }

def questao_12_7():
    total_com_10 = collection.count_documents({
        "categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]}
    })
    pipeline = [
        {"$group": {
            "_id": "$ano_cerimonia",
            "total_indicacoes": {"$sum": 1}
        }},
        {"$match": {"total_indicacoes": {"$gte": 10}}}
    ]
    anos_com_10 = [doc["_id"] for doc in collection.aggregate(pipeline)]
    venceu = collection.count_documents({
        "ano_cerimonia": {"$in": anos_com_10},
        "categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]},
        "vencedor": True
    })
    probabilidade = round((venceu / len(anos_com_10)) * 100, 2) if anos_com_10 else 0
    return {
        "pergunta": "Qual a probabilidade histórica de um filme indicado em 10 categorias ganhar Melhor Filme?",
        "comando_mongo": "múltiplas aggregations combinadas",
        "resultado": f"{probabilidade}% ({venceu} de {len(anos_com_10)} casos)"
    }

def questao_12_8():
    vencedores = list(collection.find(
        {"categoria": "ACTOR IN A LEADING ROLE", "vencedor": True},
        {"nome_do_indicado": 1, "ano_cerimonia": 1}
    ))
    contagens = []
    for v in vencedores:
        nome = v["nome_do_indicado"]
        ano_vitoria = v["ano_cerimonia"]
        indicacoes_antes = collection.count_documents({
            "nome_do_indicado": nome,
            "ano_cerimonia": {"$lte": ano_vitoria}
        })
        contagens.append(indicacoes_antes)
    media = round(sum(contagens) / len(contagens), 2) if contagens else 0
    return {
        "pergunta": "Atores que ganharam Melhor Ator tendem a ter quantas indicações antes da primeira vitória?",
        "comando_mongo": "query por vencedor + contagem de indicações anteriores por ator",
        "resultado": f"Média de {media} indicações antes da primeira vitória"
    }

def questao_12_9():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {
            "_id": "$categoria",
            "vencedores": {"$push": "$nome_do_indicado"},
            "total_vitorias": {"$sum": 1},
            "vencedores_unicos": {"$addToSet": "$nome_do_indicado"}
        }},
        {"$project": {
            "categoria": "$_id",
            "total_vitorias": 1,
            "total_unicos": {"$size": "$vencedores_unicos"},
            "repeticao": {"$divide": ["$total_vitorias", {"$size": "$vencedores_unicos"}]}
        }},
        {"$sort": {"repeticao": -1}},
        {"$limit": 10}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Qual categoria tem os vencedores mais "previsíveis" (mesmo artista/filme ganha múltiplas vezes)?',
        "comando_mongo": "db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {..., vencedores_unicos: {$addToSet: ...}}}, {$project: {repeticao: {$divide: [total, unicos]}}}])",
        "resultado": resultado
    }