import numpy as np
import matplotlib.pyplot as plt

V0 = int(input("Podaj poczatkowa predkosc "))
alfa = int(input("Podaj kąt rzutu "))

Vy0 = np.sin(np.radians(alfa)) * V0
Vx = np.sin(np.radians(alfa)) * V0
tpol = Vy0/9.81
Hmax = Vy0*tpol - (9.81*tpol**2)/2
X = Vx*2*tpol
T = 2*tpol
print('\n',"Wysokosc maksymalna= ",Hmax,'\n',"Zasięg rzutu= ",X,'\n',"Czas lotu= ",T)
Tcale = np.linspace(0,T,100)

#predkosc pozioma i pionowa
plt.subplot(1, 3, 1)
Vxx = np.linspace(Vx,Vx,100)
Vy = np.abs(Vy0 - 9.81*Tcale)
#Vy = Vy0 - 9.81*Tcale

plt.title("predkosci")
plt.plot(Tcale,Vy, label="Vy(t)")
plt.plot(Tcale,Vxx, label="Vx(t)")
plt.legend()

plt.title("położenie")
#położenie
plt.subplot(1,3,2)
X = Vx*Tcale
Y = Vy0*Tcale - (9.81*Tcale**2)/2
plt.plot(Tcale,X, label="x(t)")
plt.plot(Tcale,Y, label="y(t)")
plt.legend()

plt.title("tor ruchu")
#tor ruchu
plt.subplot(1,3,3)
plt.plot(X,Y, label="y(x)")

plt.legend()
plt.show()
