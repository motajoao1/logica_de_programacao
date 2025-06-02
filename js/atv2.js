// Leitura dos valores (simulando entrada do usuário com prompt)
const readline = require('readline-sync');

let A = readline.questionFloat("Digite o valor de A:");

let par;
let impar;

if (A % 2 === 0) {
  par = A;
  console.log("O valor é par:", par);
} else {
  impar = A;
  console.log("O valor é ímpar:", impar);
}
