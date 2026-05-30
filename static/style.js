async function enviarMensaje() {

    let mensaje = document.getElementById("mensaje").value.trim();

    if (mensaje === "") {
        return;
    }

    let chat = document.getElementById("chat");

    // HORA USUARIO

    const horaUsuario = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

    // MENSAJE USUARIO

    chat.innerHTML += `
        <div class="usuario">
            ${mensaje}
            <div class="hora">
                ${horaUsuario}
            </div>
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    document.getElementById("mensaje").value = "";

    // ESCRIBIENDO

    chat.innerHTML += `
        <div class="bot" id="escribiendo">
            Escribiendo...
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    await new Promise(resolve => setTimeout(resolve, 800));

    try {

        const respuesta = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                mensaje: mensaje
            })

        });

        const datos = await respuesta.json();

        // ELIMINAR "ESCRIBIENDO..."

        document.getElementById("escribiendo").remove();

        // HORA BOT

        const horaBot = new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit"
        });

        // RESPUESTA BOT

        chat.innerHTML += `
            <div class="bot">
                ${datos.respuesta}
                <div class="hora">
                    ${horaBot}
                </div>
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;

    } catch (error) {

        document.getElementById("escribiendo").remove();

        chat.innerHTML += `
            <div class="bot">
                Ocurrió un error al conectar con el servidor.
            </div>
        `;

    }

}

// ENTER

document.getElementById("mensaje")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        enviarMensaje();
    }

});

// ABRIR / CERRAR CHAT

function abrirChat() {

    let chat = document.getElementById("chatFlotante");

    if (chat.style.display === "block") {

        chat.style.display = "none";

    } else {

        chat.style.display = "block";

    }

}