import math
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(-6,2,200)
def f1(x):
    return -(xpoints**2)- (4*xpoints) - 5
#plt.plot(xpoints, f1(xpoints),'o:g')
plt.title('Funcion 1: -x^2-4x-5')
plt.ylabel('Edad')
plt.xlabel('Tiempo')
#plt.show()

xpoints = np.linspace(-1,5,100)
def f2(x):
    return (2*xpoints**2)- (8*xpoints) - 11
#plt.plot(xpoints, f2(xpoints),'o:r', ms = 10)
plt.title('Funcion 2: 2x^2-8x-11')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#plt.show()

tpoints = np.linspace(-1,5,100)
def f3(t):
   return (tpoints*np.exp(-2*tpoints))
#plt.plot(tpoints,f3(tpoints),'o:k', ms = 10)
plt.title('Function 3: f(t)=$te^-2t$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#plt.show()

tpoints = np.linspace(0,-24,250)
def h(t):
    return (np.sin(2*tpoints)*np.exp(-0.1*tpoints))
#plt.plot(tpoints,h(tpoints),'o:k', ms = 10)
plt.title('Function 4: h(t)=$sin(2t)*e^-0.1t$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#plt.show()

xpoints = np.linspace(0,4*np.pi,200)
def s(x):
    return (np.cos(2*xpoints)+np.sin(3*xpoints))
plt.plot(xpoints,s(xpoints),'o:b', ms = 10)
plt.title('Function 5: ')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

def v(x):
    return (-2*np.sin(2*xpoints)+3*np.cos(3*xpoints))
plt.plot(xpoints,v(xpoints),'o:m', ms = 10)
plt.legend('Funciones:')
plt.show()