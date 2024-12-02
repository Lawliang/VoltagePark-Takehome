const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function createGame () {
    try {
        const response = await fetch(`${API_BASE_URL}/api/create/`)
        const data = await response.json()
        return data;
    } catch (error) {
        console.log('Error processing create game data:', error)
    }
}

export async function fetchGame (id) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/fetch/${id}/`)
        const data = await response.json()
        return data;
    } catch (error) {
        console.log('Error processing fetching game data:', error)
    }
}

export async function processMove (id, body) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/move/${id}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
        })
        const data = await response.json()
        if (response.status === 400) {
            // Handle the specific case where the move is invalid
            console.log('Invalid move:', data.error);
        }
        return data;
    } catch (error) {
        console.log('Error processing lsat move:', error)
    }
}