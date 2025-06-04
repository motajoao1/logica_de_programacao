const readline = require('readline-sync');

const listadEnUMEROS = [];

for (let i = 1; i <= 6; i++) {
    let numero = readline.questionFloat(`Digite um número: `);
    listadEnUMEROS.push(numero);
}

const pares = listadEnUMEROS.filter(n => n % 2 === 0);
const impares = listadEnUMEROS.filter(n => n % 2 !== 0);

console.log(`\nQuantidade de pares: ${pares.length}`);
console.log(`Quantidade de impares: ${impares.length}`);
