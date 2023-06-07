import math
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(0,2*np.pi,100)
def f(x):
    return (np.power(np.cos(xpoints),3))
#plt.plot(xpoints,f(xpoints),'o:c', ms=10)
plt.title('$x=cos^{3}(t)$\n$y=sin^{3}(t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(x):
    return (np.sin(xpoints)**3)
#plt.plot(xpoints,y(xpoints),'o:m', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
#plt.show()

tpoints = np.linspace(-2*np.pi,2*np.pi,100)
def f(t):
    return (t+2*np.sin(2*t))
#plt.plot(tpoints,f(tpoints),'o:c', ms=10)
plt.title('$x=t+2sin(2t)$\n$y=t+2sen(5t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (t+2*np.cos(5*t))
#plt.plot(tpoints,y(tpoints),'o:m', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
#plt.show()

tpoints = np.linspace(0,2*np.pi,100)
def f(t):
    return (np.sin(3*t))
plt.plot(tpoints,f(tpoints),'o:c', ms=10)
plt.title('$x=sin(3t)$\n$y=sin(4t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (np.sin(4*t))
plt.plot(tpoints,y(tpoints),'o:m', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.show()