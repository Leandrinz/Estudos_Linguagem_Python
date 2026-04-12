# 🐍 Tipos Primitivos e Saída de Dados (Python)

---

## 📌 1. Tipos primitivos com input()

O `input()` sempre retorna **texto (string)**. Para trabalhar com números, precisamos converter o tipo.

### 🔧 Exemplo

```python
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
```

### 🧠 O que está acontecendo:

* `input()` → recebe como string
* `int()` → converte para número inteiro

---

## 📌 2. Operação com variáveis

```python
s = n1 + n2
```

Aqui ocorre a soma dos dois números.

---

## 📌 3. Saída de dados com print

### 🔧 Usando `.format()`

```python
print('A soma vale {}'.format(s))
```

---

## 📌 4. Como o format funciona

O `.format()` substitui as chaves `{}` pelo valor passado.

### Exemplo:

```python
'A soma vale {}'.format(s)
```

Se `s = 10`, o resultado será:

```
A soma vale 10
```

---

## 📌 5. Exemplo completo

```python
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
s = n1 + n2
print('A soma vale {}'.format(s))
```

---

## 🚀 Resumo

* `input()` → sempre retorna string
* `int()` → converte para inteiro
* `+` → soma valores numéricos
* `.format()` → insere valores dentro do texto
