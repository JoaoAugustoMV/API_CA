# API_CA
API simples para consultar de forma rápida o CA(Certificado de Aprovação), dado pelo Ministério do Trabalho brasileiro de um EPI(Equipamento de Proteção Individual)

# Stack

- Python
<<<<<<< HEAD
  - BeautifulSoup: Para Web Scrapping da pagina https://meuca.com.br/
  - Flask: Para aplicação Web
  
 
 # Consumir
 
- https://caapiepi.herokuapp.com/api/ca/:NumeroCAPretendido
=======
  - BeautifulSoup: Lib para Web Scrapping da pagina https://consultaca.com/
  - Flask: Lib para Aplicação Web
  
<<<<<<< HEAD
        "Aprovadopara":"string",
        "CA":"string",
        "Cor":"string",
        "DatadeValidade":"string",
        "DescriçãoEquipamento": "string",
        "Equipamento": "string",
        "Natureza": "string",
        "Observação": "string.",
        "RazãoSocial": "string ",
        "Referência": "string",
        "Restrição": "string ",
        "Situação": "string",
        "Tamanho": "string"
      }
      ```
  - OBS: Nem todos EPI possuem o campo Tamanho
=======
        "Aprovadopara":"string", - Situação ou ambiente adequado para o EPI
        "CA":"string", - Numero do CA
        "Cor":"string", 
        "DatadeValidade":"string",
        "DescriçãoEquipamento": "string", 
        "Equipamento": "string", - Nome do equipamento
        "Marcacao": "string", - Onde no EPI está escrito o CA
        "Natureza": "string", - Nacional ou Importado
        "Observação": "string.",
        "RazãoSocial": "string ", - Empresa fabricante ou importadora
        "Referência": "string",
        "Restrição": "string ", - Onde não pode ser usado
        "Situação": "string", - Aprovado ou Vencido
        "Tamanho": "string"
      }
      ```
  - OBS: Nem todos EPI possuem todos os campos
  - OBS2: As informações são retiradas do site https://consultaca.com/ atraves de Webscrapping, pois não há (pelo menos não achei) nenhuma fonte de dados oficiais do governo brasileiro, além do site http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx, que é extremamente lento, o que tornaria a API pouco eficaz

>>>>>>> e6d21ddf038cc30040fbf09e4a36492576f856ca
