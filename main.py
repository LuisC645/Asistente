import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar microfono y devolver el audio en texto
def transformar_audio_a_texto():

    #almacenar reconocedor en variables
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold=0.8

        #informar que comenzo la grabacionB
        print('ya puedes hablar')

        #guardra audio 
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio,languaje="es-ar")

            #prueba de que pudo ingresar
            print(f"Dijiste: {pedido}")

            #devolver pedido
            return pedido
        
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print('ups, no entendi')

            #devolver error
            return 'sigo esperando'

        except sr.RequestError:

            #no comprendio
            print('Error al buscar')

            #devolver Error
            return 'Error al buscar'

        #error inesperado
        except:
            #no comprendio
            print('Error desconocido')

            #devolver Error
            return 'Algo ha salido mal'

transformar_audio_a_texto()
