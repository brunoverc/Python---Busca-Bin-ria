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

### Complexidade do Algoritmo

- Iterativa:

| Passo                    | Complexidade     | Justificativa                                            |
|--------------------------|------------------|----------------------------------------------------------|
| Inicialização            | O(1)             | Operações simples de atribuição e cálculo de índices     |
| Loop While               | O(log n)         | O número máximo de iterações é logarítmico na quantidade de elementos na lista, devido à divisão pela metade a cada iteração |
| Condições dentro do Loop | O(1)             | As operações dentro do loop (verificação de índices, comparação de elementos) são de complexidade constante |
| Total                    | O(log n)         | A complexidade total é dominada pelo loop while, que tem complexidade logarítmica devido à busca binária          |

A complexidade de tempo do algoritmo de busca binária iterativa é O(log n), onde n é o tamanho da lista. Isso ocorre porque a lista é dividida ao meio a cada iteração, reduzindo pela metade o espaço de busca. Isso resulta em um tempo de execução eficiente, especialmente para listas grandes.

- Recursiva:

| Passo                    | Complexidade     | Justificativa                                            |
|--------------------------|------------------|----------------------------------------------------------|
| Chamada inicial          | O(1)             | Uma única chamada inicial com parâmetros específicos     |
| Condição Base da Recursão| O(1)             | Verificação se o índice final é maior ou igual ao inicial |
| Cálculo do meio          | O(1)             | Cálculo do índice do elemento do meio da lista           |
| Comparação               | O(1)             | Comparação do elemento do meio com o valor procurado     |
| Chamada recursiva        | O(log n)         | A cada chamada, a lista é dividida pela metade           |
| Total                    | O(log n)         | A complexidade total é dominada pela chamada recursiva, que tem complexidade logarítmica devido à busca binária |

A complexidade total do algoritmo é dominada pelas chamadas recursivas, que têm complexidade logarítmica devido à busca binária. Portanto, a complexidade de tempo do algoritmo de busca binária recursiva é O(log n), onde n é o tamanho da lista, o algoritmo de busca binária recursiva é eficiente para encontrar elementos em listas ordenadas devido à sua complexidade logarítmica, que reduz a quantidade de elementos a serem verificados drasticamente a cada chamada recursiva.

- Ordenada:

| Passo                    | Complexidade     | Justificativa                                            |
|--------------------------|------------------|----------------------------------------------------------|
| Inicialização da Variável| O(1)             | Operação simples de atribuição                           |
| Loop While               | O(n)             | O número máximo de iterações é linear na quantidade de elementos na lista |
| Condições Dentro do Loop | O(1)             | As operações dentro do loop (verificação de igualdade, comparações) são de complexidade constante |
| Total                    | O(n)             | A complexidade total é dominada pelo loop while, que tem complexidade linear em relação ao tamanho da lista |

## Análise de T(n)

A complexidade de tempo do algoritmo de busca sequencial ordenada é dominada pelo loop while, que tem uma complexidade linear, O(n), onde n é o tamanho da lista. Isso ocorre porque o algoritmo precisa percorrer a lista elemento por elemento até encontrar o valor procurado ou determinar que o valor não está na lista.

Para as funções divide and conquer no método interativo e recursivo a analise de tempo de execução é igual:
Podemos representar isso em termos de uma série geométrica:
𝑛, , , , …, 1
T(n) = aT(n/b) + f(n)
T(n) = T(n/b)
T(n) = T(
Onde x é o número de iterações.
 
### Solução:
 
O(n) =
 
T(n) = O(log(n))
 
Para o método Linear:
T(n) = an + b
T(n) = an
Sendo a constante, temos:
T(n) = O(n)


