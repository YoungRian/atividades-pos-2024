document.getElementById('fetch-data').addEventListener('click', async () => {
    const dataType = document.getElementById('data-type').value;
    const output = document.getElementById('output');
    output.innerHTML = 'Carregando...';

    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/${dataType}`);
        if (!response.ok) throw new Error('Erro ao buscar dados');
        const data = await response.json();
        
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
        output.innerHTML = 'Erro ao carregar os dados. Tente novamente.';
        console.error(error);
    }
});
