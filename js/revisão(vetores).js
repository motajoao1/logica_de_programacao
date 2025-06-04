//Criando um vetor 
const listadEnUMEROS = [1,2,3,4]

console.log('Listando todos os numeros da lista')
console.log(listadEnUMEROS)

console.log('\nMultiplicando valores por 2: ')
const dobrados = listadEnUMEROS.map(n=>n*2)
console.log(dobrados)

console.log('\nFiltrando elementos pares: ')
const pares = listadEnUMEROS.filter(n=>n%2===0)
console.log(pares)

console.log('\nSomando todos os numeros da lista: ')
const soma = listadEnUMEROS.reduce((soma,total) => soma + total, 0)
console.log(soma)
