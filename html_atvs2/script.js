function calcularMedia() {
    const nota1 = parseFloat(document.getElementById("nota1").value);
    const nota2 = parseFloat(document.getElementById("nota2").value);
    const nota3 = parseFloat(document.getElementById("nota3").value);
    const resultadoDiv = document.getElementById("resultado");

    // Verificar se as notas são números válidos
    if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3)) {
        resultadoDiv.textContent = "Por favor, insira notas válidas.";
        return;
    }

    const media = (nota1 + nota2 + nota3) / 3;
    let situacao;
    let classeSituacao;

    if (media >= 7) {
        situacao = "Aprovado";
        classeSituacao = "aprovado";
    } else if (media >= 4) {
        situacao = "Em Recuperação";
        classeSituacao = "recuperacao";
    } else {
        situacao = "Reprovado";
        classeSituacao = "reprovado";
    }

    resultadoDiv.innerHTML = `Média: ${media.toFixed(2)}<br>Situação: <span class="${classeSituacao}">${situacao}</span>`;
}