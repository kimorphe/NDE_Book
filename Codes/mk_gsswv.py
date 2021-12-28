import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)

sig=0.3
tb1=1.0
tb2=2.0

tt=np.linspace(-5,10,300)

arg=(tt-tb1)/sig
arg*=arg
a1=np.exp(-arg*0.5)

arg=(tt-tb2)/sig
arg*=arg
a2=np.exp(-arg*0.5)

ax1.plot(tt,a1)
ax2.plot(tt,a2)

ax1.set_xlim([-5,10])
ax2.set_xlim([-5,10])
ax1.set_ylim([-0.5,1.2])
ax2.set_ylim([-0.5,1.2])
ax1.set_axis_off()
ax2.set_axis_off()
fig.savefig("wvfms.png",bbox_inches="tight")
ax1.grid(True)
ax2.grid(True)
plt.show()
