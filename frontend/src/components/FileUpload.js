import React, { useState } from "react";
import { uploadPDF } from "../api/api";

const FileUpload = ({ setPdfPath }) => {
    const [file, setFile] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await uploadPDF(file);
            setPdfPath(response.data.path);
        } catch (error) {
            console.error("Error uploading PDF:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button type="submit">Upload PDF</button>
        </form>
    );
};

export default FileUpload;
