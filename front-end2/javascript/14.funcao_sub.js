//Criando uma função

function somar(a,b) {
    return a+b
}

function subtrair(a,b){
    return a - b
}

//Chamando uma função
//Adicionar resultado da função na constante
const soma = somar (2,3)
const subtracao = subtrair (2,3)

// Mostra o conteudo da constante
console.log(`Soma: ${soma}`)
console.log(`Subtração: ${subtracao}`)