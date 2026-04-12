# 🐍 Listas (Python) - Parte 2

---

## 📌 1. Listas dentro de listas

É possível armazenar listas dentro de outras listas.

```python
pessoas = []
dados = ['Pedro', 25]
```

---

## 📌 2. Adicionando uma lista dentro de outra

Para evitar ligação entre os dados, usamos cópia:

```python
pessoas.append(dados[:])
```

---

## 📌 3. Estrutura resultante

Agora temos uma lista dentro de outra lista:

```
pessoas[0] → ['Pedro', 25]
```

Dentro dela:

```
'pessoas[0][0]' → Pedro
'pessoas[0][1]' → 25
```

---

## 📌 4. Exemplo completo

```python
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
```

---

## 📌 5. Acessando elementos

```python
print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])     # ['Maria', 19]
```

---

## 🧠 6. Entendendo os índices

| Índice externo | Conteúdo      | Índices internos   |
| -------------- | ------------- | ------------------ |
| pessoas[0]     | ['Pedro', 25] | 0 = Pedro / 1 = 25 |
| pessoas[1]     | ['Maria', 19] | 0 = Maria / 1 = 19 |
| pessoas[2]     | ['João', 32]  | 0 = João / 1 = 32  |

---

## 🚀 Resumo

* Listas podem conter outras listas
* Estrutura: lista dentro de lista
* Acesso: `lista[linha][coluna]`
* `[:]` evita ligação de dados
