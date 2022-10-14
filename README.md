# API_CA
API Rest para consulta de CA (Certificado de Aprovação) de um EPI (Equipamento de Proteção Individual), necessário para a venda e utilização de EPI's, dado pelo Ministerio do Trabalho

# Stack

- Python
  - BeautifulSoup: Lib para Web Scrapping da pagina https://consultaca.com/
  - Flask: Lib para Aplicação Web
  
- Google Cloud: Hospedagem
 
 # Consumir
 
- https://projeto-ca-api.rj.r.appspot.com//api/ca/{NumeroCAPretendido}
  - Basta inserir o número do CA do EPI escolhido no lugar de **NumeroCAPretendido**
  - Será retornado um **JSON**, com a seguinte estrutura:
    ```json
    {
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
  - OBS2: As informações são retiradas do site https://consultaca.com/, pois não há (pelo menos não achei) nenhuma fonte de dados oficiais do governo brasileiro, além do site http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx, que é extremamente lento, o que tornaria a API pouco eficaz

