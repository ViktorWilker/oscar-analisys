import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection

collection = get_collection()

def questao_14_1():
    pipeline = [
        {"$facet": {
            "total_indicacoes": [
                {"$count": "total"}
            ],
            "total_cerimonias": [
                {"$group": {"_id": "$ano_cerimonia"}},
                {"$count": "total"}
            ],
            "total_vencedores": [
                {"$match": {"vencedor": True}},
                {"$count": "total"}
            ],
            "categoria_mais_indicada": [
                {"$group": {"_id": "$categoria", "total": {"$sum": 1}}},
                {"$sort": {"total": -1}},
                {"$limit": 1}
            ],
            "filme_mais_premiado": [
                {"$match": {"vencedor": True}},
                {"$group": {"_id": "$nome_do_filme", "oscars": {"$sum": 1}}},
                {"$sort": {"oscars": -1}},
                {"$limit": 1}
            ],
            "artista_mais_indicado": [
                {"$group": {"_id": "$nome_do_indicado", "indicacoes": {"$sum": 1}}},
                {"$sort": {"indicacoes": -1}},
                {"$limit": 1}
            ],
            "decada_mais_premiacoes": [
                {"$match": {"vencedor": True, "ano_cerimonia": {"$ne": None}}},
                {"$group": {
                    "_id": {"$multiply": [{"$floor": {"$divide": ["$ano_cerimonia", 10]}}, 10]},
                    "total": {"$sum": 1}
                }},
                {"$sort": {"total": -1}},
                {"$limit": 1}
            ],
            "total_categorias_unicas": [
                {"$group": {"_id": "$categoria"}},
                {"$count": "total"}
            ]
        }}
    ]

    raw = list(collection.aggregate(pipeline))[0]

    resultado = {
        "total_indicacoes": raw["total_indicacoes"][0]["total"],
        "total_cerimonias": raw["total_cerimonias"][0]["total"],
        "total_vencedores": raw["total_vencedores"][0]["total"],
        "categoria_mais_indicada": raw["categoria_mais_indicada"][0],
        "filme_mais_premiado": raw["filme_mais_premiado"][0],
        "artista_mais_indicado": raw["artista_mais_indicado"][0],
        "decada_mais_premiacoes": raw["decada_mais_premiacoes"][0],
        "total_categorias_unicas": raw["total_categorias_unicas"][0]["total"]
    }

    return {
        "pergunta": "Dashboard executivo completo em uma única query.",
        "comando_mongo": "db.indicados.aggregate([{$facet: { total_indicacoes: [{$count: 'total'}], total_cerimonias: [...], ... }}])",
        "resultado": resultado
    }
