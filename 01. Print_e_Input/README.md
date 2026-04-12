# 🐍 Print e Input (Python)

---

## 📌 1. input()

A função `input()` é usada para receber dados do usuário pelo teclado.

### 🔧 Exemplo

```python
nome = input('Qual é o seu nome?: ')
idade = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')
```

### 🧠 Importante

* Tudo o que vem do `input()` é tratado como **string (texto)**
* Mesmo números são armazenados como texto

---

## 📌 2. print()

A função `print()` exibe valores na tela.

### 🔧 Exemplo

```python
print(nome, idade, peso)
```

---

## 📌 3. Exemplo completo

```python
nome = input('Qual é o seu nome?: ')
idade = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')

print(nome, idade, peso)
```

---

## 📌 4. Como o print funciona nesse caso

O `print()` pode receber vários valores separados por vírgula:

```python
print(nome, idade, peso)
```

Ele imprime tudo separado por espaço automaticamente.

---

## 🚀 Resumo

* `input()` → recebe dados do usuário (sempre texto)
* `print()` → exibe dados na tela
* vírgulas no `print()` → separam os valores automaticamente
