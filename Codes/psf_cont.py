import numpy as np
import matplotlib.pyplot as plt


class IMG:
    def __init__(self,Nx,Ny):
        self.Nx=Nx
        self.Ny=Ny
        self.Xa=np.zeros(2)
        self.Xb=np.zeros(2)
        self.Amp=np.zeros([Ny,Nx],dtype=np.complex)
        self.Nx=Nx
        self.Ny=Ny
    def clear(self):
        self.Amp=np.zeros([Ny,Nx],dtype=np.complex)

    def set_xlim(self,x1,x2):
        self.Xa[0]=x1
        self.Xb[0]=x2
        self.xlim=np.array([x1,x2])
        self.xcod=np.linspace(x1,x2,self.Nx)
    def set_ylim(self,y1,y2):
        self.Xa[1]=y1
        self.Xb[1]=y2
        self.ylim=np.array([y1,y2])
        self.ycod=np.linspace(y1,y2,self.Nx)
    def show(self,ax):
        ext=[self.xlim[0],self.xlim[1],self.ylim[0],self.ylim[1]]
        Amax=np.max(np.abs(self.Amp[:]))
        im=ax.imshow(np.real(self.Amp)/Amax,extent=ext,origin="lower",cmap="gray",interpolation="none",vmin=-0.8,vmax=0.8)
        ax.set_aspect(1.0)
        fsz=14
        #ax.set_xlabel("x",fontsize=fsz)
        #ax.set_ylabel("y",fontsize=fsz)
        ax.tick_params(labelsize=fsz)
        ax.grid(True)

        return(im)
    def draw(self,Y1,Y2,sig=0.1):
        x1=self.xlim[0]
        x2=self.xlim[1]
        xcod=np.linspace(x1,x2,self.Nx)

        y1=self.ylim[0]
        y2=self.ylim[1]
        ycod=np.linspace(y1,y2,self.Ny)
        [X,Y]=np.meshgrid(xcod,ycod)
        
        rx=X-Y1[0]
        ry=Y-Y1[1]
        ri=np.sqrt(rx*rx+ry*ry)

        rx=X-Y2[0]
        ry=Y-Y2[1]
        rj=np.sqrt(rx*rx+ry*ry)

        rij=ri+rj
        
        R1=np.linalg.norm(Y1) 
        R2=np.linalg.norm(Y2) 
        Rf=R1+R2
        arg=Rf-rij;
        arg*=arg;
        self.Amp+=np.exp(-arg/sig*0.5)
    def draw_cont(self,Y1,Y2,lmb=2):

        # imaging grid
        x1=self.xlim[0]
        x2=self.xlim[1]
        xcod=np.linspace(x1,x2,self.Nx)

        y1=self.ylim[0]
        y2=self.ylim[1]
        ycod=np.linspace(y1,y2,self.Ny)
        [X,Y]=np.meshgrid(xcod,ycod)
        
        #source to grid distance
        rx=X-Y1[0]  
        ry=Y-Y1[1]  
        ri=np.sqrt(rx*rx+ry*ry)
        # receiver to grid distance
        rx=X-Y2[0]
        ry=Y-Y2[1]
        rj=np.sqrt(rx*rx+ry*ry)

        # Filght distance (S-> Pixel-> R)
        rij=ri+rj
        
        Ysc=np.array([0,0]) # scattering point
        dlt=0.0 # phase delay  (measured in length)
        R1=np.linalg.norm(Y1-Ysc) 
        R2=np.linalg.norm(Y2-Ysc) 
        Rf=R1+R2+dlt
        PI2=2*np.pi
        self.Amp+=np.exp(1j*PI2*(Rf-rij)/lmb)
    def SAFT(self,M,R,Lmb):
        #Lmb=2.0
        #M=14    # T/R points
        #R=2.0   # T/R radial distance
        dth=2*np.pi/M   # angular increment
        Y1=np.zeros(2)
        xtr=[]
        ytr=[]
        for k in range(M):  # imaging 
            th=dth*k
            Y1[0]=R*np.cos(th)
            Y1[1]=R*np.sin(th)
            self.draw_cont(Y1,Y1,lmb=Lmb) # stack continuous wave
            xtr.append(Y1[0])
            ytr.append(Y1[1])
        self.xtr=xtr
        self.ytr=ytr
        self.Amp/=M
        self.M=M
    def show_TR_points(self,ax):
        xtr=self.xtr
        ytr=self.ytr
        ax.plot(xtr,ytr,"ko",markersize=6,markerfacecolor="w")
    def show_profile(self,ax,Ycut=0.0,lstyl="-k"):
        ny=np.argmin(abs(Ycut-self.ycod))
        bx.plot(self.xcod,abs(np.real(im.Amp[ny,:])),lstyl,label="M="+str(self.M))


if __name__=="__main__":
    fig1=plt.figure()
    ax=fig1.add_subplot(111)

    # IMAGE SIZE & AREA
    Nx=100; Ny=100  # Image Size
    im=IMG(Nx,Ny)
    im.set_xlim(-3,3)   # Range x
    im.set_ylim(-3,3)   # Range y

    Lmb=2.0 # Wave Length
    M=10    # T/R points
    R=2.0   # T/R radial distance

    im.SAFT(M,R,Lmb)    #perform saft
    im.show(ax)
    im.show_TR_points(ax)

    fig1.savefig("psf_cont_M"+str(M)+".png",bbox_inches="tight")

    fig2=plt.figure()
    bx=fig2.add_subplot(111)
    im.show_profile(bx,Ycut=0,lstyl="k-")

    im.clear()
    ax.clear()

    M=20    # T/R points
    R=2.0   # T/R radius
    im.SAFT(M,R,Lmb)
    im.show(ax)
    im.show_TR_points(ax)
    fig1.savefig("psf_cont_M"+str(M)+".png",bbox_inches="tight")

    #bx.plot(im.xcod,abs(np.real(im.Amp[N2,:]))/M,"k--",label="M="+str(M))
    im.show_profile(bx,Ycut=0,lstyl="k--")
    bx.grid(True)

    fsz=14
    #bx.set_xlabel("x",fontsize=fsz)
    #bx.set_ylabel("I(x)",fontsize=fsz)
    ax.tick_params(labelsize=fsz-2)
    bx.tick_params(labelsize=fsz-2)
    #bx.legend()

    fig2.savefig("psf_cont_profile.png",bbox_inches="tight")

    plt.show()
