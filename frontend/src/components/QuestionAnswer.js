import React, { useState } from "react";
import { askQuestion } from "../api/api";

const QuestionAnswer = ({ pdfPath }) => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleAsk = async () => {
        try {
            const response = await askQuestion(pdfPath, question);
            setAnswer(response.data.answer);
        } catch (error) {
            console.error("Error asking question:", error);
        }
    };

    return (
        <div>
            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask a question..."
            />
            <button onClick={handleAsk}>Ask</button>
            {answer && <p>Answer: {answer}</p>}
        </div>
    );
};

export default QuestionAnswer;
