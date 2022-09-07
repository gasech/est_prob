# Importei uma biblioteca para realizar operações de raiz quadrada
import math

# Dados simples afim de realizar testes
dados_teste = [8,3,4,1,2,5,3,4,7]

## 1. Crie um programa que leia os dados (se for difícil fazer isto de forma automática, faça que o programa permita 
## a digitação manual de cada dado).

with open('dados.csv') as f:
    arquivo = f.readlines()

# Converte os dados de String para Int
arquivo_dados = []
for i in range(len(arquivo)):
  arquivo_dados.append(int(arquivo[i])) 

## 2. Inclua em seu programa uma rotina que organize e exiba os 40 dados em ordem crescente (rol).
def ordenar_dados(dados):
    # Ordena os dados
    dados.sort()
    return dados

## 3. Inclua em seu programa uma rotina que calcule e apresente a média dos 40 dados.
def calcular_media(dados):
    quantidade_itens = len(dados)
    soma_itens = 0
    
    for dado in dados:
        soma_itens = soma_itens + dado
    
    media = soma_itens / quantidade_itens
    
    return media

## 4. Inclua em seu programa uma rotina que determine e exiba a mediana dos 40 dados.
def calcular_mediana(dados):
    # Ordena os Dados
    dados = ordenar_dados(dados)

    tamanho_dados = len(dados)

    # Divide o tamanho dos dados por 2 com arrendodamento
    indice = (tamanho_dados - 1) // 2
   
    if (tamanho_dados % 2):
        # Caso o tamanho dos dados seja impar ele retorna a posição do indice
        return dados[indice]
    else:
        # Caso o tamanho dos dados seja par ele retorna a posição do indice e indice + 1 somados e depois divide por 2
        return (dados[indice] + dados[indice + 1]) / 2   
   
##  5. Inclua em seu programa uma rotina que verifique se existe uma (ou mais) moda(s) entre os 40 dados. Caso exista(m),
##  o programa deve apresentá-la(s). 
def calcular_moda(dados):
    ocorrencias = {}
    moda = []
    quantidade_max = 0

    for dado in dados:
        if dado in ocorrencias:
            ocorrencias[dado] = ocorrencias[dado] + 1
        else:
            ocorrencias[dado] = 1
    
        if ocorrencias[dado] == quantidade_max:
            moda.append(dado)
        elif ocorrencias[dado] > quantidade_max:
            moda = []
            moda.append(dado)
            quantidade_max = ocorrencias[dado]
    
    return moda

## 6. Inclua em seu programa uma rotina que calcule e apresente o desvio absoluto médio dos 40 dados.
def calcular_desvio_medio_absoluto(dados):
    media = calcular_media(dados)
    diferencas = []
    
    for dado in dados:
        diferenca = 0

        if media > dado:
            diferenca = media - dado
        else:
            diferenca = dado - media
        
        diferencas.append(diferenca)

    desvioAbsolutoMedio = calcular_media(diferencas)

    return desvioAbsolutoMedio

## 7. Inclua em seu programa uma rotina que calcule e apresente a variância e o desvio padrão dos 40 dados. 
## Obs.: como estamos lidando com mais de 30 dados, não é necessário usar a correção (n-1) no cálculo da variância.
def calcular_variancia_desvio_padrao(dados):
    media = calcular_media(dados)
    diferencas = []
    
    for dado in dados:
        diferenca = 0

        if media > dado:
            diferenca = media - dado
        else:
            diferenca = dado - media
        
        diferencas.append(diferenca * diferenca)

    variancia_desvio_padrao = [0, 0]
    variancia_desvio_padrao[0] = calcular_media(diferencas)
    variancia_desvio_padrao[1] = math.sqrt(variancia_desvio_padrao[0])

    return variancia_desvio_padrao

## 8. Inclua em seu programa uma rotina que agrupe os 40 dados em 7 classes (sugestão óbvia: classes de 0 a 10, 10 a
## 20, 20 a 30 e assim por diante) e apresente a distribuição de frequências destas classes. Esta tabela de distribuição
## de frequências deve ter colunas para as classes, ponto médio de cada classe (xi), frequências absolutas (ni),
## frequências relativas (ou proporções, fi) e porcentagens (%, obtidas como 100*fi). 

## 9. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima,
## apresente um histograma da distribuição. Caso a apresentação de um histograma seja muito difícil na linguagem
## de programação com a qual você esteja trabalhando, tente apresentar ao menos um diagrama de ramos-e-folhas
## dos dados, ou um gráfico de dispersão unidimensional (aquele dos pontinhos).


## 10. Inclua em seu programa uma rotina que calcule a média usando os dados agrupados em classes (item 8. acima).
## Verifique se há alguma diferença entre esta média e aquela calculada no item 3. acima. Caso haja alguma
## diferença, explique por que isso ocorre.


## 11. Inclua em seu programa uma rotina que determine a(s) classe(s) modal(is) da distribuição de frequências
## construída no item 8. acima.


## 12. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima, calcule
## e apresente o desvio absoluto médio. Verifique se há alguma diferença entre este desvio absoluto médio e aquele
## calculado no item 6. acima. Caso haja alguma diferença, explique por que isso ocorre.


## 13. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima, calcule
## e apresente a variância e o desvio padrão. Verifique se há alguma diferença entre a variância e o desvio padrão
## assim calculados e aqueles calculados no item 7. acima. Caso haja alguma diferença, explique por que isso ocorre.
## Obs.: como estamos lidando com mais de 30 dados, não é necessário usar a correção (n-1) no cálculo da variância.

    
