import axios from "axios";

const API_URL = "http://localhost:8000";

export const uploadPDF = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    return axios.post(`${API_URL}/pdf/upload`, formData);
};

export const askQuestion = async (pdfPath, question) => {
    return axios.post(`${API_URL}/qa/ask`, { pdf_path: pdfPath, question });
};
