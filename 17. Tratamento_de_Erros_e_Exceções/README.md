# 🐍 Tratamento de Erros e Exceções (Python)

---

## 📌 1. O que são erros e exceções

* **Erros de sintaxe** → acontecem quando o código está escrito de forma incorreta.
* **Exceções** → erros que acontecem أثناء a execução do programa.

---

## 📌 2. Estrutura try / except

Permite tratar erros e evitar que o programa quebre.

```python
try:
    # operação
    pass
except:
    # caso dê erro
    pass
```

---

## 📌 3. Capturando o erro

Podemos capturar a exceção para analisar o problema:

```python
try:
    # operação
    pass
except Exception as erro:
    print(f"Problema encontrado foi: {erro}")
```

---

## 📌 4. else (quando não há erro)

O bloco `else` executa quando não ocorre nenhuma exceção.

```python
try:
    # operação
    pass
except Exception as erro:
    print(f"Erro: {erro}")
else:
    print("Tudo ocorreu bem")
```

---

## 📌 5. finally (sempre executa)

O bloco `finally` é opcional e sempre será executado.

```python
try:
    # operação
    pass
except Exception as erro:
    print(f"Erro: {erro}")
else:
    print("Tudo ocorreu bem")
finally:
    print("Fim do processo")
```

---

## 📌 6. Estrutura completa

```python
try:
    # operação
    pass
except Exception as erro:
    print(f"Problema encontrado: {erro}")
else:
    print("Sem erros")
finally:
    print("Execução finalizada")
```

---

## 🚀 Resumo

* `try` → tenta executar o código
* `except` → trata o erro
* `else` → executa se não houver erro
* `finally` → sempre executa
* `Exception as erro` → captura detalhes do erro
