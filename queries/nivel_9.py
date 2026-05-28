import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_9_1():
    resultado = collection.find_one(
        {"nome_do_indicado": "Sidney Poitier"},
        sort=[("ano_cerimonia", 1)]
    )
    return {
        "pergunta": "Sidney Poitier foi o primeiro ator negro a ser indicado ao Oscar. Em que ano ele foi indicado? Por qual filme?",
        "comando_mongo": 'db.indicados.find({nome_do_indicado: "Sidney Poitier"}).sort({ano_cerimonia: 1}).limit(1)',
        "resultado": {
            "ano": resultado["ano_cerimonia"],
            "filme": resultado["nome_do_filme"]
        } if resultado else "Não encontrado"
    }

def questao_9_2():
    primeira = collection.find_one(
        {"nome_do_indicado": "Sidney Poitier"},
        sort=[("ano_cerimonia", 1)]
    )
    return {
        "pergunta": "Sidney Poitier ganhou o Oscar nessa indicação?",
        "comando_mongo": 'db.indicados.find({nome_do_indicado: "Sidney Poitier"}).sort({ano_cerimonia: 1}).limit(1)',
        "resultado": "Sim" if primeira and primeira["vencedor"] else "Não"
    }

def questao_9_3():
    resultado = collection.count_documents({
        "categoria": {"$in": ["ACTOR", "ACTRESS"]},
        "ano_cerimonia": {"$lt": 1970}
    })
    return {
        "pergunta": "Quantos atores/atrizes negros foram indicados na categoria ACTOR ou ACTRESS antes de 1970?",
        "comando_mongo": 'db.indicados.countDocuments({categoria: {$in: ["ACTOR", "ACTRESS"]}, ano_cerimonia: {$lt: 1970}})',
        "resultado": resultado
    }

def questao_9_4():
    resultado = collection.distinct(
        "nome_do_filme",
        {"categoria": {"$regex": "DIRECTING", "$options": "i"}, "vencedor": True}
    )
    return {
        "pergunta": "Liste todos os filmes dirigidos por mulheres que ganharam algum Oscar.",
        "comando_mongo": 'db.indicados.distinct("nome_do_filme", {categoria: {$regex: "DIRECTING"}, vencedor: true})',
        "resultado": resultado
    }

def questao_9_5():
    anos_denzel = set(collection.distinct("ano_cerimonia", {"nome_do_indicado": "Denzel Washington"}))
    anos_foxx = set(collection.distinct("ano_cerimonia", {"nome_do_indicado": "Jamie Foxx"}))
    anos_comuns = anos_denzel & anos_foxx
    return {
        "pergunta": "Denzel Washington e Jamie Foxx já concorreram ao Oscar no mesmo ano?",
        "comando_mongo": 'db.indicados.distinct("ano_cerimonia", {nome_do_indicado: "Denzel Washington"})',
        "resultado": "Sim" if anos_comuns else "Não"
    }

def questao_9_6():
    anos_denzel = set(collection.distinct("ano_cerimonia", {"nome_do_indicado": "Denzel Washington"}))
    anos_foxx = set(collection.distinct("ano_cerimonia", {"nome_do_indicado": "Jamie Foxx"}))
    anos_comuns = anos_denzel & anos_foxx

    if not anos_comuns:
        return {
            "pergunta": "Se sim, em qual ano e quem ganhou?",
            "comando_mongo": "",
            "resultado": "Eles não concorreram no mesmo ano"
        }

    ano = list(anos_comuns)[0]
    vencedor_denzel = collection.find_one({"nome_do_indicado": "Denzel Washington", "ano_cerimonia": ano, "vencedor": True})
    vencedor_foxx = collection.find_one({"nome_do_indicado": "Jamie Foxx", "ano_cerimonia": ano, "vencedor": True})
    vencedor = "Denzel Washington" if vencedor_denzel else "Jamie Foxx" if vencedor_foxx else "Nenhum dos dois"
    return {
        "pergunta": "Se sim, em qual ano e quem ganhou?",
        "comando_mongo": 'db.indicados.findOne({nome_do_indicado: "Denzel Washington", ano_cerimonia: ANO, vencedor: true})',
        "resultado": {"ano": ano, "vencedor": vencedor}
    }

def questao_9_7():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {
            "_id": {"filme": "$nome_do_filme", "ano": "$ano_cerimonia"},
            "categorias_vencidas": {"$sum": 1}
        }},
        {"$match": {"categorias_vencidas": {"$gt": 1}}},
        {"$sort": {"categorias_vencidas": -1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Encontre casos onde o mesmo filme ganhou Oscar em múltiplas categorias na mesma cerimônia.",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: {filme: "$nome_do_filme", ano: "$ano_cerimonia"}, categorias_vencidas: {$sum: 1}}}, {$match: {categorias_vencidas: {$gt: 1}}}])',
        "resultado": resultado
    }