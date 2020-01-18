# Fails : 171.py
# Autors : Elvijs Buls
# Datums 13.01.2019
# Sagatave funkcijas saknes meklēšanai ar dihatomijas metodi
# -* - c o d i n g : utf -8 -* -

from math import sin, fabs
from time import sleep

def f(x):
	return sin(x)

k = 0

# Definējam argumenta x robežas
a = float(input("Ievadi saknes meklēšanas intervāla apakšējo robežu: "))
b = float(input("Ievadi saknes meklēšanas intervāla augšējo robežu: "))

# Aprēķinam funkcijas vērtības dotajos punktos
funa = f(a)
funb = f(b)

# Pārbaudām vai dotajā intervālā ir saknes
if (funa * funb > 0.0):
	# Ziņo uz ekrāna, gaida 1 sekundi un darbu pabeidz
	print("Dotajā intervālā [%s, %s] sakņu nav"%(a,b))
	sleep (1); exit ()
else :
	print("Dotajā intervālā sakne(s) ir!")

# Definējam precizitāti ar kādu meklēsim sakni
deltax = 0.0001

# Sašaurinām saknes meklēšanas robežas
while (fabs(b-a) > deltax):
	x = (a+b )/2; funx = f(x)
	k = k+1

	if (funa * funx < 0.):
		b = x
	else :
		a = x

print("Funkcijas saknes vērtība: x = ", x)
print("Dotās funkcijas vērtība šajā punktā: f(x) = ", f(x))
print("Nepieciešamo iterāciju skaits intervālu dalīšanai uz pusēm: ", k)
