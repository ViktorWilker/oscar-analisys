import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_3_1():
    resultado = collection.count_documents({"nome_do_indicado": "Natalie Portman"})
    return {
        "pergunta": "Quantas vezes Natalie Portman foi indicada ao Oscar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Natalie Portman"})',
        "resultado": resultado
    }

def questao_3_2():
    resultado = collection.count_documents({"nome_do_indicado": "Natalie Portman", "vencedor": True})
    return {
        "pergunta": "Quantos Oscars Natalie Portman ganhou?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Natalie Portman", vencedor: true})',
        "resultado": resultado
    }

def questao_3_3():
    cursor = collection.find(
        {"nome_do_indicado": "Natalie Portman"},
        {"ano_cerimonia": 1, "nome_do_filme": 1, "_id": 0}
    )
    resultado = list(cursor)
    return {
        "pergunta": "Em quais anos e por quais filmes Natalie Portman foi indicada?",
        "comando_mongo": 'db.indicados.find({nome_do_indicado: "Natalie Portman"}, {ano_cerimonia: 1, nome_do_filme: 1})',
        "resultado": resultado
    }

def questao_3_4():
    cursor = collection.find(
        {"nome_do_indicado": "Natalie Portman"},
        {"ano_cerimonia": 1, "categoria": 1, "nome_do_filme": 1, "vencedor": 1, "_id": 0}
    )
    resultado = list(cursor)
    return {
        "pergunta": "Liste todas as indicações de Natalie Portman mostrando: ano, categoria, filme e se venceu.",
        "comando_mongo": 'db.indicados.find({nome_do_indicado: "Natalie Portman"}, {ano_cerimonia: 1, categoria: 1, nome_do_filme: 1, vencedor: 1})',
        "resultado": resultado
    }

def questao_3_5():
    resultado = collection.count_documents({"nome_do_indicado": "Viola Davis"})
    return {
        "pergunta": "Quantas vezes Viola Davis foi indicada ao Oscar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Viola Davis"})',
        "resultado": resultado
    }

def questao_3_6():
    resultado = collection.count_documents({"nome_do_indicado": "Viola Davis", "vencedor": True})
    return {
        "pergunta": "Quantos Oscars Viola Davis ganhou?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Viola Davis", vencedor: true})',
        "resultado": resultado
    }

def questao_3_7():
    resultado = collection.distinct("nome_do_filme", {"nome_do_indicado": "Viola Davis"})
    return {
        "pergunta": "Por quais filmes Viola Davis foi indicada?",
        "comando_mongo": 'db.indicados.distinct("nome_do_filme", {nome_do_indicado: "Viola Davis"})',
        "resultado": resultado
    }

def questao_3_8():
    resultado = collection.count_documents({"nome_do_indicado": "Amy Adams", "vencedor": True})
    return {
        "pergunta": "Amy Adams já ganhou algum Oscar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Amy Adams", vencedor: true})',
        "resultado": "Sim" if resultado > 0 else "Não"
    }

def questao_3_9():
    resultado = collection.count_documents({"nome_do_indicado": "Amy Adams", "vencedor": False})
    return {
        "pergunta": "Quantas vezes Amy Adams foi indicada sem ganhar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Amy Adams", vencedor: false})',
        "resultado": resultado
    }

def questao_3_10():
    resultado = collection.count_documents({"nome_do_indicado": "Denzel Washington", "vencedor": True})
    return {
        "pergunta": "Denzel Washington já ganhou algum Oscar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Denzel Washington", vencedor: true})',
        "resultado": "Sim" if resultado > 0 else "Não"
    }

def questao_3_11():
    resultado = collection.count_documents({"nome_do_indicado": "Denzel Washington"})
    return {
        "pergunta": "Quantas vezes Denzel Washington foi indicado ao Oscar?",
        "comando_mongo": 'db.indicados.countDocuments({nome_do_indicado: "Denzel Washington"})',
        "resultado": resultado
    }

def questao_3_12():
    cursor = collection.find(
        {"nome_do_indicado": "Denzel Washington", "vencedor": True},
        {"ano_cerimonia": 1, "categoria": 1, "nome_do_filme": 1, "_id": 0}
    )
    resultado = list(cursor)
    return {
        "pergunta": "Liste todos os Oscars que Denzel Washington ganhou (ano, categoria, filme).",
        "comando_mongo": 'db.indicados.find({nome_do_indicado: "Denzel Washington", vencedor: true}, {ano_cerimonia: 1, categoria: 1, nome_do_filme: 1})',
        "resultado": resultado
    }