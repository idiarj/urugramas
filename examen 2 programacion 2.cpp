#include<stdio.h>
int opc, i, k=1;
struct artista{
	char nombre [15];
	int edad;
	struct albumes{
	char nombrealbum[10];
	int fecha;
	float valoracion;
}albumes[2];
}artistas[2];

//Prototipo
void Menu();
void ingresar();
void mostrar();
void salir();

main(){
	Menu();
	return 0;
}
//Definicion
void ingresar(){
	for(i=0;i<2;i++){
		fflush(stdin);
		printf("Ingresa el Nombre del artista numero %d: ", i+1);
        gets(artistas[i].nombre);
        fflush(stdin);
        printf("Ingresa la edad del artista numero %d: ", i+1);
        scanf("%d", &artistas[i].edad);
        fflush(stdin);
        printf("Ingresa el nombre del album del artista numero %d: ", i+1);
        gets(artistas[i].albumes[i].nombrealbum);
        fflush(stdin);
        printf("Ingresa la fecha de lanzamiento del album del artista numero %d: ", i+1);
        scanf("%d", &artistas[i].albumes[i].fecha);
        fflush(stdin);
        printf("Ingresa la valoracion del album del artista numero %d: ", i+1);
        scanf("%f", &artistas[i].albumes[i].valoracion);
        fflush(stdin);
}
}
void mostrar(){
	for(i=0;i<2;i++){
	fflush(stdin);
    printf("El nombre del artista numero %d es: %s ", i+1, artistas[i].nombre);
    fflush(stdin);
    printf("\nLa edad de %s es: %d", artistas[i].nombre, artistas[i].edad);
    fflush(stdin);
    printf("\nEl nombre del album digitado de %s es: %s", artistas[i].nombre, artistas[i].albumes[i].nombrealbum);
    fflush(stdin);
    printf("\nLa fecha de lanzamiento del album %s de %s es: %d", artistas[i].albumes[i].nombrealbum, artistas[i].nombre, i+1, artistas[i].albumes[i].fecha);
    fflush(stdin);
    printf("\nLa valoracion de %s del artista %s es: %f \n", artistas[i].albumes[i].nombrealbum, artistas[i].nombre, artistas[i].albumes[i].valoracion);
    fflush(stdin);
}
}
void salir(){
	k--;
}

void Menu(){
	do{
	printf(" 1. Ingresar datos.\n 2. Mostrar Datos.\n 3. Salir.\n Que opcion desea usar: ");
	scanf("%d", &opc);
	if(opc>3 || opc<1){
		printf("\nOpcion invalida\n");
		printf("_______________\n \n");
	}else{
	
	switch(opc){
		case 1: 
		ingresar();
	break;
	    case 2:
	    	mostrar();
	break;
	case 3:
		salir();
		break;
}
}
}while(k);
}






