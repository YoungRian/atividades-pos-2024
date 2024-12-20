import { fetchData } from './apiWrapper.js';

document.getElementById('fetch-data').addEventListener('click', async () => {
    console.log('Fetch button clicked'); // Verifica se o evento de clique funciona
    const dataType = document.getElementById('data-type').value;
    console.log('Selected data type:', dataType); // Verifica o valor selecionado no dropdown
    const output = document.getElementById('output');
    output.innerHTML = 'Carregando...';

    try {
        const data = await fetchData(dataType);
        console.log('Data fetched:', data); // Verifica os dados retornados

        if (dataType === 'users') {
            output.innerHTML = data.map(user => `
                <div>
                    <h3>${user.name}</h3>
                    <p>Email: ${user.email}</p>
                    <p>Endereço: ${user.address.street}, ${user.address.city}</p>
                    <p>Empresa: ${user.company.name}</p>
                </div>
            `).join('');
        } else if (dataType === 'todos') {
            output.innerHTML = data.map(todo => `
                <div>
                    <h3>${todo.title}</h3>
                    <p>Status: ${todo.completed ? 'Concluído' : 'Pendente'}</p>
                    <p>ID do Usuário: ${todo.userId}</p>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error rendering data:', error); // Verifica erros de renderização
        output.innerHTML = error.message;
    }
});

