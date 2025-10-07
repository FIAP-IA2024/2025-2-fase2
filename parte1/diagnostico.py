#!/usr/bin/env python3
# diagnostico.py - Sistema de Diagnostico Cardíaco por Sintomas
import csv
import re
from pathlib import Path
from collections import Counter

def normalize(text):
    text = text.lower()
    trans = str.maketrans("áàãâäéèêëíìîïóòõôöúùûüç", "aaaaaeeeeiiiiooooouuuuc")
    text = text.translate(trans)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def carregar_mapa(mapa_path):
    mapa = []
    with open(mapa_path, encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(',')
            if len(partes) >= 3:
                s1 = [normalize(t.strip()) for t in partes[0].split('|') if t.strip()]
                s2 = [normalize(t.strip()) for t in partes[1].split('|') if t.strip()]
                doenca = ','.join(partes[2:]).strip()
                mapa.append({'Sintoma_1': s1, 'Sintoma_2': s2, 'Doenca': doenca})
    return mapa

def match_score(frase_norm, sintomas):
    score = 0
    matched = []
    for sintoma in sintomas:
        if sintoma and sintoma in frase_norm:
            score += 1
            matched.append(sintoma)
    return score, matched

def diagnosticar(frase, mapa):
    frase_norm = normalize(frase)
    scores = {}
    matched_details = {}
    
    for linha in mapa:
        diag = linha['Doenca']
        sc1, m1 = match_score(frase_norm, linha['Sintoma_1'])
        sc2, m2 = match_score(frase_norm, linha['Sintoma_2'])
        total = sc1 + sc2
        
        if total > 0:
            scores[diag] = scores.get(diag, 0) + total
            if diag not in matched_details:
                matched_details[diag] = []
            matched_details[diag].extend(m1 + m2)
    
    if not scores:
        mais_comum = Counter([l['Doenca'] for l in mapa]).most_common(1)[0][0]
        return {'Frase': frase, 'Sintomas_Encontrados': '', 'Diagnóstico_Sugerido': mais_comum, 'Pontuação': 0.0}
    
    melhor = max(scores.keys(), key=lambda k: scores[k])
    sintomas_unicos = sorted(set(matched_details[melhor]))
    sintomas = ';'.join(sintomas_unicos)
    
    # Pontuação melhorada: baseada em sintomas únicos encontrados
    # 1 sintoma = 3.5, 2 sintomas = 6.0, 3 sintomas = 8.0, 4+ sintomas = 10.0
    num_sintomas_unicos = len(sintomas_unicos)
    if num_sintomas_unicos == 1:
        pontuacao_normalizada = 3.5
    elif num_sintomas_unicos == 2:
        pontuacao_normalizada = 6.0
    elif num_sintomas_unicos == 3:
        pontuacao_normalizada = 8.0
    else:
        pontuacao_normalizada = 10.0
    
    return {
        'Frase': frase, 
        'Sintomas_Encontrados': sintomas,
        'Diagnóstico_Sugerido': melhor, 
        'Pontuação': pontuacao_normalizada
    }

def processar(txt_path, mapa_path, out_path):
    mapa = carregar_mapa(mapa_path)
    resultados = []
    with open(txt_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                resultados.append(diagnosticar(line, mapa))
    
    # Ordem das colunas: Frase, Sintomas_Encontrados, Diagnóstico_Sugerido, Pontuação
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Frase', 'Sintomas_Encontrados', 'Diagnóstico_Sugerido', 'Pontuação']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resultados)
    
    print(f"Arquivo gerado: {out_path}")
    print(f"Total de frases: {len(resultados)}")
    print(f"Pontuação média: {sum(r['Pontuação'] for r in resultados) / len(resultados):.1f}/10")

if __name__ == "__main__":
    base = Path(__file__).parent
    processar(base / "phrases_10.txt", base / "mapa_sintomas.csv", base / "resultados_sugestao.csv")
