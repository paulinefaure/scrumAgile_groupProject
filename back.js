const SS = SpreadsheetApp.getActiveSpreadsheet();
//https://script.google.com/macros/s/AKfycbycYSGtKd4ZsbFg1RX5AKAc3BcUjxYUJ6qoakPyVuWKLQknT2-hKm3gc0qBV6Ko5RZv/exec

function doGet() {
  return HtmlService.createHtmlOutputFromFile('Main.html');
}
function newPage(page) {
  return HtmlService.createHtmlOutputFromFile(page).getContent()
}

function getLogin() {
  let values = SS.getSheetByName('Login').getRange('A2:C20').getValues().filter(pair => pair[0] != '' && pair[1]!='')
  return(values) 
}

function addUser(user) {
  let values = SS.getSheetByName('Login').getRange('A2:C').getValues().filter(elem => elem[0] != '' && elem[1] != '')
  values.push(user)
  SS.getSheetByName('Login').getRange('A2:C' + (values.length + 1)).setValues(values)
}

function checkLoginValidity(values) {
  let login = getLogin()
  let value = login.filter(pair => pair[0] == values[0] && pair[1] == values[1])
  return([value.length, value])
}

function findFunction() {
  console.log('here => ',USER)
  return(USER[0])
}

function getInfo(page) {
  let values = SS.getSheetByName(page).getRange('A2:F20').getValues().filter(pair => pair[0] != '' && pair[1]!='')
  return values
}

function addInfos(page, info) {
  if (page != 'Customer')
    info.push('')
  let data = getInfo(page)
  data.push(info)
  console.log(data)
  SS.getSheetByName(page).getRange('A2:F'+ (data.length + 1)).setValues(data)
  

}
