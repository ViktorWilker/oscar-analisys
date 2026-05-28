
import sys
import os
import re
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def _safe_import(module_name: str):
    try:
        import importlib
        return importlib.import_module(module_name)
    except Exception as e:
        print(f"[WARN] Could not import {module_name}: {e}")
        return None

n1  = _safe_import("queries.nivel_1")
n2  = _safe_import("queries.nivel_2")
n3  = _safe_import("queries.nivel_3")
n4  = _safe_import("queries.nivel_4")
n5  = _safe_import("queries.nivel_5")
n6  = _safe_import("queries.nivel_6")
n7  = _safe_import("queries.nivel_7")
n8  = _safe_import("queries.nivel_8")
n9  = _safe_import("queries.nivel_9")
n10 = _safe_import("queries.nivel_10")
n11 = _safe_import("queries.nivel_11")
n12 = _safe_import("queries.nivel_12")
n13 = _safe_import("queries.nivel_13")
n14 = _safe_import("queries.nivel_14")

def _q(module, fn_name: str):
    """Returns the function object, or None if module/function is missing."""
    if module is None:
        return None
    return getattr(module, fn_name, None)


QUESTIONS = [
    ("1.1", _q(n1, "questao_1_1")),
    ("1.2", _q(n1, "questao_1_2")),
    ("1.3", _q(n1, "questao_1_3")),
    ("1.4", _q(n1, "questao_1_4")),
    ("1.5", _q(n1, "questao_1_5")),

    ("2.1", _q(n2, "questao_2_1")),
    ("2.2", _q(n2, "questao_2_2")),
    ("2.3", _q(n2, "questao_2_3")),
    ("2.4", _q(n2, "questao_2_4")),
    ("2.5", _q(n2, "questao_2_5")),
    ("2.6", _q(n2, "questao_2_6")),

    ("3.1",  _q(n3, "questao_3_1")),
    ("3.2",  _q(n3, "questao_3_2")),
    ("3.3",  _q(n3, "questao_3_3")),
    ("3.4",  _q(n3, "questao_3_4")),
    ("3.5",  _q(n3, "questao_3_5")),
    ("3.6",  _q(n3, "questao_3_6")),
    ("3.7",  _q(n3, "questao_3_7")),
    ("3.8",  _q(n3, "questao_3_8")),
    ("3.9",  _q(n3, "questao_3_9")),
    ("3.10", _q(n3, "questao_3_10")),
    ("3.11", _q(n3, "questao_3_11")),
    ("3.12", _q(n3, "questao_3_12")),

    ("4.1", _q(n4, "questao_4_1")),
    ("4.2", _q(n4, "questao_4_2")),
    ("4.3", _q(n4, "questao_4_3")),
    ("4.4", _q(n4, "questao_4_4")),
    ("4.5", _q(n4, "questao_4_5")),

    ("5.1", _q(n5, "questao_5_1")),
    ("5.2", _q(n5, "questao_5_2")),
    ("5.3", _q(n5, "questao_5_3")),
    ("5.4", _q(n5, "questao_5_4")),
    ("5.5", _q(n5, "questao_5_5")),
    ("5.6", _q(n5, "questao_5_6")),

    ("6.1", _q(n6, "questao_6_1")),
    ("6.2", _q(n6, "questao_6_2")),
    ("6.3", _q(n6, "questao_6_3")),
    ("6.4", _q(n6, "questao_6_4")),
    ("6.5", _q(n6, "questao_6_5")),
    ("6.6", _q(n6, "questao_6_6")),
    ("6.7", _q(n6, "questao_6_7")),
    ("6.8", _q(n6, "questao_6_8")),

    ("7.1", _q(n7, "question_7_1")),
    ("7.2", _q(n7, "question_7_2")),
    ("7.3", _q(n7, "question_7_3")),
    ("7.4", _q(n7, "question_7_4")),
    ("7.5", _q(n7, "question_7_5")),

    ("8.1", _q(n8, "questao_8_1")),
    ("8.2", _q(n8, "questao_8_2")),
    ("8.3", _q(n8, "questao_8_3")),
    ("8.4", _q(n8, "questao_8_4")),
    ("8.5", _q(n8, "questao_8_5")),

    ("9.1", _q(n9, "questao_9_1")),
    ("9.2", _q(n9, "questao_9_2")),
    ("9.3", _q(n9, "questao_9_3")),
    ("9.4", _q(n9, "questao_9_4")),
    ("9.5", _q(n9, "questao_9_5")),
    ("9.6", _q(n9, "questao_9_6")),
    ("9.7", _q(n9, "questao_9_7")),

    ("10.1", _q(n10, "questao_10_1")),
    ("10.2", _q(n10, "questao_10_2")),
    ("10.3", _q(n10, "questao_10_3")),
    ("10.4", _q(n10, "questao_10_4")),
    ("10.5", _q(n10, "questao_10_5")),
    ("10.6", _q(n10, "questao_10_6")),

    ("11.1", _q(n11, "questao_11_1")),
    ("11.2", _q(n11, "questao_11_2")),
    ("11.3", _q(n11, "questao_11_3")),
    ("11.4", _q(n11, "questao_11_4")),
    ("11.5", _q(n11, "questao_11_5")),
    ("11.6", _q(n11, "questao_11_6")),

    ("12.1", _q(n12, "questao_12_1")),
    ("12.2", _q(n12, "questao_12_2")),
    ("12.3", _q(n12, "questao_12_3")),
    ("12.4", _q(n12, "questao_12_4")),
    ("12.5", _q(n12, "questao_12_5")),
    ("12.6", _q(n12, "questao_12_6")),
    ("12.7", _q(n12, "questao_12_7")),
    ("12.8", _q(n12, "questao_12_8")),
    ("12.9", _q(n12, "questao_12_9")),

    ("13.1", _q(n13, "questao_13_1")),
    ("13.2", _q(n13, "questao_13_2")),
    ("13.3", _q(n13, "questao_13_3")),
    ("13.4", _q(n13, "questao_13_4")),
    ("13.5", _q(n13, "questao_13_5")),

    ("14.1", _q(n14, "questao_14_1")),
]

def run_all() -> list[dict]:
    results = []
    total = len(QUESTIONS)

    for i, (label, fn) in enumerate(QUESTIONS, start=1):
        print(f"  [{i:>2}/{total}] questao {label} ... ", end="", flush=True)

        if fn is None:
            print("SKIP (function not found)")
            results.append({
                "label": label,
                "pergunta": f"Questão {label}",
                "comando_mongo": "",
                "resultado": "",
                "error": "function not found"
            })
            continue

        try:
            data = fn()
            print("OK")
            results.append({
                "label": label,
                "pergunta": data.get("pergunta", ""),
                "comando_mongo": data.get("comando_mongo", ""),
                "resultado": data.get("resultado", ""),
                "error": None
            })
        except Exception as e:
            print(f"ERROR — {e}")
            results.append({
                "label": label,
                "pergunta": f"Questão {label}",
                "comando_mongo": "",
                "resultado": "",
                "error": str(e)
            })

    return results


LEVEL_HEADINGS = {
    "1":  "Nível 1 — Primeiros Passos",
    "2":  "Nível 2 — Explorando Categorias",
    "3":  "Nível 3 — Atores e Atrizes Famosos",
    "4":  "Nível 4 — Vencedores Históricos",
    "5":  "Nível 5 — Análise de Indicações",
    "6":  "Nível 6 — Análise de Filmes",
    "7":  "Nível 7 — Operações de Atualização",
    "8":  "Nível 8 — Análise Temporal",
    "9":  "Nível 9 — Questões Históricas e Sociais",
    "10": "Nível 10 — Análise Avançada",
    "11": "Nível 11 — Desafios Complexos",
    "12": "Nível 12 — Casos Práticos",
    "13": "Nível 13 — Queries Criativas",
    "14": "Nível 14 — Dashboard Completo",
}


def _level_key(label: str) -> str:
    """'10.3' → '10',  '3.1' → '3'"""
    return label.split(".")[0]


def _format_result(value) -> str:
    if value is None or value == "" or value == []:
        return "_—_"

    if isinstance(value, (int, float, bool, str)):
        return f"`{value}`"

    if isinstance(value, dict):
        rows = "\n".join(f"| `{k}` | {_format_result(v)} |" for k, v in value.items())
        return f"| Campo | Valor |\n|---|---|\n{rows}"

    if isinstance(value, list):
        if not value:
            return "_—_"

        truncated = len(value) > 20
        display = value[:20]

        if isinstance(display[0], dict):
            all_keys: list[str] = []
            for row in display:
                for k in row.keys():
                    if k not in all_keys:
                        all_keys.append(k)

            header = "| " + " | ".join(all_keys) + " |"
            separator = "|" + "|".join(["---"] * len(all_keys)) + "|"
            body_rows = []
            for row in display:
                cells = " | ".join(str(row.get(k, "")) for k in all_keys)
                body_rows.append(f"| {cells} |")

            table = "\n".join([header, separator] + body_rows)
            if truncated:
                table += f"\n\n_... e mais {len(value) - 20} registros_"
            return table

        bullets = "\n".join(f"- `{item}`" for item in display)
        if truncated:
            bullets += f"\n- _... e mais {len(value) - 20} itens_"
        return bullets

    return f"```\n{value}\n```"


def build_markdown(results: list[dict]) -> str:
    lines: list[str] = []

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines += [
        "# 🏆 Oscar — Exercícios MongoDB",
        "",
        f"> Gerado automaticamente em {now}",
        "",
        "---",
        "",
    ]

    current_level = None

    for entry in results:
        label = entry["label"]
        level = _level_key(label)

        if level != current_level:
            current_level = level
            heading = LEVEL_HEADINGS.get(level, f"Nível {level}")
            lines += ["", f"## {heading}", ""]

        lines += [f"### {label} — {entry['pergunta']}", ""]

        if entry["error"]:
            lines += [
                f"> ⚠️ **Erro ao executar:** `{entry['error']}`",
                "",
            ]
            continue

        if entry["comando_mongo"]:
            lines += [
                "**Comando MongoDB**",
                "",
                "```js",
                entry["comando_mongo"],
                "```",
                "",
            ]

        lines += [
            "**Resultado**",
            "",
            _format_result(entry["resultado"]),
            "",
            "---",
            "",
        ]

    return "\n".join(lines)

def main():
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")

    print("\n🎬 Oscar MongoDB — README Generator")
    print("=" * 40)
    print("Running all questions...\n")

    results = run_all()

    ok    = sum(1 for r in results if r["error"] is None)
    error = sum(1 for r in results if r["error"] is not None)
    print(f"\n✅ {ok} OK   ❌ {error} errors")

    print("\nBuilding markdown...")
    markdown = build_markdown(results)

    print(f"Writing {output_path} ...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"\n✅ README.md written ({len(markdown):,} characters).")
    if error:
        print(f"⚠️  {error} question(s) failed — check the callouts in the README.")


if __name__ == "__main__":
    main()