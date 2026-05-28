import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_13_1():
    resultado = collection.distinct(
        "nome_do_filme",
        {"nome_do_filme": {"$regex": "^The ", "$options": "i"}, "vencedor": True}
    )
    return {
        "pergunta": 'Encontre todos os filmes cujo nome começa com "The" e ganharam pelo menos um Oscar.',
        "comando_mongo": 'db.indicados.distinct("nome_do_filme", {nome_do_filme: {$regex: "^The "}, vencedor: true})',
        "resultado": sorted(resultado)
    }

def questao_13_2():
    resultado = collection.distinct(
        "nome_do_indicado",
        {"nome_do_indicado": {"$regex": "-"}}
    )
    return {
        "pergunta": 'Liste todos os indicados cujo nome contém um sobrenome composto (ex: "Mary-Louise Parker").',
        "comando_mongo": 'db.indicados.distinct("nome_do_indicado", {nome_do_indicado: {$regex: "-"}})',
        "resultado": sorted(resultado)
    }

def questao_13_3():
    pipeline = [
        {"$match": {"vencedor": True}},
        {"$group": {
            "_id": {"categoria": "$categoria", "ano": "$ano_cerimonia"},
            "vencedores": {"$push": "$nome_do_indicado"},
            "total": {"$sum": 1}
        }},
        {"$match": {"total": {"$gt": 1}}},
        {"$sort": {"_id.ano": 1}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": "Encontre todas as cerimônias onde houve empate (múltiplos vencedores na mesma categoria no mesmo ano).",
        "comando_mongo": 'db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: {categoria, ano}, total: {$sum: 1}}}, {$match: {total: {$gt: 1}}}])',
        "resultado": resultado
    }

def questao_13_4():
    pipeline = [
        {"$match": {
            "categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]},
            "vencedor": True
        }},
        {"$sample": {"size": 5}},
        {"$project": {"nome_do_filme": 1, "ano_cerimonia": 1, "_id": 0}}
    ]
    resultado = list(collection.aggregate(pipeline))
    return {
        "pergunta": 'Crie uma query que simule uma "loteria" - selecione 5 filmes aleatórios que ganharam Melhor Filme.',
        "comando_mongo": 'db.indicados.aggregate([{$match: {categoria: {$in: [...]}, vencedor: true}}, {$sample: {size: 5}}])',
        "resultado": resultado
    }

def questao_13_5():
    vencedores = collection.distinct(
        "nome_do_filme",
        {"categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]}, "vencedor": True}
    )
    contagem = {}
    for filme in vencedores:
        if filme:
            palavras = len(filme.split())
            contagem[palavras] = contagem.get(palavras, 0) + 1
    resultado = sorted(contagem.items())
    return {
        "pergunta": "Encontre padrões nos nomes dos filmes vencedores (quantos têm uma palavra, duas palavras, etc.).",
        "comando_mongo": "db.indicados.distinct('nome_do_filme', {categoria: {$in: [...]}, vencedor: true}) + análise em Python",
        "resultado": {f"{k} palavra(s)": v for k, v in resultado}
    }