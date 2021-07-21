import pandas as pd
from datetime import date

#https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

#Código da tabela no SGS - Sistema Gerenciador de Séries Temporais
codSerie = '1'

dataInicial = '01/01/1997'
dataFinal = date.today().strftime('%d/%m/%Y')

url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codSerie,dataInicial,dataFinal)

df = pd.read_json(url)
df.set_index('data', inplace=True)

#Exporta a consulta em arquivo csv
df.to_csv('PreçoDólar.csv', sep=';')