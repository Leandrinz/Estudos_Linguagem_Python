# 🐍 Dicionários (Python)

---

## 📌 1. O que são dicionários

O problema das listas é que acessamos os valores apenas por índices numéricos (0, 1, 2...).

Nos dicionários, podemos acessar valores por **chaves nomeadas** (ex: 'nome', 'idade').

---

## 📌 2. Como identificar estruturas em Python

* Tuplas → `()`
* Listas → `[]`
* Dicionários → `{}` ou `dict()`

---

## 📌 3. Criando um dicionário

```python
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])  # Pedro
```

---

## 📌 4. Adicionando elementos

```python
dados['sexo'] = 'M'
```

---

## 📌 5. Removendo elementos

```python
del dados['idade']
```

---

## 📌 6. Exemplo completo

```python
filme = {
    'título': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
```

---

## 📌 7. Métodos importantes

### 🔎 values()

Mostra apenas os valores:

```python
print(filme.values())
```

---

### 🔑 keys()

Mostra apenas as chaves:

```python
print(filme.keys())
```

---

### 📦 items()

Mostra chaves e valores:

```python
print(filme.items())
```

---

## 📌 8. Percorrendo dicionários

```python
for k, v in filme.items():
    print(f'O {k} é {v}')
```

Exemplo de saída:

```
O título é Star Wars
O ano é 1977
O diretor é George Lucas
```

---

## 📌 9. Junção com listas e dicionários

É possível armazenar dicionários dentro de listas.

```python
locadora = [
    {'filme': 'Star Wars', 'ano': 1977},
    {'filme': 'Avengers', 'ano': 2012}
]
```

Acesso:

```python
print(locadora[0]['ano'])  # 1977
```

---

## 🚀 Resumo

* Dicionários usam chaves ao invés de índices
* Estrutura: `{chave: valor}`
* `keys()` → chaves
* `values()` → valores
* `items()` → chave e valor
* podem ser usados dentro de listas
