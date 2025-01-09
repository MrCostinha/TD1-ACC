# Projeto: Divisão do Conjunto

## Descrição do Problema

O **Problema da Divisão do Conjunto** busca determinar se um conjunto de números inteiros pode ser dividido em dois subconjuntos disjuntos, de forma que a soma dos elementos em cada subconjunto seja igual. Por exemplo, o conjunto O = {8, 3, 21, 12, 4} pode ser dividido em M = {4, 8, 12} e N = {3, 21}, pois M e N são disjuntos e a soma dos elementos de M é igual â soma dos elementos de N, que é 24.

### Aplicabilidade Prática

* **Alocação de recursos em computação em nuvem:** Divisão eficiente de recursos como memória, CPU e armazenamento entre diferentes aplicações em nuvem, garantindo que cada aplicação tenha os recursos necessários para funcionar de forma ideal.
* **Design de experimentos:** Dividir participantes de um estudo em grupos de controle e experimentais com características similares.

## Algoritmos Implementados

1. **Divisão e Conquista:**  Este algoritmo aborda o problema de forma recursiva, dividindo-o em subproblemas menores e mais simples. A cada passo, ele decide se inclui o próximo número em um subconjunto ou no outro, explorando ambas as possibilidades e combinando os resultados para verificar se alguma combinação leva a uma divisão válida do conjunto original.
2. **Algoritmo Guloso:** Este algoritmo utiliza uma heurística para tentar encontrar uma solução de forma eficiente, mas não garante que a solução encontrada seja a ideal. Ele ordena os números em ordem decrescente e, a cada passo, adiciona o próximo número ao subconjunto que possui a menor soma no momento. Essa estratégia visa equilibrar as somas dos subconjuntos, buscando uma divisão aproximada do conjunto original.