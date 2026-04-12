# 🐍 Tuplas (Python) / Variáveis Compostas

---

## 📌 1. Problema das variáveis simples

Uma variável comum guarda apenas um valor por vez.

```python
lanche = 'hamburguer'
```

A variável `lanche` ocupa um espaço na memória com esse valor.

---

Se atribuirmos outro valor:

```python
lanche = 'suco'
```

O valor anterior é substituído.

✔️ O espaço não guarda mais de um valor ao mesmo tempo.

---

## 📌 2. Solução: Tuplas

Tuplas permitem armazenar **vários valores em uma única variável**.

```python
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
```

---

## 📌 3. Acesso aos elementos

Cada item da tupla possui um índice:

```python
lanche[0]  # hamburguer
lanche[1]  # suco
lanche[2]  # pizza
lanche[3]  # pudim
```

---

## 📌 4. Característica principal

### ⚠️ Tuplas são IMUTÁVEIS

Isso significa que:

* Não podem ser alteradas depois de criadas
* Não é possível adicionar ou remover elementos

```python
lanche[0] = 'x-burguer'  # ❌ erro
```

---

## 📌 5. Exemplo completo

```python
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
```

---

## 🚀 Resumo

* Variável comum → guarda apenas 1 valor
* Tupla → guarda vários valores
* Acesso por índice → lanche[0], lanche[1]...
* Tuplas são imutáveis (não podem ser alteradas)
