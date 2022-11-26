#include<stdio.h>
int factorial(int x);
int x;
main(){
	printf("Ingresa x");
	scanf("%d", &x);
	printf("%d", factorial(x));
}
int factorial(int x){
	int rta;
	if(x==0){
		rta=1;
	}else{
		rta=x*factorial(x-1);
	}
	return rta;
}
