# Projeto MaxMinDC

O **MaxMinDC** é um projeto que implementa um algoritmo de **divisão e conquista** para encontrar o menor e o maior elemento em uma lista de números. Essa abordagem reduz o número de comparações em relação a métodos tradicionais, utilizando a estratégia clássica de **Dividir, Conquistar e Combinar**.

---

## Descrição do Projeto

O objetivo do algoritmo é encontrar o **valor mínimo e o valor máximo** de uma lista numérica. Ele utiliza uma estratégia recursiva baseada na técnica de **divisão e conquista**. A ideia é dividir a lista em sublistas menores até que os casos base sejam alcançados (um ou dois elementos), conquistar os resultados localmente e, por fim, combinar os resultados das metades para obter o mínimo e o máximo global.

### Lógica do Código (linha a linha):

#### Função `max_min_dc(arr, low, high)`

- **Parâmetros:** `arr`: lista de números, `low`: índice inicial, `high`: índice final.
- Se `low == high`: há apenas um elemento → retorna este elemento como mínimo e máximo.
- Se `high == low + 1`: há dois elementos → retorna o menor e o maior com apenas uma comparação.
- Divide a lista em duas partes (índice médio `mid`).
- Chama recursivamente a função nas duas metades.
- Após obter `(min_esq, max_esq)` e `(min_dir, max_dir)`, retorna `min(min_esq, min_dir)` e `max(max_esq, max_dir)`.

#### Função `max_min_select(arr)`

- Verifica se a lista está vazia e levanta uma exceção (`ValueError`) caso esteja.
- Chama a função recursiva `max_min_dc` passando os limites da lista.

#### Bloco principal (`if __name__ == '__main__'`)

- Define uma lista de exemplo.
- Chama a função principal.
- Exibe o resultado no terminal.

---

## Como Executar o Projeto

### Requisitos

- Python 3.6 ou superior.
- Nenhuma dependência externa é necessária.

### Passos

1. Clone ou copie o arquivo Python para seu computador.
2. Execute o script com:

```bash
python nome_do_arquivo.py
```

> Substitua `nome_do_arquivo.py` pelo nome do seu arquivo `.py`.

### Exemplo de Saída

```py
Sequência: [7, 2, 9, 0, 4, 6, 3, 8, 1, 5]
Mínimo: 0
Máximo: 9
```

---

## Relatório Técnico

### Análise do Algoritmo

- O algoritmo reduz o número total de comparações em comparação com a abordagem ingênua (varrer toda a lista duas vezes).
- No pior caso, faz cerca de **3n/2 - 2** comparações para `n` elementos, contra **2n - 2** da abordagem ingênua.

### Complexidade Assintótica

- **Melhor caso:** O(log n) níveis de recursão e O(1) comparações por chamada.
- **Pior caso:** O(n), pois todo elemento é examinado ao menos uma vez.
- **Complexidade temporal:** O(n)
- **Complexidade espacial:** O(log n) devido à pilha de recursão.

### Vantagens

- Reduz número de comparações.
- Ideal para listas grandes.
- Baseado em princípios robustos de algoritmos.



### Análise da complexidade assintótica pela aplicação do Teorema Mestre

```plaintext
- Dado T(n) = 2T(n/2) + O(1)
1- Identificar os valores de a, b e f(n)
T(n) = aT(n/b) + f(n)
a = 2
b = 2
f(n) = O(1)

2- Calcule log_b(a) para determinar o valor de p
p = log_b(a)
p = log_2(2)
p = 1

4- Determine em qual dos três casos do Teorema Mestre esta recorrência se enquadra
Como f(n) = O(n^(1-epsilon)) = O(n^0), a recorrência se enquadra no caso 1.

Solução:
T(n) = Θ(n)


```

---

## Licença

Este projeto está licenciado sob a Licença MIT.