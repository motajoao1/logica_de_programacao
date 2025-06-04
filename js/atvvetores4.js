const readline = require('readline-sync');

const listadEnUMEROS = [];

for (let i = 1; i <= 5; i++) {
    let numero = readline.questionFloat(`Digite um número: `);
    listadEnUMEROS.push(numero);
}

const negativo = listadEnUMEROS.filter(n => n < 0);
const positivos = listadEnUMEROS.filter(n => n >= 0).reduce((soma, total) => soma + total,  0)
//const somaPositivos = positivos.reduce((soma, total) => soma + total, 0);

console.log(`\nQuantidade de negativos: ${negativo.length}`);
console.log(`Soma de positivos: ${positivos}`);

