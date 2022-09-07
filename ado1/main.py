# Importa as funções que eu fiz no outro arquivo modulo.py
import modulo

## 1. Crie um programa que leia os dados (se for difícil fazer isto de forma automática, faça que o programa permita 
## a digitação manual de cada dado).

with open('dados.csv') as f:
    arquivo = f.readlines()

# Converte os dados de String para Int
arquivo_dados = []

for i in range(len(arquivo)):
  arquivo_dados.append(int(arquivo[i]))

print("\n2) Dados ordenados:")
print(modulo.ordenar_dados(arquivo_dados))

print("\n3) Média:")
print(modulo.calcular_media(arquivo_dados))

print("\n4) Mediana:")
print(modulo.calcular_mediana(arquivo_dados))

print("\n5) Moda:")
print(modulo.calcular_moda(arquivo_dados))

print("\n6) Desvio médio absoluto:")
print(modulo.calcular_desvio_medio_absoluto(arquivo_dados))

print("\n7) Variância e desvio padrão:")
print(modulo.calcular_variancia_desvio_padrao(arquivo_dados))

print("\n8) Frequência de classes:")
distri_freq = modulo.calcular_frequencia_classes(arquivo_dados)

for linha in distri_freq:
    print(linha, distri_freq[linha])

print("\n9) Grafico De distribuição de frequência de classes:")
modulo.mostrar_grafico_distribuicao_frequencia(distri_freq)

print("\n10) Média da frequência de classes:")
print(modulo.calcular_media_frequencia(distri_freq))

print("\n11) Moda da frequência de classes:")
print(modulo.calcular_classe_modal(distri_freq))

print("\n12) Desvio médio absoluto da Frequência de classes:")
print(modulo.calcular_desvio_medio_absoluto_classes(distri_freq))

print("\n13) Variância e desvio padrão da frequência de classes:")
print(modulo.calcular_variancia_desvio_padrao_classes(distri_freq))
