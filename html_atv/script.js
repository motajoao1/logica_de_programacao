function ContagemRegressiva() {

    const numeroImput = document.getElementById(`numeroImput`)
    let numero = parseInt(numeroImput.value)


    const resultadoDiv = document.getElementById(`Contagem_Regressiva`)
    resultadoDiv.innerHTML= ` `

    resultadoDiv.innerHTML += `<h2>Contagem Regressiva de ${numero}</h2>`


    for (let i = numero; i>=1; i--){
        resultadoDiv.innerHTML += `<p>${i}</p>`
    }
}

const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', ContagemRegressiva)