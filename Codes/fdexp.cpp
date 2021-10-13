#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){
	int i,j,N;
	double pmax=4.0;
	double dp,p;
	int Np=11;

	double h;
	double A=1.0;
	double fk,gk,r,tmp;
	double x,ex,err;

	FILE *fp;
	char fname[128];

		printf("j=%d\n",j);
	sprintf(fname,"%s","order1.out");
	fp=fopen(fname,"w");
	fprintf(fp,"# h, N,  fk, exp(xk), |err|\n");

	dp=(pmax-1)/(Np-1);
	for(j=0;j<Np;j++){
		p=dp*j+1;
		N=pow(10,p);
		fk=A;
		h=1./N;
		r=1+h;
	for(i=0;i<N;i++){
		fk*=r;
		x=(i+1)*h;
		ex=exp(x);
		err=abs(fk-ex);
		//fprintf(fp,"# x,  fk, exp(xk), |err|\n");
		//fprintf(fp,"%lf %lf %lf %le\n",x,fk,ex,err);
	};
	fprintf(fp,"%le, %d, %lf, %le\n",h,N,ex,err);
	};


	double gk0,gk1,gk2;
	sprintf(fname,"%s","order2.out");
	fp=fopen(fname,"w");
	fprintf(fp,"# h, N,  fk, exp(xk), |err|\n");
	for(j=0;j<Np;j++){
		p=dp*j+1;
		N=pow(10,p);
		h=1./N;
		gk0=A*exp(-h);
		gk0=A;
		gk1=A;
	for(i=0;i<N;i++){
		if(i>0) gk=2.*h*gk1+gk0;
		if(i==0) gk=h*gk1+gk0;
		x=(i+1)*h;
		ex=exp(x);
		err=abs(gk-ex);
		gk0=gk1;
		gk1=gk;
	}
	fprintf(fp,"%le, %d, %lf, %le\n",h,N,ex,err);
	}

	return(0);
};
