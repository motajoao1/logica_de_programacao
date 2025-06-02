const readline = require('readline-sync');

let numero = readline.questionFloat("Digite um número: ");
let resultado = verificarNumero(numero);
console.log(resultado);

function verificarNumero(numero) {
  if (numero > 0) {
    return "O número é positivo.";
  } else if (numero < 0) {
    return "O número é negativo.";
  } else {
    return "O número é zero.";
  }
}
