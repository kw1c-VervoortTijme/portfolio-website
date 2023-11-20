//  Auteur:         Tijme Vervoort
// Aanmaakdatum:    23-1-2023

// hier vul ik mijn cijfers in om het gemiddelde te berekenen
var subjects = [
  "Realiseren",
  "Computervaardigheden",
  "Plannen en Ontwerpen",
  "Testen en verbeteren",
];

var gradesREA = [9.5, 4.8, 5.9];
var gradesCOM = [8.6, 7.6, 8.7];
var gradesPO = [8.7, 6.7, 6.7];
var gradesTV = [10, 4.4, 4.4];

var table = "";

// hier word de som gemaakt
function CreateTable(gradesArray, subjectArray) {
  table += "<tr>";
  table += "<th>" + subjects[subjectArray] + "</th>";
  for (var i = 0; i < gradesArray.length; i++) {
    table += "<td>" + gradesArray[i] + "</td>";
  }
  var total = 0;
  for (i = 0; i < gradesArray.length; i++) {
    total += gradesArray[i];
  }
  var avarage = total / gradesArray.length;

  table += "<td>" + Math.round(avarage * 10) / 10;
  +"</td>";
  table += "</tr>";
  return table;
}

// hier onderscheid hij de vakken
CreateTable(gradesREA, 0);
CreateTable(gradesCOM, 1);
CreateTable(gradesPO, 2);
CreateTable(gradesTV, 3);
document.getElementById("tbody").innerHTML = table;
