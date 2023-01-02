import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=16

f=1.0
pi2=np.pi;
pi2=pi2*pi2;

f2=f*f

t0=1.0;
tt=np.linspace(0,10,801)
t2=tt-t0
t2=t2*t2
R=(1-2*pi2*f2*t2)*np.exp(-pi2*f2*t2)

W=np.fft.fft(R)
dt=tt[1]-tt[0]
Nt=len(tt)
df=1/dt/Nt
freq=np.arange(Nt)*df
fmax=1/dt*0.5

fig=plt.figure(figsize=[10,4])
ax=fig.add_subplot(121)
ax.plot(tt,R,"k")
ax.grid(True)
#ax.set_title("Ricker wavelet")
ax.set_xlim([0,5])

bx=fig.add_subplot(122)
bx.plot(freq,np.abs(W),"k")
bx.grid(True)
#bx.set_xlim([0,fmax])
bx.set_xlim([0,5])

fig.savefig("ricker.png",bbox_inches="tight")

plt.show()
