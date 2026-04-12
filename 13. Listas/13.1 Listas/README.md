# 🐍 Listas (Python) - Parte 1

---

## 📌 1. O que são listas

Diferente das tuplas, as listas são **mutáveis**, ou seja, podem ser alteradas durante a execução do programa.

São definidas usando colchetes:

```python
[]
```

---

## ➕ 2. Adicionando elementos

### 🔧 append()

Adiciona um elemento no final da lista:

```python
lanche.append('cookie')
```

---

### 📍 insert()

Insere um elemento em uma posição específica:

```python
lanche.insert(2, 'cookie')
```

---

## ❌ 3. Removendo elementos

### 🗑️ del

```python
del lanche[3]
```

---

### 🗑️ pop()

Remove pelo índice (ou o último elemento se vazio):

```python
lanche.pop(3)
lanche.pop()
```

---

### 🗑️ remove()

Remove pelo valor:

```python
lanche.remove('cookie')
```

---

### 🔎 Verificação antes de remover

```python
if 'cookie' in lanche:
    lanche.remove('cookie')
```

---

## 📋 4. Formas de declarar listas

```python
valores = list(range(4, 11))
valores = [8, 2, 5, 4, 9, 3, 0]
```

---

## 🔃 5. Ordenação

### Crescente

```python
valores.sort()
```

### Decrescente

```python
valores.sort(reverse=True)
```

---

## 📏 6. Tamanho da lista

```python
len(valores)
```

---

## 🔗 7. Ligação entre listas

Quando uma lista é atribuída a outra, ambas ficam conectadas:

```python
a = [2, 3, 4, 5]
b = a
b[2] = 8
```

✔️ Isso altera as duas listas

---

## 🧪 8. Cópia de lista (sem ligação)

Para criar uma lista independente:

```python
b = a[:]
```

---

## 🚀 Resumo

* Listas são mutáveis
* `append()` → adiciona no final
* `insert()` → adiciona em posição específica
* `del`, `pop`, `remove` → remoção
* `sort()` → ordena
* `len()` → tamanho
* `a = b` → cria ligação
* `a[:]` → cria cópia independente
