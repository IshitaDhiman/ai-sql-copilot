import { useState } from "react";

function SQLInput({ onSubmit }) {

    const [question, setQuestion] = useState("");

    return (
        <div>

            <textarea
                rows={4}
                placeholder="Ask anything about your banking database..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <br />

            <button
                onClick={() => onSubmit(question)}
            >
                Generate SQL
            </button>

        </div>
    );
}

export default SQLInput;