import json
    
VALID_KEYS = [
    "id_registro",
    "ano_filmagem",
    "ano_cerimonia",
    "cerimonia",
    "categoria",
    "nome_do_indicado",
    "nome_do_filme",
    "vencedor",
    "diretor"
]

EXTENSIBLE_NUMBERS = {
    "um": 1, "dois": 2, "três": 3,
    "quatro": 4, "cinco": 5, "seis": 6,
    "sete": 7, "oito": 8, "nove": 9, "dez": 10
}

def remove_invalid_keys(doc):
    return {k: v for k, v in doc.items() if k in VALID_KEYS}

def fix_id_registro(doc):
    val = doc.get("id_registro")
    if isinstance(val, str):
        lower = val.lower().strip()
        if lower in EXTENSIBLE_NUMBERS:
            doc["id_registro"] = EXTENSIBLE_NUMBERS[lower]
        elif lower.isdigit():
            doc["id_registro"] = int(lower)
    return doc

def fix_ano_cerimonia(doc):
    val = doc.get("ano_cerimonia")
    if isinstance(val, str):
        digits = ''.join(filter(str.isdigit, val))
        if len(digits) == 4:
            doc["ano_cerimonia"] = int(digits)
        else:
            doc["ano_cerimonia"] = None
    return doc

def fix_nome_do_filme(doc):
    val = doc.get("nome_do_filme")
    if isinstance(val, str):
        val = val.strip().rstrip(";").strip()
        if val.upper() == "NULL" or val == "":
            doc["nome_do_filme"] = None
        else:
            doc["nome_do_filme"] = val
    return doc

def fix_vencedor(doc):
    val = doc.get("ven cedor") or doc.get("vencedor")
    if isinstance(val, str):
        doc["vencedor"] = val.lower().strip() == "true"
    else:
        doc["vencedor"] = bool(val) if val is not None else False
    doc.pop("ven cedor", None)
    return doc

def ensure_defaults(doc):
    if "diretor" not in doc:
        doc["diretor"] = None
    return doc

def remove_mongo_id(doc):
    doc.pop("_id", None)
    return doc

def clean_doc(doc):
    doc = remove_mongo_id(doc)
    doc = fix_id_registro(doc)
    doc = fix_ano_cerimonia(doc)
    doc = fix_nome_do_filme(doc)
    doc = fix_vencedor(doc)
    doc = ensure_defaults(doc)
    doc = remove_invalid_keys(doc)
    return doc

def clean_data():
    with open("data/oscar.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cleaned = [clean_doc(doc) for doc in data]
    
    with open("data/oscar_clean.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)
        
    print(f"{len(cleaned)} documentos limpos e salvos em data/oscar_clea.json")
    

clean_data()