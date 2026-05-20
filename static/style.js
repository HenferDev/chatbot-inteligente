async function enviarMensaje(){

    let mensaje = document.getElementById('mensaje').value;

    let chat = document.getElementById('chat');

    chat.innerHTML += `<p><b>Tú:</b> ${mensaje}</p>`;

    let respuesta = await fetch('/chat', {

        method: 'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body: JSON.stringify({
            mensaje: mensaje
        })

    });

    let datos = await respuesta.json();

    chat.innerHTML += `<p><b>Bot:</b> ${datos.respuesta}</p>`;

    document.getElementById('mensaje').value = '';
}


