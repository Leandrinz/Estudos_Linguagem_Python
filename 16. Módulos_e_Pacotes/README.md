# 🐍 Módulos e Pacotes (Python)

---

## 📌 1. Modularização

Modularização é o processo de **dividir um programa grande em partes menores** chamadas módulos.

### 🎯 Objetivos

* Dividir o programa em partes menores
* Melhorar a legibilidade
* Facilitar manutenção

### ✅ Vantagens

* Organização do código
* Facilidade de manutenção
* Ocultação de detalhes internos
* Reutilização em outros projetos

---

## 📌 2. Módulos

Módulos são arquivos Python com funções, variáveis e códigos reutilizáveis.

### 🔧 Exemplo de uso

```python
import modulo
```

Ou importando funções específicas:

```python
from modulo import funcao
```

---

## 📌 3. Pacotes

Quando os módulos começam a ficar grandes, usamos **pacotes**.

Pacotes são **pastas que agrupam vários módulos**.

---

### 📁 Estrutura de pacotes

```
pasta/
│-- modulo1.py
│-- modulo2.py
│-- __init__.py
```

---

### 🔧 Como importar pacotes

```python
import pasta
from pasta import funcao
```

---

## 📌 4. Exemplos de uso de pacotes

Pacotes podem organizar funcionalidades por categoria:

* 🎨 Cores
* 📅 Datas
* 🔢 Números
* 🔤 Strings

---

## 🚀 Resumo

* Modularização → dividir o código em partes menores
* Módulos → arquivos Python reutilizáveis
* Pacotes → conjunto de módulos em uma pasta
* `import` → importa módulos
* `from ... import ...` → importa funções específicas
