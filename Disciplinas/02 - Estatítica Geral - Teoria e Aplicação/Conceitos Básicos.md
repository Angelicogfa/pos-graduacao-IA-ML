### Introdução a Estatistica

[Simbolos](https://latex.wikia.org/wiki/List_of_LaTeX_symbols) matemáticos/estatisticos

> Conceitos básicos da Estatística

* População: Todos os elementos existentes.
* Amostragem: Sub-conjunto de itens da população.
* Parâmetros: São as informações obtidas atraves de análises (médias, percentuais...) com base em todos os indivíduos da população.
* Estatíticas: São as informações obtidas atraves de analises com base nos indivíduos de uma amostragem.

> Tipos de dados

Tipo de dado ou variável é a forma que classificamos toda informação obtida durante uma pesquisa. E elas são classificadas de forma diferente de acordo com a natureza dessa informação, sendo elas:

* **Qualitativas** ou **categórias**: Consistem dem atributos, qualidades, caracteríticas.
  * *Nominais*: Representam nomes, rotulos ou categorias que não tem ordem ou hierarquia (ex: categorias sem ordem ou hierarquia). 
  * *Ordinais*: Mantêm uma relação de ordem do menor para o maior (ex: carinha na avaliação de um atendimento).
* **Quantitativos** ou **numéricas**: Consistem em medidas ou contagens numéricas.
  * *Discretas*: Resultam de um conjunto finido ou enumerável de valores possíveis - **quantidade**. (ex: número de alunos; números de ventiladores com defeitos. Normalmente são números inteiros)
  * *Continuas*: Resultam em um número infinito de valores possíveis - **mensuração**. (ex: medição de uma área; peso; altura; volume; área. Podem vir em valores inteiros ou decimal)

> Medidas de tendência central

São meios de verificar como os dados estão distribuidos. Se eles se encontram mais centralizados ou se tendem para alguma ponta.

* **Média Aritmetica Simples**: É a soma de todos os registros dividido pela quantidade.
  * A média de uma amostragem é identificada pelo simbolo: $\overline{x}$
  * A média de uma população é identificada pelo simbolo: $\mu$
*  **Mediana**: É o valor que divide a amostra em duas partes iguais.
   *  Quando a quantidade de elementos é par: $\frac{n+2}{2}$
   *  Quando a quantidade de elementos é impar:  $\frac{n}{2}$
*  **Moda**: É o valor que aparece com maior frequência na amostragem.
   *  Normalmente é mais utilizado com dados do tipo categórico; Pode existir uma ou mais moda ou até mesmo nenhuma.

> Medidas de posição relativa

Representa dentro da estatistica medidas que dividem nossa amostra em determinadas parcelas.

* **Score z**: Mede os valores da amostra em relação à media, expresso em desvio padrão.
  * Escore Z = $\frac{x - \overline{x}}{S}$
* **Quartil**: São divididos em 3 quartis, dividindo a amostra em 4 partes, tendo cada parte 25% dos dados. São separados em: `min, 25%, 50%, 75%, max`.
* **Decis**: São divididos em 9 partes, dividindo a amostra em 10 partes, tendo cada parte com 10% dos dados. São separados em: `min, 10%, 20%...80%, 90%, max`.
* **Percentis**: São divididos em 99 partes, dividindo a amostra em 100 partes, tendo cada parte com 1% dos dados. São separados em: `min, 1%, 2%...98%, 99%, max`.

Para calcular os divisores, vamos usar apenas o calculo do *percentil* pois esse pode ser facilmente transposto para os outros `P -> Q` ou `P -> D`.

Para calcular devemos primeiro seguir os seguintes passos: 
* Ordenar os dados do menor para o maior (ordem crescente);
* Calcular a posição ocupada pelo percentil $\mathrm{P}{k}$ por meio da seguinte formula: L=[$\frac{k}{100}$]\.n
  * onde, `n` é o tamanho da amostra, `k` é o percentil que deseja calcular e `L` é a posição do percentil na amostra.
  * Se o valor de `L` é um *número inteiro* o percentil $\mathrm{P}{k}$ será obtido pela média entre os valores que ocupam as posições L e L+1.
  * Se o valor de `L` é um *número decimal* devemos arredondar o valor de `L` para o *maior inteiro* mais proximo, ai sim o percentil $\mathrm{P}{k}$ será obtido pelo valor que ocupa a posição `L` já arredondada.

>> Exemplos

Dado os seguintes dados:
```python
itens = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]
n = len(itens)
print(n)
12
```
---
Calcule o 3º Quartil:
Sabemos que o terceiro quartil corresponde ao percentil 75. Dessa forma temos que a posição do 3º quartil na amostra é:

```math
L=(\frac{k}{100}).n = (\frac{75}{100}).12 = 9º posição
```

```python
item1 = itens[8]
item2 = itens[9]
print(item1, item2)
77 79
```

```math
Q_3 = P_\mathrm{75} = \frac{77+79}{2}=78
```

```
Aproximadamente 75% dos consumidores demoram até 78 segundos entre início e a finalizaçã da compra.
```
---

Calcule o 4º Decil
Sabemos que o 4º decil corresponde ao percentil 40. Dessa forma, a posição do 4º na amostra é:

```math
L = (\frac{4}{100}).n = (\frac{40}{100}).12 = 4,8 
```

Como a posição obtida em `L` é decimal, para obtermos o 4º decil devemos encontrar o valor que ocupa a 5º posição da amostra.

```python
item = itens[4]
print(item)
74
```

```
Aproximadamente 40% dos consumidores demoram 74 segundos entre o inicio e a finalização da compra.
```
---

10% dos consumidores mais rápidos demoram, no máximo, quantos segundos entre início e a finalização da compra ?

Calcule o 10º percentil.

```math
L=(\frac{k}{100}).n = (\frac{10}{100}).12 = 1,2
```

Como a posição obtida em `L` é decimal, para obtermos o 10º decil devemos encontrar o valor que ocupa a 2º posição da amostra.

```python
item = itens[1]
print(item)
73
```
---
20% dos consumidores demoram, no mínimo, quantos segundos entre o início e a finalização da compra ?

Calculo o 20º percentil

```math
L = (\frac{x}{100}).n = (\frac{20}{100}).12 = 2,4
```
Como a posição obtida em `L` é decimal, para obtermos o 20º decil devemos encontrar o valor que ocupa a 3º posição da amostra.

```python
item = itens[2]
print(item)
73
```
---
Calcule o `score z` para o menor e o maior valor da amostragem

```math
\overline{x} = \frac{71 + 73 ... 81 + 83}{12} = 76,0833
```
```math
S = \surd{\frac{(71-76,0833)^2 + (73-76,0833)^2... (81-76,0833)^2 + (83-76,0833)^2}{12-1}} = 3,5280
```

Calculando o `score z` para o menor valor da amostra temos:
```math
Escore Z =  \frac{x - \overline{x}}{S} = \frac{71-76,0833}{3,5280} = -1,4408
```

```
O consumidor mais rapido está a 1,4408 desvio padrão ABAIXO da média do tempo gasto entre o início e a finalização da compra.
```

Calculando o `score z` para o maior valor da amostra temos:
```math
Escore Z =  \frac{x - \overline{x}}{S} = \frac{83-76,0833}{3,5280} = +1,9605
```

```
O consumidor mais lento está a 1,9605 desvio padrão ACIMA da média do tempo gasto entre o início e a finalização da compra.
```

