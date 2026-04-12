# 🐍 Módulos (Python)

---

## 📌 1. O que são módulos

Módulos são bibliotecas prontas do Python que adicionam funcionalidades ao código.

---

## 📌 2. Como importar um módulo

Para usar uma biblioteca, utilizamos:

```python
import nome_do_modulo
```

---

## 📌 3. Como usar funções do módulo

Após importar, usamos o nome do módulo seguido de `.`:

```python
import math
math.nome_da_funcao()
```

---

## 📌 4. Módulo random

O módulo `random` é usado para gerar números aleatórios.

### 🔧 Importação

```python
import random
```

---

### 🎲 random.random()

Gera um número aleatório entre 0 e 1.

```python
random.random()
```

---

### 🎯 random.randint(x, y)

Gera um número inteiro aleatório dentro de um intervalo.

```python
random.randint(1, 10)
```

Exemplo: pode gerar qualquer número entre 1 e 10.

---

## 🚀 Resumo

* `import nome` → importa um módulo
* `módulo.funcao()` → usa uma função do módulo
* `random.random()` → número entre 0 e 1
* `random.randint(x, y)` → número inteiro aleatório entre x e y
