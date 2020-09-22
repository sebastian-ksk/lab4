/*##########################################################################
#           ███╗   ███╗██╗ ██████╗██████╗  ██████╗       ██████╗           #
#           ████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗      ██╔══██╗          #
#           ██╔████╔██║██║██║     ██████╔╝██║   ██║█████╗██████╔╝          #
#           ██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║╚════╝██╔═══╝           #
#           ██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝      ██║               # 
#           ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝       ╚═╝               #                                
############################################################################ 
#                _               ____    _   _      _  _                   # 
#               | |        /\   |  _ \  | \ | |    | || |                  # 
#               | |       /  \  | |_) | |  \| | ___| || |_                 # 
#               | |      / /\ \ |  _ <  | . ` |/ _ \__   _|                # 
#               | |____ / ____ \| |_) | | |\  | (_) | | |                  #  
#               |______/_/    \_\____/  |_| \_|\___/  |_|                  #  
############################################################################
#INTEGRANTES: KEVIN ARBEY ALARCON LEON   COD:201512409                     #
#             JUAN SEBASTIAN CASTELLANOS COD:201411425                     #
#             EMILSE FUENTES GARCIA      COD:201510603                     #
############################################################################
#OBJETIVO DEL PROGRAMA: PUNTO No 2:                                        # 
# implementar un algoritmo que permita el calculo del determinante de una  #
# matriz nxn, en lenguaje C para tarjeta Raspberry-pi                      #                                             
############################################################################
#COMENTARIOS:                                                              #
#para ejecutar en raspberry                                                #
#gcc -o PROGRAM PROGRAM.c -lm -std=c99 -Wall -DTEST --debug                # 
#./punto2                                                                  #
#----------------------------inicio de programa---------------------------*/

/* INCLUCION DE LIBRERIAS PARA CALCULOS MATEMATICOS E ITERPRETACION DEL
   CODIGO*/
#include <stdio.h>
#include <math.h>
// SE DEFINE EL MAXIMO VALOR DE LA MATRIZ PARA EVITAR ERRORES EN LA 
// DISPOSICION DE MEMORIA
#define max_valor 20    

/*-------------------------------------------------------------------------
INICIALIZACION DE LAS FUNCIONES A USAR EN EL PROGRAMA
--VIS_MAT: PERMITE LA VIZUALIZACION EN FORMA CUADRADA DE LA MATRIZ
--DETERMINATE: CALCULA EL VALOR DEL DETERMINATE DE CADA MATRIZ ENVIADA
  A LA FUNCION
--sub_determinante: PARA EL PROGRAMA SE USA EL METODO DE ELIMINACION 
                    POR FILAS POR TANTO SE REQUIERE PARA CALCULAR LOS
                    RESPECTIVOS FACTORES PARA CADA POCICION DE LA FILA 0
LA FUNCION DETERMINATE Y SUB_DETERMINATE SON FUNCIONES RECURSIVAS ENTRE SI
---------------------------------------------------------------------------*/
void vis_mat(float matriz[][max_valor], int tam);
float determinante(float matriz[][max_valor], int tam);
float sub_determinante(int tam, float matriz[][max_valor],  int fila, int columna);
int main();
/*------------------------------------------------------------------------------
---------------------VISUALIZACION DE MATRIZ----------------------------------*/
void vis_mat(float matriz[][max_valor], int tam)
{
   printf("\t----------------MATRIZ [%d x %d]= -----------------------\n", tam,tam); //ENCABEZADO DE LA MATRIZ
   for (int i = 0; i < tam; i++) 
   {                                    //RECORRIDO DE FILAS                  
     printf("|");
      for (int j = 0; j < tam; j++) 
      {                                 //RECORRIDO DE COLUMNAS
          printf("\t%f", matriz[i][j]); //VIZUALIZACION DE FACTOR [FILA][COLUMNA]
      }
      printf("\t|\n");
   }
} 
/*------------------------------------------------------------------------------
-----------------CALCULO DE SUBDETERMINANTE O COFACTOR DE ECUACION------------*/
float sub_determinante(int tam, float matriz[][max_valor],  int fila, int columna)
{
   float submatriz[max_valor][max_valor];  //INICIALIZACION DE SUBMATRIZ DE HASTA EL MAXIMO TAMAÑO
   int n = tam - 1;                       //TAMAÑO DE LA SUBMATRIZ
   int sub_col= 0;                        //INDICADORES DE COLUMNA
   int sub_fila = 0;                      //Y FILA PARA LA SUBMATRIZ
   for (int i = 0; i < tam; i++)          //RECORRIDO DE FILAS DE LA MATRIZ PARA OPTENER LA SUBMATRIZ
    {      
    for (int j = 0; j < tam; j++)         //RECORRIDO DE COLUMNAS DE DE LA MATRIZ PARA OPTENER LA SUBMATRIZ
       {
         if (i != fila && j != columna)   //DISCRIMINACION DE LA FILA Y COLUMNA INICADAS POR LA FUNCION DETERMINATE
         {                                //PARA EL CASO SIEMPRE CERA LA FILA[0] COLUMNA[ 0 HASTA TAM]
            submatriz[sub_fila][sub_col] = matriz[i][j]; //CREACION TERMINO A TERMINO DE LA SUBMATRIZ[TAM-1 X TAM-1]
            sub_col++;                                   //INCREMENTO HACIA LA SIGUIENTE COLUMNA 
            if (sub_col >= n)                           //CONDICIONAL FINAL DE COLUMNAS
            {
               sub_fila++;                              //INCREMENTO HACIA LA SISGUIENTE FILA
               sub_col = 0;                             //REINICO PARA RECORRIDO DE LASCOLUMNAS
            } } } }
  //EL FACTOR RESULTANTE OBEDECE A LA FORMULA GENERAL (-1)^(FILA+COLUMNA)*DET(SUBMATRIZ[TAM-1 X TAM-1])
  // PARA LO CUAL SE REQUIERE EL LLAMADO RECURSIVO A LA FUNCION DETERMINANTE()
   return pow(-1.0, fila + columna) * determinante(submatriz, n); 
}  
/*------------------------------------------------------------------------------
-----------------CALCULO DE DETRMINATE  DE LA MATRIZ------------*/
float determinante(float matriz[][max_valor], int tam)
{
   float det = 0.0;                               //INICIALIZACION DEL DETERMINATE
   if (tam == 1) {                                //SI LA MATRIZ ES DE TAMAÑO 1 REGRESA SU UNICO VALOR POSIBLE
      det = matriz[0][0];   
   } else {
      for (int j = 0; j < tam; j++) {            //RECORRIDO DE COLUMNAS SOBRE LA FILA 0
        //EL DETERMINATE  ES LA SUMATORIA DESDE i=0, SUM{a(i,j)*(-1)^(i+j)*DET[A(i,j)]} hasta n 
         det = det + matriz[0][j] * sub_determinante(tam, matriz,  0, j);
      }
   }
   
   return det;
}
 /*------------------------------------------------------------------------------
----------------------------FUNCION PRINCIPAL DEL PROGRAMA------------*/
int main()
{
  float matriz[max_valor][max_valor];
  int tam;
  //********************INGRESO DEL TAMAÑO DE LA MATRIZ*********************
  printf("\n\t------------------------------------------------------- \n");
  printf("\t\tTAMAÑO DE LA MATRIZ [MAX_VALOR %d]: ", max_valor);          
  scanf("%d", &tam);                                                    
  //DISCRIMINACION DE VARIABLES NO VALIDAS PARA EL TAMAÑO DE LA MATRIZ
  while (tam < 0 || tam > max_valor)
  {
    printf("\nEL TAMAÑO %d NO ES UN VALOR VALIDO \n", max_valor);
    printf("Ingrese nuevamente el tam de la matriz: ");
    scanf(" TAMAÑO= %d", &tam);
  }
  printf("\t\t\t\tTAMAÑO= %d", tam);

 //*************************************************************************
 //******************INGRESO DE DATOS DE LA MATRIZ**************************
  printf("\n\t------------------------------------------------------ \n");
  printf("\t---------------------INGRESO DE DATOS------------------ \n");
   for (int i = 0; i < tam; i++) {
      for (int j = 0; j < tam; j++) {
        printf("\t\t\t  DATO  %i %i = ",i,j);
        scanf("\t%f", &matriz[i][j]);
      }
      printf("\n");
   }
//**************************************************************************
//******************VISUALIZACION DE LA MATRIZ INGRESADA********************
   printf("\n\t----------------MATRIZ INGRESADA-----------------------\n");
   vis_mat(matriz, tam);
//**************************************************************************
//*****************CALCULO DEL DETREMINANTE DE LA MATRIZ********************
   printf("\n\t---------------------------------------------------------\n");
   printf("\n\tEL DETERMINANTE DE LA MATRIZ ES =: %f\n", determinante(matriz, tam));
//**************************************************************************
   return 0;
   
}
 

 

 
 

