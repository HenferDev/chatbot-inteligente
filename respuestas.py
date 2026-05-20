import random

def responder(mensaje):

    mensaje = mensaje.lower()

    saludos = [
        "¡Hola! ☕ Bienvenido a Don Nicolás Coffee Shop.",
        "Hola 👋 ¿En qué podemos ayudarte hoy?",
        "¡Qué gusto verte en Don Nicolás Coffee Shop ☕!"
    ]

    despedidas = [
        "¡Gracias por visitarnos ☕!",
        "Esperamos verte pronto en Don Nicolás Coffee Shop 👋",
        "¡Que tengas un excelente día!"
    ]

    recomendaciones = [
        "Te recomendamos nuestro Cappuccino de especialidad ☕",
        "Nuestro Cold Brew Berries es uno de los favoritos 🫐",
        "El Cold Brew artesanal es perfecto si deseas algo refrescante 😎"
        ""
    ]

    if any(palabra in mensaje for palabra in ['hola', 'buenas', 'hey', 'buen', 'buenos']):
        return random.choice(saludos)

    elif 'menu' in mensaje or 'menú' in mensaje:

        return """
☕ MENÚ DON NICOLÁS

• Espresso
• Cortado 
• Cappuccino
• Latte
• Mocca
• Cold Brew
• Iced Nikko Latte
"""

    elif  "horario" in mensaje or "abren" in mensaje or "abierto" in mensaje:

        return " Nuestro horario es de 7 AM a 9 PM. ¡Será un gusto atenderte."

    elif "ubicacion" in mensaje or "ubicación" in mensaje or "donde" in mensaje or "ubicados" in mensaje:

        return "📍 Estamos ubicados en el centro histórico de Esquipulas, en 1. Calle 3-01, será un gusto atenderte."

    elif "instagram" in mensaje or "redes" in mensaje:

        return "📸 Síguenos en Instagram: @donnicolascoffeeshop"

    elif "recomendacion" in mensaje or "recomiendame" in mensaje or "recomiéndame" in mensaje or "recomiendas" in mensaje  or "recomienda" in mensaje or "otra"  in mensaje:

        return random.choice(recomendaciones)

    elif "wifi" in mensaje:

        return "📶 Sí contamos con WiFi para nuestros clientes."

    elif "gracias" in mensaje:

        return "☕ ¡Con mucho gusto!"

    elif any(palabra in mensaje for palabra in ["adios", "adiós", "bye"]):
        return random.choice(despedidas)

    else:

        return "☕ Lo siento, aún estoy aprendiendo. ¿Puedes escribir tu consulta de otra manera?"