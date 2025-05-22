//digite no terminal o comando abaxio
// npm install readline-sync

const readlineSync = require('readline-sync')

let numero = parseInt(readlineSync.question("Digite um número para a tabela"))

console.log('Tabela do número ${número}:')

for (let i=1;i<=10;i++){
    let resultado = numero * 1;
    console.log(`${numero} x ${i} = ${resultado}`)
}