# API_CA
API simples para consultar de forma rápida o CA(Certificado de Aprovação), dado pelo Ministério do Trabalho brasileiro de um EPI(Equipamento de Proteção Individual)

# Stack

- Python
  - BeautifulSoup: Para Web Scrapping da pagina https://consultaca.com/
  - Flask: Para aplicação Web
- Google Cloud
   - App Engine: Hospedagem da aplicação Web
  
 
 # Consumir
 
- https://caapiepi.herokuapp.com/api/ca/:NumeroCAPretendido
```
      {
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
  - OBS: Nem todos EPI possuem todos os campos
  - OBS2: As informações são retiradas do site https://consultaca.com/, pois não há (pelo menos não achei) nenhuma fonte de dados oficiais do governo brasileiro, além do site http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx, que é extremamente lento, o que tornaria a API pouco eficaz


