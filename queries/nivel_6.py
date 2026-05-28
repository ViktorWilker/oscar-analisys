import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_6_1():
    resultado = collection.distinct(
        "ano_cerimonia",
        {"nome_do_filme": {"$regex": "Toy Story", "$options": "i"}, "vencedor": True}
    )
    return {
        "pergunta": "A série de filmes Toy Story ganhou Oscars em quais anos?",
        "comando_mongo": 'db.indicados.distinct("ano_cerimonia", {nome_do_filme: {$regex: "Toy Story", $options: "i"}, vencedor: true})',
        "resultado": sorted(resultado)
    }

def questao_6_2():
    resultado = collection.count_documents({"nome_do_filme": {"$regex": "Toy Story", "$options": "i"}})
    return {
        "pergunta": "Quantas indicações a franquia Toy Story recebeu no total?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_filme: {$regex: "Toy Story", $options: "i"}})',
        "resultado": resultado
    }

def questao_6_3():
    resultado = collection.distinct(
        "categoria",
        {"nome_do_filme": {"$regex": "Toy Story", "$options": "i"}}
    )
    return {
        "pergunta": "Em quais categorias os filmes Toy Story foram indicados?",
        "comando_mongo": 'db.indicados.distinct("categoria", {nome_do_filme: {$regex: "Toy Story", $options: "i"}})',
        "resultado": resultado
    }

def questao_6_4():
    resultado = collection.distinct("ano_cerimonia", {"nome_do_filme": "Crash"})
    return {
        "pergunta": 'Em qual edição do Oscar o filme "Crash" concorreu?',
        "comando_mongo": 'db.indicados.distinct("ano_cerimonia", {nome_do_filme: "Crash"})',
        "resultado": resultado
    }

def questao_6_5():
    resultado = collection.count_documents({"nome_do_filme": "Crash"})
    return {
        "pergunta": 'Quantas indicações o filme "Crash" recebeu?',
        "comando_mongo": 'db.indicados.countDocuments({nome_do_filme: "Crash"})',
        "resultado": resultado
    }

def questao_6_6():
    resultado = collection.count_documents({
        "nome_do_filme": "Crash",
        "categoria": {"$in": ["OUTSTANDING PICTURE", "BEST PICTURE"]},
        "vencedor": True
    })
    return {
        "pergunta": '"Crash" ganhou o Oscar de Melhor Filme?',
        "comando_mongo": 'db.indicados.countDocuments({nome_do_filme: "Crash", categoria: {$in: ["OUTSTANDING PICTURE", "BEST PICTURE"]}, vencedor: true})',
        "resultado": "Sim" if resultado > 0 else "Não"
    }

def questao_6_7():
    resultado = collection.find_one({"nome_do_filme": {"$regex": "Central do Brasil", "$options": "i"}})
    return {
        "pergunta": 'O filme "Central do Brasil" aparece no banco de dados?',
        "comando_mongo": 'db.indicados.findOne({nome_do_filme: {$regex: "Central do Brasil", $options: "i"}})',
        "resultado": "Sim" if resultado else "Não"
    }

def questao_6_8():
    resultado = collection.count_documents({"nome_do_filme": {"$regex": "Central do Brasil", "$options": "i"}})
    return {
        "pergunta": 'Quantas indicações "Central do Brasil" recebeu?',
        "comando_mongo": 'db.indicados.countDocuments({nome_do_filme: {$regex: "Central do Brasil", $options: "i"}})',
        "resultado": resultado
    }