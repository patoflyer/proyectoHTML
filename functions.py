import math
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(-6,2,200)
def f1(x):
    return -(xpoints**2)- (4*xpoints) - 5
#plt.plot(xpoints, f1(xpoints),'o:g')
plt.title('f(x)=$-x^{2}-4x-5$')
plt.ylabel('Eje x')
plt.xlabel('Eje y')
#plt.show()

xpoints = np.linspace(-1,5,100)
def f2(x):
    return (2*xpoints**2)- (8*xpoints) - 11
#plt.plot(xpoints, f2(xpoints),'o:r', ms = 10)
plt.title('$f(x)=2x^{2}-8x-11$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#plt.show()

tpoints = np.linspace(-1,5,100)
def f3(t):
   return (tpoints*np.exp(-2*tpoints))
#plt.plot(tpoints,f3(tpoints),'o:k', ms = 10)
plt.title('$f(t)=te^{-2t}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#plt.show()

tpoints = np.linspace(0,-24,250)
def h(t):
    return (np.sin(2*tpoints)*np.exp(-0.1*tpoints))
#plt.plot(tpoints,h(tpoints),'o:k', ms = 10)
plt.title('$h(t)=sin(2t)*e^{-0.1t}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#plt.show()

xpoints = np.linspace(0,4*np.pi,200)
def s(x):
    return (np.cos(2*xpoints)+np.sin(3*xpoints))
#plt.plot(xpoints,s(xpoints),'o:b', ms = 10)
plt.title('$s(x)=cos(2x)+sin(2x)$\n$v(x)=-2sin(2x)+3cos(3x)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def v(x):
    return (-2*np.sin(2*xpoints)+3*np.cos(3*xpoints))
#plt.plot(xpoints,v(xpoints),'o:r', ms = 10)
plt.legend(['$s(x)$','$v(x)$'])
#plt.show()

xpoints = np.linspace(0,4*np.pi,200)
def f4(x):
    return (xpoints*np.exp(-3*xpoints))
#plt.plot(xpoints,f4(xpoints),'o:c',ms=10)
plt.title('$f(x)=xe^{-3x}$\n$g(x)=1-3xe^{-3x}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def g(x):
    return (1-(3*xpoints*np.exp(-3*xpoints)))
#plt.plot(xpoints,g(xpoints),'o:m', ms=10)
plt.legend(['f(x)','g(x)'])
#plt.show()

tpoints = np.linspace(0,4*np.pi,100)
def f5(t):
    return (np.sin(3*tpoints)*(np.cos(2*tpoints)))
#plt.plot(tpoints,f5(tpoints),'o:c', ms=10)
plt.title('$f(t)=sin(3t)*cos(2t)$\n$g(t)=(1/2)*cos(t))+(5/2)(cos(5t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def g2(t):
    return (0.5*np.cos(tpoints)+(5/2)*np.cos(5*tpoints))
#plt.plot(tpoints,g2(tpoints),'o:m', ms =10)
plt.legend(['$f(t)$','$g(t)$'])
#plt.show()

tpoints = np.linspace(0,2*np.pi,100)
def x(t):
    return ((1+np.sin(tpoints))*(np.cos(tpoints)))
plt.plot(tpoints,x(tpoints),'o:c', ms=10)
plt.title('$x(t)=$(1+sin(t))*cos(t)\n$y(t)=(1+2sin(t))*(sin(t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (1+(2*np.sin(tpoints))*(np.sin(tpoints)))
plt.plot(tpoints,y(tpoints),'o:m', ms =10)
plt.legend(['$x(t)$','$y(t)$'])
plt.show()