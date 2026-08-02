import { useState } from "react";
import api from "./services/api";
import SQLInput from "./components/SQLInput";
import SQLResult from "./components/SQLResult";
import "./App.css";

function App() {

    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const askQuestion = async (question) => {

        try {

            setLoading(true);

            const response = await api.post(
                "/sql/execute",
                null,
                {
                    params: {
                        question: question
                    }
                }
            );

            setResult(response.data);

        }
        catch (err) {

            alert(err.response?.data?.detail || err.message);

        }
        finally {

            setLoading(false);

        }

    };

    return (

        <div className="app">

            <div className="container">

                <h1>AI SQL Copilot</h1>

                <p className="subtitle">
                    Ask banking questions in natural language and generate SQL instantly.
                </p>

                <SQLInput
                    onSubmit={askQuestion}
                    loading={loading}
                />

                <SQLResult
                    key={result?.generated_sql ?? ""}
                    result={result}
                    loading={loading}
                />

            </div>

        </div>

    );

}

export default App;