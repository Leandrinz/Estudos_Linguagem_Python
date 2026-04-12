# 🐍 Estrutura de Repetição For (Python)

---

## 📌 1. O que é o for

O `for` é uma estrutura de repetição usada para executar um bloco de código várias vezes.

---

## 📌 2. Sintaxe básica

```python
for c in range(1, 10):
    passo
```

### 🧠 Explicação

* `c` → variável de controle (nome ilustrativo)
* `range()` → define o intervalo da repetição

---

## 📌 3. Usando condições dentro do for

É possível colocar condicionais dentro do laço:

```python
for c in range(1, 10):
    if c % 2 == 0:
        print(c)
```

---

## 📌 4. Repetição decrescente

Para contar de trás para frente, usamos `-1`:

```python
for c in range(10, 1, -1):
    print(c)
```

---

## 📌 5. Pulando valores

Também é possível definir o passo da repetição:

```python
for c in range(1, 10, 2):
    print(c)
```

### 🧠 Explicação

* O último valor do `range` define o salto (step)
* Ex: `2` → pula de 2 em 2

---

## 🚀 Resumo

* `for` → repetição
* `range(início, fim, passo)`
* passo negativo → ordem decrescente
* passo positivo → define o intervalo de salto
* pode usar `if` dentro do laço
