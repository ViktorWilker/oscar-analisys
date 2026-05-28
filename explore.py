import json
from collections import defaultdict

with open("data/oscar.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
campos = defaultdict(set) #tipos encontrados
ausentes = defaultdict(int) #quantos docs n tem esse campo
valores_unicos = defaultdict(set) 
todos_campos = set()

for doc in data:
    todos_campos.update(doc.keys())
    for campo, valor in doc.items():
        campos[campo].add(type(valor).__name__)
        if len(valores_unicos[campo]) < 20:
            valores_unicos[campo].add(valor)


for doc in data:
    for campo in todos_campos:
        if campo not in doc:
            ausentes[campo] += 1
            

print(f"Total de documentos: {len(data)}")
print(f"\nCampos encontrados: {todos_campos}")
print("\n--- Tipos por campo ---")
for campo, tipos in campos.items():
    print(f"{campo}: {tipos}")
print("\n--- Ausências por campo ---")
for campo, qtd in ausentes.items():
    print(f"{campo}: {qtd} docs sem esse campo")
print("\n--- Valores únicos (campos pequenos) ---")
for campo, valores in valores_unicos.items():
    if len(valores) <= 20:
        print(f"{campo}: {valores}")
