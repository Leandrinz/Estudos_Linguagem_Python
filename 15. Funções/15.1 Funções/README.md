# 🐍 Funções (Python) - Parte 1

---

## 📌 1. O que são funções

Funções são como **rotinas** dentro do código.

Elas representam ações que podem ser executadas várias vezes.

Exemplos de funções já prontas:

* `print()`
* `float()`

---

## 📌 2. Criando funções

Podemos criar nossas próprias funções usando `def`.

### 🔧 Exemplo

```python
def mostraLinha():
    print('----------------------')
```

---

## 📌 3. Chamando funções

Depois de criar, basta chamar pelo nome:

```python
mostraLinha()
print('SISTEMAS DE ALUNOS')
mostraLinha()
```

---

## ⚠️ 4. Organização do código

As funções devem ser declaradas no início do código, separadas por duas linhas do restante do programa.

---

## 📌 5. Parâmetros

Funções podem receber valores para personalização.

### 🔧 Exemplo

```python
def mensagem(msg):
    print('--------------')
    print(msg)
    print('--------------')
```

### 📌 Uso

```python
mensagem('SISTEMA DE ALUNOS')
mensagem('VASCO')
```

### 🧠 Resultado

```
--------------
VASCO
--------------
```

---

## 📌 6. Empacotamento de parâmetros

Permite receber vários valores em uma única função.

### 🔧 Exemplo

```python
def contador(*num):
    print(num)
```

### 📌 Uso

```python
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
```

🧠 O `*num` significa que os valores são empacotados em uma tupla.

---

## 📌 7. Trabalhando com listas

```python
valores = [7, 2, 5, 0, 4]
```

Podemos manipular os valores dentro da lista diretamente ou através de funções.

📌 Exemplo de ideia:

* dobrar valores
* modificar elementos sem desempacotar

(implementação detalhada pode ser feita em outro arquivo como `teste3.py`)

---

## 🚀 Resumo

* Funções = rotinas reutilizáveis
* `def` → cria função
* parâmetros → personalizam funções
* `*args` → empacota múltiplos valores
* listas podem ser manipuladas dentro de funções
