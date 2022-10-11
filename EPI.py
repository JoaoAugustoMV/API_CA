# pip install beautifulsoup4

import unicodedata
import requests
from bs4 import BeautifulSoup


class EPI:

  def __init__(self, ca):
    self = self
    self.ca = ca

# Div#box_result
  def retornarBoxResult(self, ca):
    url = f'https://consultaca.com/{ca}'
    soup = BeautifulSoup(requests.get(url).content, features="html.parser") # HTML da pag
    box_result = soup.find('div',id='box_result') # Div com os dados
     # tag para guiar a raspagem
    return box_result

  def padraoString(self, string):
    return unicodedata.normalize('NFD', string).encode('ascii', 'ignore').decode('utf8')

  def retornarJSON(self):
    box_result = self.retornarBoxResult(self.ca)
    brs = box_result.find_all('br') 
    # pegarTexto = ['Situação', 'Validade', 'Razão Social', 'Razão Social Importador', 'Site', 'N° do Laudo'] # Atributo que estão dentro de outra tag 
    ignorarCampo = ["CA's"]
    json = {} # Dicionario 
    for br in brs[3:]:
      chave = br.previous.replace(':', '') 
      valor = br.nextSibling
      if(chave in ignorarCampo):
        continue
      # if(chave in pegarTexto): 
      try:
        valor = valor.getText()
      except:
        return "Erro inesperado"

      if ('Declaro' in br.previous): # Acabar com a raspagem
        break
      chave = self.padraoString(chave)
      try:
        valor = self.padraoString(valor)
      except: # Alguns
        valor = valor.getText()
        valor = self.padraoString(valor)
        if (chave == 'SituaAAo'):
          chave == 'Situacao'
      
      json[chave] = valor
    json['Equipamento'] = box_result.find('h1').getText()
    json['CA'] = self.ca
    return json
