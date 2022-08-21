# pip install beautifulsoup4
#
import requests
from bs4 import BeautifulSoup
import bs4


class EPI:
  ca = ''
  linhasTabela = []
  epiJSON = {}

  def __init__(self,  ca):
    self.ca = ca

  def receberLinhasTabela(self): # Web Scrapping da Tabela com os dados do EPI
    url = f'https://meuca.com.br/{self.ca}'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.table
    self.linhasTabela = table.find_all('tr')

    return self.linhasTabela

  def receberEPI(self):
    self.receberLinhasTabela()
    for linha in self.linhasTabela:
        if (linha.td):
          nomeCampo = linha.th.getText().replace(' ', '')
          dadoCampo = linha.td.div.getText()
          if(nomeCampo == 'CA'):
            dadoCampo = dadoCampo[:5]
          elif(nomeCampo == 'Situação'):
            dadoCampo = dadoCampo.split(' ')[0]
          self.epiJSON[nomeCampo] = dadoCampo
    return self.epiJSON
## end EPI
