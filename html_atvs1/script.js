const containerEntradas = document.getElementById('entradasDeNotas');
const numeroDeUsuarios = 4;

// Cria os campos de entrada para cada usuário
for (let i = 1; i <= numeroDeUsuarios; i++) {
    const div = document.createElement('div');
    div.classList.add('input-group');

    const label = document.createElement('label');
    label.setAttribute('for', 'nota' + i);
    label.textContent = `Nota do Usuário ${i}:`;

    const input = document.createElement('input');
    input.type = 'number';
    input.id = 'nota' + i;
    input.placeholder = 'Digite a nota';
    input.required = true;

    div.appendChild(label);
    div.appendChild(input);
    containerEntradas.appendChild(div);
}

function calcularMedia() {
    let soma = 0;
    let notasValidas = 0;
    const saida = document.getElementById('resultado');

    for (let i = 1; i <= numeroDeUsuarios; i++) {
        const inputNota = document.getElementById('nota' + i);
        const nota = parseFloat(inputNota.value);

        if (!isNaN(nota)) {
            soma += nota;
            notasValidas++;
        } else {
            saida.textContent = `Por favor, insira um valor válido para a Nota do Usuário ${i}.`;
            saida.style.color = 'red';
            return;
        }
    }

    const media = soma / notasValidas;
    saida.style.color = '#333';
    saida.textContent = `A média das notas é: ${media.toFixed(2)}`;
}
