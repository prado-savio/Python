# 13.04

from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Estatística com R - 13.04")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
#print(f"Instalar MatPlotLib: pip install matplotlib")
#print(f"         SeaBorn   : pip install seaborn")
#print(f"Biblioteca: Choosing color palettes")
#print(f"		https://seaborn.pydata.org/tutorial/color_palettes.html")
print(f"\n------------------------------------------------------------\n\n\n")

# Instalar o pacote 'readr' necessário para a leitura de arquivos CSV
install.packages("readr")

# Instalar o pacote 'readxl' necessário para a leitura de arquivos Excel
install.packages("readxl")

# Carregar pacotes instalados
library(readr)
library(readxl)

# Ler o arquivo CSV com a função read.csv()
dados <- read.csv("ESPORTISTAS_MOD7", sep=";")

# Visualizar os dados, muito semelhante ao Python
head(dados)


#---------------------#
#        MÉDIA        #
#---------------------#
mean(dados$Ganhos_Totais)											# $ é usado para acessar uma coluna específica em um Dataframe

# Agrupados por esporte
aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = mean)		# aggregate refere-se ao groupby
																	# ~ especifica que queremos agrupar os dados por Esporte e calcular a média dos ganhos totais para cada grupo
																	# FUN = mean, especifica que queremos calcular a média dos valores em cada grupo



#---------------------#
#      MEDIANA        #
#---------------------#
median(dados$Ganhos_Totais)

aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = median)



#---------------------#
#         MODA        #
#---------------------#
calcular_moda <- function(x) {
	unique_x <- unique(x)											# obter os valores únicos do vetor
	contagem <- tabulate(match(x, unique_x))						# contar a frequencia de cada valor
	moda <- unique_x[which.max(contagem)]							# encontrar o índice do valor com a frequência máxima
	return(moda)
}
calcular_moda(dados$Ganhos_Totais)



#---------------------#
#   DESVIO PADRÃO     #
#---------------------#
aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = sd)




print('\n\n\n----- Fim de execução -----\n')
