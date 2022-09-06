## 1. Crie um programa que leia os dados (se for difícil fazer isto de forma automática, faça que o programa permita a digitação manual de cada dado).
with open('dados.csv') as f:
    arquivo = f.readlines()

# Converte os dados de String para Int
arquivoInt = []
for i in range(len(arquivo)):
  arquivoInt.append(int(arquivo[i])) 

## 2. Inclua em seu programa uma rotina que organize e exiba os 40 dados em ordem crescente (rol).
def ordenarDados(dados):
    # Ordena os dados
    dados.sort()
    return dados

## 3. Inclua em seu programa uma rotina que calcule e apresente a média dos 40 dados.
def calcularMedia(dados):
    quantidadeItens = len(dados)
    somaItens = 0
    
    for dado in dados:
        somaItens = somaItens + dado
    
    media = somaItens / quantidadeItens
    
    return media

## 4. Inclua em seu programa uma rotina que determine e exiba a mediana dos 40 dados.

dadosTeste = [8,3,4,1,2,5,3,4,7]

def calcularMediana(dados):
    dados = ordenarDados(dados)
    
    return dados
   
   
## 5. Inclua em seu programa uma rotina que verifique se existe uma (ou mais) moda(s) entre os 40 dados. Caso exista(m), o programa deve apresentá-la(s). 
"""
6. Inclua em seu programa uma rotina que calcule e apresente o desvio absoluto médio dos 40 dados.
7. Inclua em seu programa uma rotina que calcule e apresente a variância e o desvio padrão dos 40 dados.
Obs.: como estamos lidando com mais de 30 dados, não é necessário usar a correção (n-1) no cálculo da variância.

8. Inclua em seu programa uma rotina que agrupe os 40 dados em 7 classes (sugestão óbvia: classes de 0 a 10, 10 a
20, 20 a 30 e assim por diante) e apresente a distribuição de frequências destas classes. Esta tabela de distribuição
de frequências deve ter colunas para as classes, ponto médio de cada classe (xi), frequências absolutas (ni),
frequências relativas (ou proporções, fi) e porcentagens (%, obtidas como 100*fi).

9. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima,
apresente um histograma da distribuição. Caso a apresentação de um histograma seja muito difícil na linguagem
de programação com a qual você esteja trabalhando, tente apresentar ao menos um diagrama de ramos-e-folhas
dos dados, ou um gráfico de dispersão unidimensional (aquele dos pontinhos).

10. Inclua em seu programa uma rotina que calcule a média usando os dados agrupados em classes (item 8. acima).
Verifique se há alguma diferença entre esta média e aquela calculada no item 3. acima. Caso haja alguma
diferença, explique por que isso ocorre.

11. Inclua em seu programa uma rotina que determine a(s) classe(s) modal(is) da distribuição de frequências
construída no item 8. acima.

12. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima, calcule
e apresente o desvio absoluto médio. Verifique se há alguma diferença entre este desvio absoluto médio e aquele
calculado no item 6. acima. Caso haja alguma diferença, explique por que isso ocorre.

13. Inclua em seu programa uma rotina que, baseada na distribuição de frequências montada no item 8. acima, calcule
e apresente a variância e o desvio padrão. Verifique se há alguma diferença entre a variância e o desvio padrão
assim calculados e aqueles calculados no item 7. acima. Caso haja alguma diferença, explique por que isso ocorre.
Obs.: como estamos lidando com mais de 30 dados, não é necessário usar a correção (n-1) no cálculo da variância.
"""

    
