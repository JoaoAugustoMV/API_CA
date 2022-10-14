function getEPI(ca){ // Retorna todas as informações do EPI
  url = 'https://projeto-ca-api.rj.r.appspot.com/api/ca/' + ca
  let resp = UrlFetchApp.fetch(url)
  
  return JSON.parse(resp)
}
function selecionarCamposEPI(ca){ // Retorna campos especificos do EPI
  let epi = getEPI(ca)
  return { 
    'Equipamento': epi['Equipamento'], // A
    'Situacao': epi['Situacao'], // D
    'DataValidade': epi['Validade'] // E
  }
  
}


function pegarCas(){ // Retorna os valores da coluna CA
  let planilha = SpreadsheetApp.getActive().getSheetByName("CA's") // Seleciona planilha CA's
  let intervalo = planilha.getRange('C:C') // Coluna com os CA's
  let coluna = intervalo.getValues() 
  listaCa = []
  for(ca of intervalo.getValues()){
    if(typeof ca[0] === 'number'){ // Se não for vazia
      listaCa.push(ca[0].toString())
    }
    
  }
  return listaCa 
}

function preencherCamposEPI(){ // Itera os ca e preenche suas informações
  let planilha = SpreadsheetApp.getActive().getSheetByName("CA's") // Seleciona planilha CA's
  let listaCa = pegarCas()
  for(caIndex in listaCa){
    let epi = selecionarCamposEPI(listaCa[caIndex])
    planilha.getRange(`A${Number(caIndex) + 2}`).setValue((epi)['Equipamento'])
    planilha.getRange(`D${Number(caIndex) + 2}`).setValue((epi)['Situacao'])
    planilha.getRange(`E${Number(caIndex) + 2}`).setValue((epi)['DataValidade'])
  

  } // end for
} // end preencherCamposEPI

