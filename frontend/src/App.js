import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import QuestionAnswer from "./components/QuestionAnswer";

function App() {
    const [pdfPath, setPdfPath] = useState("");

    return (
        <div>
            <h1>PDF Question-Answer App</h1>
            {!pdfPath ? (
                <FileUpload setPdfPath={setPdfPath} />
            ) : (
                <QuestionAnswer pdfPath={pdfPath} />
            )}
        </div>
    );
}

export default App;

