# 🐍 Cores no Terminal (Python)

---

## 📌 1. Código de cores ANSI

Para adicionar cores no terminal, usamos o padrão:

```python
\033[style;text;backm
```

### 🔧 Exemplo

```python
\033[0;33;44m
```

---

## 📌 2. Estrutura

* **style** → estilo da fonte
* **text** → cor do texto
* **back** → cor de fundo

---

## 🎨 3. Style (estilo da fonte)

| Código | Significado              |
| ------ | ------------------------ |
| 0      | Sem estilo               |
| 1      | Negrito                  |
| 4      | Sublinhado               |
| 7      | Negativo (inverte cores) |

---

## 📝 4. Cores do texto

| Código | Cor        |
| ------ | ---------- |
| 30     | Branco     |
| 31     | Vermelho   |
| 32     | Verde      |
| 33     | Amarelo    |
| 34     | Azul       |
| 35     | Roxo       |
| 36     | Azul claro |
| 37     | Cinza      |

---

## 🎨 5. Cores de fundo

| Código | Cor        |
| ------ | ---------- |
| 40     | Branco     |
| 41     | Vermelho   |
| 42     | Verde      |
| 43     | Amarelo    |
| 44     | Azul       |
| 45     | Roxo       |
| 46     | Azul claro |
| 47     | Cinza      |

---

## 🧪 6. Exemplo completo

```python
print('\033[0;33;44mTexto colorido\033[m')
```

---

## 🚀 Resumo

* Formato: `\033[style;text;backm`
* style → estilo da fonte
* text → cor do texto
* back → cor de fundo
* `\033[m` → reset das cores
