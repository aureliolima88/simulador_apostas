# 🎲 Simulador de Apostas Numéricas

> ⚠️ **Aviso Importante**
>
> Este simulador **não garante** que você irá acertar todos os números ou ganhar qualquer prêmio.
> O projeto foi desenvolvido **exclusivamente para fins educacionais**, com o objetivo de reforçar conceitos de programação em Python, como combinações, amostragem aleatória e estrutura de classes.
---

## 📌 Sobre o Projeto

O **Simulador de Apostas Numéricas** é uma aplicação em Python que gera combinações aleatórias de números e estrelas, inspirado em jogos de loteria como o EuroMillions.

A ideia central é permitir a criação de múltiplas apostas automáticas, respeitando regras configuráveis como:

* Quantidade total de números disponíveis
* Quantidade de estrelas disponíveis
* Quantidade de números por jogo
* Quantidade de estrelas por jogo
* Número total de apostas a serem geradas

---

## ⚙️ Funcionalidades

* ✅ Geração de combinações aleatórias sem repetição
* ✅ Configuração personalizada dos parâmetros do jogo
* ✅ Armazenamento das apostas em memória
* ✅ Exibição formatada dos resultados no console
* ✅ Uso de conceitos como:

  * `itertools.combinations`
  * `random.sample`
  * Programação orientada a objetos (POO)

---

## 🧠 Conceitos Aplicados

Este projeto foi criado para praticar e consolidar:

* Manipulação de listas
* Geração de combinações matemáticas
* Aleatoriedade controlada
* Estruturação de classes em Python
* Organização e documentação de código

---

## 📂 Estrutura do Código

A classe principal do projeto é:

### `JogoAposta`

Responsável por:

* Definir os parâmetros do jogo
* Gerar combinações de números e estrelas
* Armazenar os resultados
* Exibir os jogos gerados

---

## 🚀 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/aureliolima88/simulador_apostas
```

### 2. Execute o script

```bash
python main.py
```

---

## 🛠️ Exemplo de Uso

```python
if __name__ == '__main__':
    jogo = JogoAposta(10)  # quantidade de limites, não ultrapassando as 66 combinações possíveis de estrela
    jogo.gerar_combinacoes()
```

---

## 📊 Exemplo de Saída

```
JOGO Nº 1: JOGO: 3 12 25 33 49 ESTRELA: 2 7
JOGO Nº 2: JOGO: 1 9 18 27 45 ESTRELA: 3 11
...
```

---

## ⚠️ Limitações

* O número de combinações solicitadas (`limite`) **não pode exceder** o total de combinações possíveis.
* O sistema não verifica automaticamente esse limite.
* Não há persistência de dados (os jogos são armazenados apenas em memória).

---

## 📈 Possíveis Melhorias

* [ ] Validação automática do limite de combinações
* [ ] Exportação dos resultados para arquivo (CSV/JSON)
* [ ] Interface gráfica (GUI)
* [ ] Integração com APIs de resultados reais
* [ ] Testes automatizados

---

## 🤝 Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por Aurélio Lima, para fins de estudo e prática em Python.

---

