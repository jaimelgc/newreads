import axios from "axios";

const publicApi = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

export default publicApi;