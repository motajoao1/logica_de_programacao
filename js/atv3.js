const readline = require('readline-sync');

let A = readline.questionInt("Digite o número do dia da semana (1 a 7):");

if (A == 1) {
  A = "domingo";
  console.log("O final de semana é:", A);
} else if (A == 2) {
  A = "segunda";
  console.log("O dia útil da semana é:", A);
} else if (A == 3) {
  A = "terça";
  console.log("O dia útil da semana é:", A);
} else if (A == 4) {
  A = "quarta";
  console.log("O dia útil da semana é:", A);
} else if (A == 5) {
  A = "quinta";
  console.log("O dia útil da semana é:", A);
} else if (A == 6) {
  A = "sexta";
  console.log("O dia útil da semana é:", A);
} else if (A == 7) {
  A = "sábado";
  console.log("O final de semana é:", A);
} else {
  console.log("Inválido");
}
