let apiUrl = null;

export const getApiUrl = async () => {
    if (apiUrl) return apiUrl;

    try {
        // Try to get the API URL from the environment variable first
        const envApiUrl = process.env.REACT_APP_API_URL;
        if (envApiUrl) {
            apiUrl = envApiUrl;
            return apiUrl;
        }

        // If no environment variable, try to detect the backend server
        const response = await fetch('http://localhost:8000/');
        const data = await response.json();
        apiUrl = data.server_url;
        return apiUrl;
    } catch (error) {
        console.error('Failed to detect API URL:', error);
        // Fallback to default if detection fails
        apiUrl = 'http://localhost:8000';
        return apiUrl;
    }
}; 