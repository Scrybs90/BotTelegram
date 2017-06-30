# -*- coding: utf-8 -*-
# Importamos las librerias necesarias
from telegram.ext import *
#from telegram.ext import Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
#from telegram import InlineQueryResultArticle, InputTextMessageContent
# Esta libreria no es estrictamente necesaria, pero es util para generar números aleatorios
# que necesitamos al generar el id del inline
from random import getrandbits


# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text

    print("ID: " + str(id) + " MENSAJE: " + mensaje)


# Método que utilizaremos para cuando se mande el comando de "start"
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Bienvenido al bot de Bytelix!')


# Método que mandará el mensaje "¡Hola, lector de Bytelix!"
def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola, lector de Bytelix!')


# Método que mandará el logo de la página
def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Icono.png', 'rb'))


# Método que responderá a las peticiones inline
def inline(bot, update):
    # Sólo procesaremos el inline cuando haya algún texto introducido
    query = update.inline_query.query

    if not query:
        return

    texto_inline = query
    resultados = list()

    # Texto que se enviará y se mostrará al usuario
    alternativa1_texto = 'Hola desde el bot de Bytelix, ' + texto_inline
    alternativa2_texto = 'Bienvenido, ' + texto_inline
    alternativa3_texto = '¿Conoces Bytelix, ' + texto_inline + '?'

    # Resultados que se mostrarán para elegir
    alternativa1 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa1_texto,
        input_message_content=InputTextMessageContent(alternativa1_texto))

    alternativa2 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa2_texto,
        input_message_content=InputTextMessageContent(alternativa2_texto))

    alternativa3 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa3_texto,
        input_message_content=InputTextMessageContent(alternativa3_texto))

    # Añadimos los resultados que hemos creado a la lista de resultados
    resultados.append(alternativa1)
    resultados.append(alternativa2)
    resultados.append(alternativa3)

    # Y mostramos la lista al usuario
    bot.answerInlineQuery(update.inline_query.id, results=resultados)


def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    # Por supuesto no os olvidéis de cambiar donde pone "TOKEN" por el token que os ha dado BotFather
    updater = Updater("248326254:AAFOkR3P9jRCCdRoYM-a2L3rqkJOpJ6BTGU")

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    # Ahora registramos cada método a los comandos necesarios
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holamundo", hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", logo))

    # Registramos también el modo inline
    dispatcher.add_handler(InlineQueryHandler(inline))

    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()


# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    main()
