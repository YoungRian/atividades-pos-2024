export async function fetchData(dataType) {
    const url = `https://jsonplaceholder.typicode.com/${dataType}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Erro ao buscar dados');
        return await response.json();
    } catch (error) {
        console.error(error);
        throw new Error('Erro ao carregar os dados. Tente novamente.');
    }
}