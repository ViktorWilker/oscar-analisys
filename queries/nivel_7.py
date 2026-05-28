import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import get_collection
from pymongo import MongoClient
from datetime import datetime

collection = get_collection()

client = MongoClient("mongodb://localhost:27017")
migrations = client["oscar"]["_migrations"]


def already_ran(question_id: str):
    return migrations.find_one({"question": question_id})


def register_execution(question_id: str, result: dict):
    migrations.insert_one({
        "question": question_id,
        "executed_at": datetime.now(),
        "saved_result": result
    })


def run_once(question_id: str, fn):
    record = already_ran(question_id)
    if record:
        print(f"[SKIP] {question_id} already executed. Using saved result.")
        return record["saved_result"]

    result = fn()
    register_execution(question_id, result)
    print(f"[OK]   {question_id} executed and registered.")
    return result


def _run_7_1():
    result_true = collection.update_many(
        {"vencedor": "true"},
        {"$set": {"vencedor": True}}
    )
    result_false = collection.update_many(
        {"vencedor": "false"},
        {"$set": {"vencedor": False}}
    )
    total = result_true.modified_count + result_false.modified_count
    return {
        "pergunta": 'No campo "vencedor", altere todos os valores "true" (string) para true (booleano) e "false" (string) para false (booleano).',
        "comando_mongo": (
            'db.indicados.updateMany({vencedor: "true"}, {$set: {vencedor: true}})\n'
            'db.indicados.updateMany({vencedor: "false"}, {$set: {vencedor: false}})'
        ),
        "resultado": f"{total} documentos atualizados"
    }


def _run_7_2():
    films = [
        {
            "id_registro": 99001,
            "ano_filmagem": 1994,
            "ano_cerimonia": 1995,
            "cerimonia": 67,
            "categoria": "BEST PICTURE",
            "nome_do_indicado": "The Shawshank Redemption",
            "nome_do_filme": "The Shawshank Redemption",
            "vencedor": False,
            "diretor": None
        },
        {
            "id_registro": 99002,
            "ano_filmagem": 2001,
            "ano_cerimonia": 2002,
            "cerimonia": 74,
            "categoria": "BEST PICTURE",
            "nome_do_indicado": "Mulholland Drive",
            "nome_do_filme": "Mulholland Drive",
            "vencedor": False,
            "diretor": None
        },
        {
            "id_registro": 99003,
            "ano_filmagem": 2003,
            "ano_cerimonia": 2004,
            "cerimonia": 76,
            "categoria": "BEST PICTURE",
            "nome_do_indicado": "Eternal Sunshine of the Spotless Mind",
            "nome_do_filme": "Eternal Sunshine of the Spotless Mind",
            "vencedor": False,
            "diretor": None
        }
    ]
    collection.insert_many(films)
    return {
        "pergunta": "Inclua no banco 3 filmes que nunca foram nomeados ao Oscar, mas que você acha que merecem.",
        "comando_mongo": "db.indicados.insertMany([...])",
        "resultado": "3 filmes inseridos: The Shawshank Redemption, Mulholland Drive, Eternal Sunshine of the Spotless Mind"
    }


def _run_7_3():
    winners = [
        {"id_registro": 99010, "ano_filmagem": 2019, "ano_cerimonia": 2020, "cerimonia": 92,
         "categoria": "BEST INTERNATIONAL FEATURE FILM", "nome_do_indicado": "Parasite",
         "nome_do_filme": "Parasite", "vencedor": True, "diretor": None},
        {"id_registro": 99011, "ano_filmagem": 2020, "ano_cerimonia": 2021, "cerimonia": 93,
         "categoria": "BEST INTERNATIONAL FEATURE FILM", "nome_do_indicado": "Another Round",
         "nome_do_filme": "Another Round", "vencedor": True, "diretor": None},
        {"id_registro": 99012, "ano_filmagem": 2021, "ano_cerimonia": 2022, "cerimonia": 94,
         "categoria": "BEST INTERNATIONAL FEATURE FILM", "nome_do_indicado": "Drive My Car",
         "nome_do_filme": "Drive My Car", "vencedor": True, "diretor": None},
        {"id_registro": 99013, "ano_filmagem": 2022, "ano_cerimonia": 2023, "cerimonia": 95,
         "categoria": "BEST INTERNATIONAL FEATURE FILM", "nome_do_indicado": "All Quiet on the Western Front",
         "nome_do_filme": "All Quiet on the Western Front", "vencedor": True, "diretor": None},
        {"id_registro": 99014, "ano_filmagem": 2023, "ano_cerimonia": 2024, "cerimonia": 96,
         "categoria": "BEST INTERNATIONAL FEATURE FILM", "nome_do_indicado": "The Zone of Interest",
         "nome_do_filme": "The Zone of Interest", "vencedor": True, "diretor": None},
    ]
    collection.insert_many(winners)
    return {
        "pergunta": 'Adicione uma nova categoria chamada "BEST INTERNATIONAL FEATURE FILM" com alguns vencedores recentes (2020-2024).',
        "comando_mongo": "db.indicados.insertMany([...])",
        "resultado": "5 vencedores inseridos na categoria BEST INTERNATIONAL FEATURE FILM (2020-2024)"
    }


def _run_7_4():
    result = collection.update_many(
        {"nome_do_filme": {"$regex": ";$"}},
        [{"$set": {"nome_do_filme": {"$rtrim": {"input": "$nome_do_filme", "chars": ";"}}}}]
    )
    return {
        "pergunta": "Corrija possíveis erros de digitação nos nomes dos filmes (espaços extras, caracteres especiais).",
        "comando_mongo": (
            'db.indicados.updateMany(\n'
            '  {nome_do_filme: {$regex: ";$"}},\n'
            '  [{$set: {nome_do_filme: {$rtrim: {input: "$nome_do_filme", chars: ";"}}}}]\n'
            ')'
        ),
        "resultado": f"{result.modified_count} documentos corrigidos"
    }


def _run_7_5():
    result = collection.delete_many({"nome_do_filme": None})
    return {
        "pergunta": "Remova todos os registros com valor NULL no campo nome_do_filme.",
        "comando_mongo": "db.indicados.deleteMany({nome_do_filme: null})",
        "resultado": f"{result.deleted_count} documentos removidos"
    }


def question_7_1():
    return run_once("7_1", _run_7_1)

def question_7_2():
    return run_once("7_2", _run_7_2)

def question_7_3():
    return run_once("7_3", _run_7_3)

def question_7_4():
    return run_once("7_4", _run_7_4)

def question_7_5():
    return run_once("7_5", _run_7_5)


def reset_migrations_level_7():
    result = migrations.delete_many({"question": {"$regex": "^7_"}})
    print(f"[RESET] {result.deleted_count} migration records removed.")
    print("You can now re-run level 7 questions.")


if __name__ == "__main__":
    for fn in [question_7_1, question_7_2, question_7_3, question_7_4, question_7_5]:
        r = fn()
        print(f"  Result: {r['resultado']}\n")