const resultados = document.getElementById('resultados');

async function logJSONData() {
    const response = await fetch('http://127.0.0.1:5000/');
    const jsonData = await response.json();

    for (var i = 0; i < jsonData.data.length; i++) {
        console.log(jsonData.data[i]);
        const tr = document.createElement('tr');
        const id = document.createElement('td');
        const endereco = document.createElement('td');
        const resultado = document.createElement('td');
        const parceiro = document.createElement('td');

        resultados.appendChild(tr);
        tr.appendChild(id);
        tr.appendChild(endereco);
        tr.appendChild(resultado);
        tr.appendChild(parceiro);

        id.textContent = jsonData.data[i].id
        endereco.textContent = jsonData.data[i].endereco
        resultado.textContent = jsonData.data[i].resultado
        parceiro.textContent = jsonData.data[i].nome_parceiro

        id.scope = 'row';
    }
}
logJSONData()