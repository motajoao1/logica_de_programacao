const readline = require('readline-sync');

let a = readline.questionFloat("Digite um número: ");
let b = readline.questionFloat("Digite um número: ");
let c = readline.questionFloat("Digite um número: ");
const listadEnUMEROS = [a, b, c];

console.log('Listando todos os numeros da lista');
console.log(listadEnUMEROS);

console.log('\nSomando todos os numeros da lista e dando a média:');
const soma = a + b + c;
const media = soma / listadEnUMEROS.length;
console.log(media);