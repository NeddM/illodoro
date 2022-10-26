# ILLODORO
Script personal creado en Python, no es más que un programa para realizar la [Técnica Pomodoro](https://es.wikipedia.org/wiki/T%C3%A9cnica_Pomodoro).

El nombre no es más que una pequeña firma personal, dejando un poco de acento andaluz y de marca personal.

### Librerias necesarias
Para ejecutar el script, necesitamos de varias librerías, voy a facilitarlas todas a continuación:
* from **os** import **system**, **name**
* import **time**
* import **pyaudio**
* import **wave**
* import **sys**

### Funcionamiento
El funcionamiento es sencillo.

Ejecutamos el script, y se nos pedirá un tiempo en minutos; ese tiempo es el periodo en el que estaremos trabajando.

En base al tiempo que estemos trabajando, se nos crea otro periodo de tiempo para los descansos cortos, y otro periodo de tiempo para los descansos largos.
Los descansos cortos son una quinta parte del periodo de tiempo trabajado, y los descansos largos son como cuatro descansos cortos.

Una vez hayamos introducido el tiempo de trabajo, el programa nos preguntará si estamos seguros de que queremos empezar a trabajar con ese tiempo; existen tres respuestas:
* **Y / Yes**: Confirmamos que queremos empezar a ejecutar el script  con el tiempo introducido.
* **N / No**: No queremos trabajar con el tiempo introducido, y se ejecuta de nuevo el programa.
* **Exit**: Salimos del script.

Una vez confirmemos que el tiempo introducido es correcto, comenzará una cuenta atrás. Cuando esta cuenta atrás llegue a cero, sonará un aviso de que comienza nuestro tiempo de descanso corto.

Después de cuatro periodos de trabajo, disfrutaremos de un periodo de descanso largo.

---

# ILLODORO
Personal script created with Python, it is just the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

The name is just a personal signature, leaving my personal brading.

### Imports needed
To execute this script we need some packages:
* from **os** import **system**, **name**
* import **time**
* import **pyaudio**
* import **wave**
* import **sys**

### How it works
We start the script, and it will ask for the minutes; this minutes are the working time.

With that working time, the script calculates the rest time, long and short.
The short rest time is five times shorter than the working time, and the long rest is four times longer than the short rest time.

Once we had made the input of minutes, the script will ask about if we are sure that we want to work with this range time. We can give three answers:
* **Y / Yes**: We confirm that we want to start the script with the time range we set.
* **N / No**: We missed when setting the working time, so the script will restart.
* **Exit**: Exits the script.

Once confirm, the countdown will start, when the countdown is at cero. The script will make a sound effect. Its time to rest a little bit!
