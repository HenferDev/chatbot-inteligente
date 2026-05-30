from datetime import datetime
import random

def responder(mensaje):

    mensaje = mensaje.lower().strip()

    recomendaciones = [
        "Te recomendamos nuestro Cappuccino, es una de las bebidas favoritas de nuestros clientes.",
        "Si buscas algo refrescante, puedes probar nuestro Cold Brew.",
        "Nuestro Latte es una excelente opción si prefieres un café suave y equilibrado.",
        "El Mocca combina perfectamente el sabor del café con el chocolate.",
        "El Iced Nikko Latte es una bebida muy popular durante los días calurosos."
    ]

    despedidas = [
        "Gracias por visitarnos. Esperamos atenderte pronto.",
        "Será un gusto recibirte nuevamente en Don Nicolás Coffee Shop.",
        "Que tengas un excelente día."
    ]

    # SALUDOS

    if any(palabra in mensaje for palabra in [
        "hola",
        "buenas",
        "hey",
        "saludos"
    ]):

        hora = datetime.now().hour

        if hora < 12:
            saludo = "Buenos días."
        elif hora < 18:
            saludo = "Buenas tardes."
        else:
            saludo = "Buenas noches."

        return f"{saludo} Bienvenido a Don Nicolás Coffee Shop. Puedo ayudarte con información sobre menú, horarios, ubicación, recomendaciones y contacto."

    # MENÚ

    elif any(palabra in mensaje for palabra in [
        "menu",
        "menú",
        "bebidas",
        "comida",
        "comidas",
        "productos",
        "que venden",
        "qué venden"
    ]):

        return """
Puedes consultar nuestro menú completo aquí:

<a href="/static/Menu.pdf" target="_blank">Ver menú</a>
"""

    # HORARIOS

    elif any(palabra in mensaje for palabra in [
        "horario",
        "horarios",
        "abren",
        "abierto",
        "cierran"
    ]):

        return "Nuestro horario de atención es de lunes a domingo de 7:00 AM a 9:00 PM."

    # UBICACIÓN

    elif any(palabra in mensaje for palabra in [
        "ubicacion",
        "ubicación",
        "donde",
        "dónde",
        "ubicados"
    ]):

        return "Estamos ubicados en 1 Calle 3-01, Centro Histórico de Esquipulas."

    # PRECIOS

    elif any(palabra in mensaje for palabra in [
        "precio",
        "precios",
        "cuanto cuesta",
        "cuánto cuesta",
        "coste"
    ]):

        return "Contamos con diferentes precios según la bebida. Puedes consultarlos directamente en nuestra cafetería o mediante WhatsApp."

    # INSTAGRAM

    elif "instagram" in mensaje:

        return "Puedes encontrarnos en Instagram como @donnicolascoffeeshop."

    # FACEBOOK

    elif "facebook" in mensaje:

        return "Puedes encontrarnos en Facebook como Don Nicolás Coffee Shop."

    # WHATSAPP / CONTACTO

    elif any(palabra in mensaje for palabra in [
        "whatsapp",
        "numero",
        "número",
        "telefono",
        "teléfono",
        "contacto",
        "celular"
    ]):

        return "Puedes comunicarte con nosotros mediante WhatsApp al número +502 5433-2402 o utilizando el botón disponible en esta página."

    # WIFI

    elif "wifi" in mensaje:

        return "Sí, contamos con servicio de WiFi para nuestros clientes."

    # RECOMENDACIONES

    elif any(palabra in mensaje for palabra in [
        "recomendacion",
        "recomendación",
        "recomiendame",
        "recomiéndame",
        "recomienda",
        "recomiendas",
        "que tomo",
        "qué tomo",
        "algo para tomar",
        "recomendarme"
    ]):

        return random.choice(recomendaciones)

    # INTENCIÓN DE COMPRA

    elif any(palabra in mensaje for palabra in [
        "comprar",
        "pedido",
        "pedir",
        "ordenar",
        "orden",
        "quiero un",
        "quiero una",
        "me vende",
        "vender"
    ]):

        return "Gracias por tu interés. Actualmente este chatbot funciona como asistente informativo. Para realizar pedidos o recibir atención personalizada puedes comunicarte mediante nuestro WhatsApp."

    # CAFÉ

    elif "cafe" in mensaje or "café" in mensaje:

        return "Nos especializamos en bebidas a base de café preparadas cuidadosamente para brindar una experiencia única a nuestros clientes."

    # QUIÉN ERES

    elif "quien eres" in mensaje or "quién eres" in mensaje:

        return "Soy el asistente virtual de Don Nicolás Coffee Shop. Estoy aquí para ayudarte con información sobre nuestros productos y servicios."

    # GRACIAS

    elif any(palabra in mensaje for palabra in [
        "gracias",
        "muchas gracias",
        "te agradezco"
    ]):

        return "Con mucho gusto. Estoy para ayudarte."

    # DESPEDIDAS

    elif any(palabra in mensaje for palabra in [
        "adios",
        "adiós",
        "bye",
        "hasta luego",
        "nos vemos",
        "chao",
        "chau"
    ]):

        return random.choice(despedidas)

    # RESPUESTA POR DEFECTO

    else:

        return "No logré comprender tu consulta. Puedes preguntarme sobre menú, horarios, ubicación, recomendaciones, redes sociales o WhatsApp."