# 🐍 Condições Aninhadas (Python)

---

## 📌 1. O que são condições aninhadas

Condições aninhadas são usadas quando precisamos de **mais de dois caminhos possíveis** no programa.

Em vez de apenas `if` e `else`, usamos também `elif`.

---

## 📌 2. Estrutura básica

```python
if condição1:
    bloco 1
elif condição2:
    bloco 2
else:
    bloco final
```

---

## 📌 3. Como funciona

* `if` → primeira condição
* `elif` → outras condições intermediárias (pode ter vários)
* `else` → caso nenhuma condição seja verdadeira

---

## 📌 4. Exemplo simples

```python
nota = int(input('Digite sua nota: '))

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')
```

---

## 📌 5. Regras importantes

* Pode ter **vários `elif`**
* Só pode ter **um `if` no início**
* Só pode ter **um `else` no final**
* O Python executa de cima para baixo

---

## 🚀 Resumo

* `if` → primeira condição
* `elif` → condições intermediárias
* `else` → caso contrário
* usado quando há **mais de 2 caminhos possíveis**
