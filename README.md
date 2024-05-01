# Avaliação de Desempenho de Algoritmos de Busca

Este projeto consiste na avaliação de desempenho de três algoritmos de busca: Busca Binária Recursiva, Busca Binária Iterativa e Busca Linear. O objetivo é comparar o tempo de execução desses algoritmos em diferentes cenários.

## Algoritmos Implementados

### Busca Binária Recursiva

A busca binária recursiva é implementada pela função `binary_search_recursion`, que divide repetidamente a lista de busca ao meio até encontrar o valor desejado.

### Busca Binária Iterativa

A busca binária iterativa é implementada pela função `binary_search_iteration`, que realiza uma busca eficiente em uma lista ordenada dividindo-a ao meio sucessivamente.

### Busca Linear

A busca linear é implementada pela função `ordered_sequential_search`, que percorre linearmente a lista até encontrar o valor desejado.

## Análise de Desempenho

Para avaliar o desempenho dos algoritmos, foram realizadas análises em diferentes cenários:

- **Busca em Palavras de um Arquivo Texto:**
  - Foi realizado um teste de busca em um arquivo com 245366 palavras da língua portuguesa, medindo o tempo de execução de cada algoritmo.

- **Busca em Arrays Numéricos Ordenados:**
  - Foram criadas amostras de tamanhos diferentes com valores numéricos ordenados.
  - Para cada tamanho de amostra, um número aleatório dentro do array foi selecionado para busca, medindo o tempo de execução de cada algoritmo.

## Executando o Código

Para executar a comparação de desempenho entre os algoritmos, execute o notebook `Comparacao_Desempenho_Algoritmos.ipynb`. Certifique-se de ter as dependências necessárias instaladas.

### Dependências

- Python 3.x
- Jupyter Notebook
- Bibliotecas: time, random, matplotlib e pandas

## Resultados e Conclusões

Os resultados obtidos mostram que a busca binária, tanto na sua versão recursiva quanto iterativa, é significativamente mais eficiente do que a busca linear, especialmente em conjuntos de dados maiores e ordenados.

## Contribuições

Contribuições e sugestões são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests para melhorar este projeto.

