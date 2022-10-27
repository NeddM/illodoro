from os import system, name
import time
import pyaudio
import wave
import sys

tituloApp = " - - " * 3 + " ILLODORO " + " - - " * 3
colorBlanco = "\033[0;37m"
colorRojo = "\033[0;31m"
colorVerde = "\033[0;32m"
colorAmarillo = "\033[0;33m"


def sonido(color):
    limpiarConsola()
    print("\033[0;37m" + tituloApp)
    print(color + "00:00")
    chunk = 1024
    f = wave.open(r"sonido.wav", "rb")
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)

    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()


def limpiarConsola():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def cuentaAtras(color, segundosTrabajo):
    print("\033[0;37m" + tituloApp)
    while segundosTrabajo:
        minutos, segundos = divmod(segundosTrabajo, 60)
        contador = "{:02d}:{:02d}".format(minutos, segundos)
        print(color + contador, end="\r")
        time.sleep(1)
        segundosTrabajo -= 1
    sonido(color)


def main():
    limpiarConsola()
    print("\033[0;37m" + tituloApp)
    contador = 0
    try:
        segundosTrabajo = input("Introduce el tiempo de trabajo en minutos: ")
        segundosTrabajo = int(segundosTrabajo) * 60
        segundosDescanso = round(segundosTrabajo / 5)
        segundosDescansoLargo = round(segundosDescanso * 4)
        confirmacion = input(
            "\033[0;37m" + "¿Estás listo para empezar? (Yes/No/Exit): ")

        if confirmacion.upper() == "Y" or confirmacion.upper() == "YES":
            while contador < 5:
                if contador < 3:
                    limpiarConsola()
                    cuentaAtras(colorRojo, segundosTrabajo)
                    contador += 1
                    limpiarConsola()
                    cuentaAtras(colorVerde, segundosDescanso)
                elif contador == 3:
                    limpiarConsola()
                    cuentaAtras(colorRojo, segundosTrabajo)
                else:
                    limpiarConsola()
                    cuentaAtras(colorAmarillo, segundosDescansoLargo)
                    contador = 0
        elif confirmacion.upper() == "N" or confirmacion.upper() == "NO":
            main()
        else:
            sys.exit()

    except ValueError:
        print("¡Inserta un valor válido!")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
