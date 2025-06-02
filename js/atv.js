// Leitura dos valores (simulando entrada do usuário com prompt)

const readline = require('readline-sync')

let A = readline.questionFloat("Digite o valor de A:");
let B = readline.questionFloat("Digite o valor de B:");

let C;

if (A === B) {
  C = A + B;
} else {
  C = A * B;
}

console.log("O valor de C é:", C);
