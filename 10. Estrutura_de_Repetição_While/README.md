# 🐍 Estrutura de Repetição While (Python)

---

## 📌 1. O que é o while

O `while` é uma estrutura de repetição usada quando **não sabemos exatamente quantas vezes o bloco será executado**.

Ele executa enquanto uma condição for verdadeira.

---

## 📌 2. Estrutura básica

### 🔧 Em linguagem natural

```
enquanto condição for verdadeira:
    executar ação
```

---

### 🐍 Em Python

```python
while condição:
    passo
```

---

## 📌 3. Exemplo básico

```python
c = 1

while c <= 10:
    print(c)
    c += 1
```

---

## 📌 4. Condição negada (not)

Também podemos usar `not` para inverter a lógica:

```python
while not condição:
    passo
```

### 🧠 Exemplo

```python
resposta = ''

while not resposta == 'sim':
    resposta = input('Digite sim para parar: ')
```

---

## 📌 5. Uso de condições dentro do while

É possível combinar o `while` com condições internas:

```python
while c <= 10:
    if c % 2 == 0:
        print(c)
    c += 1
```

---

## 📌 6. Características importantes

* O `while` depende de uma condição lógica
* Pode gerar loops infinitos se não houver controle
* Muito usado quando não se sabe o número de repetições

---

## 🚀 Resumo

* `while` → repete enquanto a condição for verdadeira
* usado quando não sabemos o número de repetições
* precisa de controle da condição para não entrar em loop infinito
* pode usar `not` e condições internas
