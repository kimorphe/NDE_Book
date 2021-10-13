#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(int argc, char* argv[]){

	int Nt=200;	// total time steps

	double m0=1.0;	// mass 
	double k0=1.0;	// spring constant
	double w0=sqrt(k0/m0);	// natural angular frequency

	// m u''(t) +k u(t)=0
	//	Initial Condition
	double u0=1.0;	// displacement 
	double v0=0.0;	// velocity

	double PI=4.0*atan(1.0);
	double T0=2.*PI/w0;	// natural period
	printf("Natual period T0=%lf",T0);
	double Td=5*T0;	// time range
	double dt=Td/Nt;	// time increment
	int i;

	double tt=0.0;
	double U2,U1,U0;
	U1=u0;
	U0=U1-dt*v0;
	printf("%lf, %lf, %lf\n",tt,U1,u0);
	double u_true;
	double h2=(dt*w0)*(dt*w0);

	char fname[128];
	sprintf(fname,"sdof%d.out",Nt); // sdof(Nt).out
	FILE *fp=fopen(fname,"w");
	fprintf(fp,"# time[/T0], u_FD, u_exact\n");
	fprintf(fp,"%lf, %lf, %lf\n",0.0,u0,u0);
	for(i=0;i<Nt;i++){
		tt=(i+1)*dt;
		U2=2.*U1-U0-h2*U1;  // central
		//U2=(2.*U1-U0)/(1+h2); // backward
		//U2=2.*U1-U0-h2*U0;  // forward
		u_true=u0*cos(w0*tt);
		fprintf(fp,"%lf, %lf, %lf\n",tt/T0,U2,u_true);
		U0=U1;
		U1=U2;
	}
	printf("# h=%lf\n",w0*dt);
	fclose(fp);

	return(0);
};
