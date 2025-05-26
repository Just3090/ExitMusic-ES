import os
import re
import json

DIRECTORY = "Archivosparatraducir"
MAX_FILES = 10

def analizar_contenido(contenido):
    bloques = re.findall(
        r'translate\s+\w+\s+[\w_]+:\s*((?:\s*#.*\n)*\s*(?:e|narrator|centered|"\w+")\s*"(.*?)"|(?:\s*pass)+)', 
        contenido, re.DOTALL
    )
    total_dialogo = len(bloques)
    traducidos_dialogo = 0
    for bloque in bloques:
        if "pass" in bloque[0]:
            continue
        if re.search(r'\n\s*\w+\s*""', bloque[0]):
            continue
        if re.search(r'\n\s*\w+\s*".+?"', bloque[0]):
            traducidos_dialogo += 1
    old_new = re.findall(r'old\s+"((?:[^"\\]|\\.)*)"\s*\n\s*new\s+"((?:[^"\\]|\\.)*)"', contenido)
    total_strings = len(old_new)
    traducidos_strings = sum(1 for orig, trans in old_new if trans.strip() and trans.strip() != orig.strip())
    traducidas = traducidos_dialogo + traducidos_strings
    total = total_dialogo + total_strings
    return traducidas, total

def main():
    archivos = [f for f in os.listdir(DIRECTORY) if f.endswith(".rpy")][:MAX_FILES]
    total_traducidas = total_lineas = 0
    detalles = []
    for archivo in archivos:
        with open(os.path.join(DIRECTORY, archivo), encoding="utf-8") as f:
            contenido = f.read()
        traducidas, total = analizar_contenido(contenido)
        porcentaje = (traducidas / total * 100) if total else 0
        detalles.append({"archivo": archivo, "traducidas": traducidas, "total": total, "porcentaje": porcentaje})
        total_traducidas += traducidas
        total_lineas += total
    total_porcentaje = (total_traducidas / total_lineas * 100) if total_lineas else 0
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump({
            "total_traducidas": total_traducidas,
            "total_lineas": total_lineas,
            "total_porcentaje": total_porcentaje,
            "detalles": detalles
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()