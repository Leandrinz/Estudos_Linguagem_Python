# 🐍 Condições (Python)

---

## 📌 1. Estrutura básica do if/else

Em Python, usamos condições para tomar decisões no código.

### 🔧 Sintaxe

```python
if condição:
    bloco verdadeiro
else:
    bloco falso
```

---

## 📌 2. Exemplo prático

```python
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

print('--FIM--')
```

---

## 📌 3. Condição simplificada (if inline)

Também podemos escrever condições de forma reduzida:

```python
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')
```

---

## 🧠 Como funciona a versão simplificada

```python
valor_se_verdadeiro if condição else valor_se_falso
```

---

## 🚀 Resumo

* `if` → executa se a condição for verdadeira
* `else` → executa se for falsa
* versão simplificada → `A if condição else B`
