# API_CA
API simples para consultar de forma rápida o CA(Certificado de Aprovação), dado pelo Ministério do Trabalho brasileiro de um EPI(Equipamento de Proteção Individual)

# Stack

- Python
  - BeautifulSoup: Para Web Scrapping da pagina https://meuca.com.br/
  - Flask: Para aplicação Web
  
 - Heroku: Hospedagem
 
 # Consumir
 
- https://caapiepi.herokuapp.com/api/ca/:NumeroCAPretendido
  - Basta inserir o número do CA do EPI escolhido no lugar de **NumeroCAPretendido**
  - Será retornado um **JSON**, com a seguinte estrutura:
    ```json
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
  - OBS: Nem todos EPI possuem o campo Tamanho
