function gerarTabuada() {
    //Pega o valor do input do html
    const numeroImput = document.getElementById(`numeroImput`)
    let numero = parseInt(numeroImput.value)

    //Mostra o resultado opnde a tabela deve ser exibida

    const resultadoDiv = document.getElementById(`resultadoTabuada`)
    resultadoDiv.innerHTML= ` `

    //Add um titulo para tabuada

    resultadoDiv.innerHTML += `<h2>Tabuada do número ${numero}</h2>`

    //Laço de repetição para tabuada

    for (let i = 1; i<=10; i++){
        let resultado = numero * i
        //Adiciona cada linha da tabuada como um paragráfo
        resultadoDiv.innerHTML += `<p>${numero} x ${i} - ${resultado}</p>`
    }
}

//A função gerar tabuada será executada quando clicar no botão
const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', gerarTabuada)