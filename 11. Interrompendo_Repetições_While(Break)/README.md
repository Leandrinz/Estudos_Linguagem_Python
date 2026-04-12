# 🐍 Interrompendo Repetições While (break)

---

## 📌 1. O que é o break

O `break` é um comando usado para **interromper imediatamente um laço de repetição**.

Quando ele é executado, o loop é encerrado e o programa continua após ele.

---

## 📌 2. Simulando um do while no Python

O Python não possui estrutura `do while`, mas podemos simular usando `while True`.

---

## 📌 3. Estrutura básica

```python
while True:
    if condição1:
        passo

    if condição2:
        pula

    if condição3:
        pega

    if condição4:
        pula
        break  # interrompe o loop

    pega
```

---

## 📌 4. Como o break funciona

* Ele encerra o loop imediatamente
* Não executa mais nada dentro do `while`
* Sai direto para a próxima parte do código

---

## 📌 5. Exemplo simples

```python
while True:
    numero = int(input('Digite um número (0 para parar): '))

    if numero == 0:
        break

    print('Você digitou:', numero)
```

---

## 📌 6. Característica importante

* `while True` cria um loop infinito
* `break` é responsável por controlar a saída

---

## 🚀 Resumo

* `break` → interrompe o loop
* `while True` → loop infinito controlado manualmente
* simula o comportamento de um `do while`
