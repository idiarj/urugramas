#include<stdio.h>
#include<windows.h>
int opc;
int suma(int a, int b);
int resta(int a, int b);
int multiplicacion(int a, int b);
float division(float c, float d);
main()
{
    do{
	printf("Menu\n");
	printf(" 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n Que opcion desea: ");
	scanf("%d", &opc);
	system("cls");
}while(opc>4 || opc<1);
	switch(opc){
	case 1: 
	int a;
	int b;
	printf("Ha escogido la opcion de suma\n");
	printf("El resultado es %d", suma(a, b));
	break;
	case 2:
	printf("Ha escogido la opcion de resta\n");
    printf("El resultado es %d", resta(a, b));
	break;
	case 3: 
	printf("Ha escogido la opcion de multiplicacion");
	printf("El resultado es %d", multiplicacion(a, b));
	case 4:
	printf("Ha escogido la opcion de division\n");
	float c;
	float d;
	printf("Ha escogido la opcion de multiplicacion");
	printf("El resultado es %f", division(c, d));
		
	}
		return 0;	
}
	int suma(int a, int b)
	{
		int resultadoS;
		printf("Ingrese el primer numero a: ");
		scanf("%d", &a);
		printf("Ingrese el segundo numero b: ");
		scanf("%d", &b);
		resultadoS=a+b;
		return resultadoS;
    }
    	int resta(int a, int b)
	{
		int resultadoR;
		printf("Ingrese el primer numero a: ");
		scanf("%d", &a);
		printf("Ingrese el segundo numero b: ");
		scanf("%d", &b);
		resultadoR=a-b;
		return resultadoR;
    }
    	int multiplicacion(int a, int b)
	{
		int resultadoM;
		printf("Ingrese el primer numero a: ");
		scanf("%d", &a);
		printf("Ingrese el segundo numero b: ");
		scanf("%d", &b);
		resultadoM=a*b;
		return resultadoM;
    }
        float division(float c, float d)
	{
		float resultadoD;
		printf("Ingrese el primer numero c(numerador): ");
		scanf("%f", &c);
		printf("Ingrese el segundo numero d(denominador): ");
		scanf("%f", &d);
		resultadoD=c/d;
		return resultadoD;
    }
    
