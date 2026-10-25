import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const exampleQuestions = [
    "What does FT102 mean?",
    "Why can a fund transfer fail?",
    "What happens if KYC documents are expired?",
    "What happens when a fixed deposit is closed before maturity?"
  ];

  const handleAsk = async () => {
    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setAnswer("");
    setSources([]);

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      setAnswer(data.answer);
      setSources(data.sources || []);
    } catch (error) {
      setAnswer("Something went wrong while contacting the backend.");
    }

    setLoading(false);
  };

  return (
    <div className="page">
      <header className="header">
        <div>
          <h1>Banking Support Assistant</h1>
          <p>AI-powered banking knowledge assistant using RAG and a local LLM.</p>
        </div>
      </header>

      <main className="main-content">
        <section className="assistant-card">
          <h2>Ask a Banking Question</h2>

          <textarea
            rows="5"
            placeholder="Example: What does FT102 mean?"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button
            className="ask-button"
            onClick={handleAsk}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask Assistant"}
          </button>

          <div className="examples">
            <p>Try an example:</p>

            <div className="example-buttons">
              {exampleQuestions.map((example, index) => (
                <button
                  key={index}
                  className="example-button"
                  onClick={() => setQuestion(example)}
                >
                  {example}
                </button>
              ))}
            </div>
          </div>
        </section>

        {answer && (
          <section className="result-card">
            <div className="answer-header">
              <span className="status-dot"></span>
              <h2>Answer</h2>
            </div>

            <p className="answer-text">{answer}</p>

            {sources.length > 0 && (
              <div className="sources">
                <h3>Sources</h3>

                <div className="source-list">
                  {sources.map((source, index) => (
                    <span className="source-tag" key={index}>
                      {source}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </section>
        )}
      </main>

      <footer>
        AI-Powered Banking Support Assistant • React • FastAPI • Ollama
      </footer>
    </div>
  );
}

export default App;