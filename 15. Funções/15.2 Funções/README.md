# 🐍 Funções (Python) - Parte 2

---

## 📌 1. Interactive Help

O Python possui um sistema de ajuda interativa.

### 🔧 help()

Mostra informações sobre funções e comandos.

```python
help()
```

### 📌 Exemplo

```python
help(print)
```

⚠️ Em alguns ambientes como VS Code pode não funcionar corretamente.

---

### 🔧 **doc**

Outra forma de ver informações internas:

```python
print(input.__doc__)
```

---

## 📌 2. Docstrings

Docstrings são strings de documentação dentro de funções.

São usadas para explicar o funcionamento do código.

### 🔧 Exemplo

```python
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(2, 10, 2)
```

📌 Diferente de comentários (`#`), docstrings usam aspas triplas:

```python
def exemplo():
    """Essa função faz algo específico"""
```

---

## 📌 3. Parâmetros opcionais (valores padrão)

Permitem evitar erros quando nem todos os argumentos são passados.

### 🔧 Exemplo

```python
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
```

### 📌 Uso

```python
somar(3, 2, 5)
somar(8, 4)
```

### 🧠 Versão mais segura

```python
def somar(a=0, b=0, c=0):
```

---

## 📌 4. Escopo de variáveis

Escopo define onde uma variável existe.

### 🌍 Escopo global

* Existe em todo o código

### 📍 Escopo local

* Existe apenas dentro da função

### ⚠️ Exemplo

```python
def funcao():
    x = 10  # variável local

print(x)  # erro
```

---

## 📌 5. Retornando valores

Funções podem retornar valores com `return`.

### 🔧 Exemplo

```python
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
```

---

## 🚀 Resumo

* `help()` → ajuda interativa
* `__doc__` → documentação interna
* docstring → documentação dentro da função
* parâmetros padrão → evitam erros
* escopo → define onde variáveis existem
* `return` → devolve valores da função
