# 🐍 Manipulação de Strings (Python)

---

## 📌 1. Atribuição

Uma string é armazenada em uma variável e ocupa posições na memória, começando do índice 0.

⚠️ Espaços também contam como caracteres.

```python
frase = 'Curso em Vídeo Python'
```

---

## ✂️ 2. Fatiamento (Slicing)

Permite acessar partes da string:

```python
frase[9]        # caractere na posição 9
frase[9:13]     # do índice 9 até 12
frase[9:13:2]   # do 9 ao 12 pulando de 2 em 2
frase[:5]       # do início até 4
frase[15:]      # do 15 até o final
frase[9::3]     # do 9 até o final pulando de 3 em 3
```

---

## 🔎 3. Análise de strings

```python
len(frase)                 # tamanho da string
frase.count('o')          # conta ocorrências de 'o'
frase.count('o', 0, 13)   # conta no intervalo
frase.find('deo')         # posição da substring
frase.find('Android')     # retorna -1 se não encontrar
'Curso' in frase          # verifica existência (True/False)
```

---

## 🔄 4. Transformação

```python
frase.replace('Python', 'Android')  # substitui texto
frase.upper()                       # maiúsculas
frase.lower()                       # minúsculas
frase.capitalize()                  # primeira letra maiúscula
frase.title()                       # início de cada palavra maiúsculo
frase.strip()                       # remove espaços das bordas
frase.rstrip()                      # remove espaços à direita
frase.lstrip()                      # remove espaços à esquerda
```

---

## 🧩 5. Divisão (split)

```python
frase.split()        # separa por espaços
frase.split('o')     # separa pelo caractere 'o'
frase.split()[0]     # pega o primeiro elemento
```

---

## 🔗 6. Junção (join)

```python
'-'.join(frase)                     # junta caracteres com '-'
' '.join(frase.split())            # junta palavras com espaço
' '.join(['Curso', 'em', 'Vídeo']) # junta lista de palavras
```

---

## 🚀 Resumo

* Strings começam no índice 0
* Espaços contam como caracteres
* slicing → extrair partes
* análise → medir e buscar
* transformação → alterar texto
* split → dividir
* join → unir
