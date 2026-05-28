import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_4_1():
    resultado = collection.find_one(
        {"categoria": "ACTRESS", "vencedor": True},
        sort=[("ano_cerimonia", 1)]
    )
    return {
        "pergunta": "Quem ganhou o primeiro Oscar para Melhor Atriz (ACTRESS)? Em que ano e por qual filme?",
        "comando_mongo": 'db.indicados.find({categoria: "ACTRESS", vencedor: true}).sort({ano_cerimonia: 1}).limit(1)',
        "resultado": {
            "nome": resultado["nome_do_indicado"],
            "ano": resultado["ano_cerimonia"],
            "filme": resultado["nome_do_filme"]
        }
    }

def questao_4_2():
    resultado = collection.find_one(
        {"categoria": "ACTOR", "vencedor": True},
        sort=[("ano_cerimonia", 1)]
    )
    return {
        "pergunta": "Quem ganhou o primeiro Oscar para Melhor Ator (ACTOR)? Em que ano e por qual filme?",
        "comando_mongo": 'db.indicados.find({categoria: "ACTOR", vencedor: true}).sort({ano_cerimonia: 1}).limit(1)',
        "resultado": {
            "nome": resultado["nome_do_indicado"],
            "ano": resultado["ano_cerimonia"],
            "filme": resultado["nome_do_filme"]
        }
    }

def questao_4_3():
    resultado = collection.count_documents({"vencedor": True})
    return {
        "pergunta": "Quantos vencedores existem ao todo na base de dados?",
        "comando_mongo": "db.indicados.countDocuments({vencedor: true})",
        "resultado": resultado
    }

def questao_4_4():
    resultado = collection.distinct(
        "nome_do_filme",
        {"categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]}, "vencedor": True}
    )
    return {
        "pergunta": 'Liste todos os filmes que ganharam o Oscar de Melhor Filme.',
        "comando_mongo": 'db.indicados.distinct("nome_do_filme", {categoria: {$in: ["OUTSTANDING PICTURE", "BEST PICTURE"]}, vencedor: true})',
        "resultado": resultado
    }

def questao_4_5():
    resultado = len(collection.distinct("nome_do_filme", {"vencedor": True}))
    return {
        "pergunta": "Quantos filmes diferentes já ganharam o Oscar?",
        "comando_mongo": 'db.indicados.distinct("nome_do_filme", {vencedor: true}).length',
        "resultado": resultado
    }