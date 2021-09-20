#Son código ya escrito previamente, ya sea nuestro, de Python o de la comunidad

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=110))

from datetime import timedelta, date   # Si importo el método timedelta desde el modulo datetime, 
print(timedelta(minutes=110))    # puedo ejecutarlo sin especificar el origen
print(date.today())

import fmath
fmath.add(1,3)

from fmath import add
add(1,3)

# Pypi buena página para importar código. Cada código tiene 
# un comando que con solo ponerlo en la consola de windows hará 
# que se descargue. Posteriormente, tendremos que hacer import 
# y usar este código siguiendo su documentación adjunta