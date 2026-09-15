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
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f5f7fa;
            
        }
    </style>

</head>
<body>

<h1>Statistics AI Tutor</h1>

<input id="question" type="text" placeholder="Escribe tu pregunta aquí" onkeydown="if(event.key === 'Enter') askQuestion()">
<button onclick="askQuestion()">Preguntar</button>

<div id="chat"></div>

<script>
async function askQuestion() {
    const question = document.getElementById("question").value;

    if (question.trim() === "") {
        return;
    }

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();

    document.getElementById("chat").innerText += "Tú: " + question + "\\n";
    document.getElementById("chat").innerText += "Tutor: " + data.answer + "\\n\\n";

    document.getElementById("question").value = "";
}
</script>

</body>
</html>
"""
    )