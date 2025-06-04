const readline = require('readline-sync');

const listadEnUMEROS = [];

for (let i = 1; i <= 6; i++) {
    let numero = readline.questionFloat("Digite um número: ");
    listadEnUMEROS.push(numero);
}

console.log('\nFiltrando elementos pares:');
const pares = listadEnUMEROS.filter(numero => numero % 2 === 0);
console.log(pares);


console.log('\nFiltrando elementos ímpares:');
const impares = listadEnUMEROS.filter(numero => numero % 2 !== 0);
console.log(impares);
