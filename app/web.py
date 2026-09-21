from fastapi.responses import HTMLResponse


def get_chat_page():
    return HTMLResponse(
        content="""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistics AI Tutor</title>

    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            background-color: #f5f7fa;
        }

        .chat-container {
            max-width: 800px;
            margin: 40px auto;
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        h1 {
            margin-top: 0;
        }

        .subtitle {
            color: #6b7280;
            margin-top: -8px;
            margin-bottom: 24px;
            font-size: 15px;
        }

        #chat {
            margin-bottom: 25px;
            line-height: 1.5;
            min-height: 80px;
            max-height: 500px;
            overflow-y: auto;
        }

        .user-message {
            background-color: #2563eb;
            color: white;
            max-width: 70%;
            width: fit-content;
            margin-left: auto;
            padding: 10px 14px;
            border-radius: 12px;
            margin-top: 18px;
            max-height: 200px;
            overflow-y: auto;
        }

        .tutor-message {
            background-color: #f3f4f6;
            padding: 10px 14px;
            border-radius: 12px;
            margin-top: 10px;
        }

        .sources-message {
            margin-top: 6px;
            padding-left: 14px;
            font-size: 13px;
            color: #6b7280;
        }

        .loading-message {
        
            display: inline-block;
        }
        
        .loading-dots::after {
            content: " ...";
            animation: loadingDots 1.2s infinite;
        }

        @keyframes loadingDots {
            0% { content: ""; }
            33% { content: "."; }
            66% { content: ".."; }
            100% { content: "..."; }
        }

        .welcome-message {
            background-color: #f3f4f6;
            padding: 14px 16px;
            border-radius: 12px;
            width: fit-content;
        }

        .welcome-message p {
            margin: 6px 0 0;
        }

        .input-area {
            display: flex;
            gap: 8px;
            align-items: flex-end;
        }

        #question {
            flex: 1;
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            resize: none;
            max-height: 150px;
        }

        button {
            padding: 12px 18px;
            background-color: #2563eb;
            border-radius: 8px;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #1d4ed8;
            
        }

        button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

    </style>

    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['\\(', '\\)']],
                displayMath: [['\\[', '\\]']]
            }
        };
    </script>

    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body>
    <div class="chat-container">
        <h1>Statistics AI Tutor</h1>
        <p class="subtitle">
            Tutor académico de Estadística basado en los materiales de tu curso
        </p>

        <div id="chat">
            <div class="welcome-message">
                <strong>¡Hola! 👋</strong>
                <p>Puedes preguntarme sobre los temas disponibles en los materiales del curso.</p>
            </div>
        </div>

        <div class="input-area">
            <textarea
                id="question"
                placeholder="Escribe tu pregunta aquí"
                rows="1"
                oninput="autoResize(this)"
                onkeydown="if(event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); askQuestion(); }"
            ></textarea>
            <button id="ask-button" onclick="askQuestion()">Enviar</button>
        </div>
    </div>

    <script>

        function autoResize(textarea) {
            textarea.style.height = "auto";
            textarea.style.height = textarea.scrollHeight + "px";
        }

        async function askQuestion() {
            const question = document.getElementById("question").value;
            const askButton = document.getElementById("ask-button");
            const welcomeMessage = document.querySelector(".welcome-message");

            if (askButton.disabled) {
                return;
            }

            if (question.trim() === "") {
                return;
            }

            if (welcomeMessage) {
                welcomeMessage.remove();
            }

           
            askButton.disabled = true;

            const userMessage = document.createElement("div");
            userMessage.className = "user-message";
            userMessage.innerText = question;
            document.getElementById("chat").appendChild(userMessage);

            document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;

            document.getElementById("question").value = "";
            autoResize(document.getElementById("question"));

            const loadingMessage = document.createElement("div");
            loadingMessage.className = "tutor-message loading-message";
            loadingMessage.innerHTML = 'Pensando<span class="loading-dots"></span>';
            document.getElementById("chat").appendChild(loadingMessage);

            try {
                const response = await fetch("/ask", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        question: question
                    })
                });

                if (!response.ok) {
                    throw new Error("Error en la respuesta del servidor");
                }

                const data = await response.json();

                loadingMessage.remove();

                const tutorMessage = document.createElement("div");
                tutorMessage.className = "tutor-message";
                tutorMessage.innerHTML = marked.parse(data.answer);
                document.getElementById("chat").appendChild(tutorMessage);

                if (data.sources.length > 0) {
                    const sourcesMessage = document.createElement("div");
                    sourcesMessage.className = "sources-message";
                    sourcesMessage.innerText = "Fuentes: " + data.sources
                    .map(source => source.document + " — página " + source.page)
                    .join(" | ");
                    document.getElementById("chat").appendChild(sourcesMessage);
                    }
                
                document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;


                MathJax.typesetPromise([tutorMessage]);

                askButton.disabled = false;
                document.getElementById("question").focus();

            } catch (error) {
                loadingMessage.remove();
                alert("Ocurrió un error al comunicarse con el tutor.");
                askButton.disabled = false;
            }
        }
    </script>
</body>
</html>
"""
    )