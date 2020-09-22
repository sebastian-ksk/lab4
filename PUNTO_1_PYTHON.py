############################################################################
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
#OBJETIVO DEL PROGRAMA: PUNTO No 1:                                        # 
# implementar un algoritmo que permita el calculo de la tabla de Routh     # 
# teniendo en cuenta los casos especiales                                  #     
############################################################################
#----------------------------inicio de programa----------------------------
import sys                                  
######################################
#FUNCION PARA CALCULAR EL DETERMINANTE
#DE LA MATRIZ 2X2 PARA EL CALCULO
#DE COEFICIENTES DE LA TABLA DE
#ROUTH
######################################
def determinante(a,b,c,d):
    deter=(a*b-c*d)/a
    return deter
########################################
#FUNCION PARA CALCULAR LA DERIVADA DEL
#ARREGLO ANTERIOR AL ARREGLO.
#PARA CASO ESPECIAL DE COEFICIENTES NULOS
#DERIVADA[I]=GRADO*ARREGLO_ANTERIOR[i] 
########################################
def deriv_casoe(vect_a,grado_v):
    fact=grado_v
    new_v=[0 for x in range(len(vect_a))]                                          
    for j in range(0 ,len(vect_a)):
        new_v[j]=vect_a[j]*fact                                                     
        fact-=2    
    return new_v
########################################
#FUNCION PRINCIPAL 
########################################
def main():
    #INICIALIZACION DE VARIABLES
    grado=0                     #GRADO DEL POLINOMIO                                                                
    dic_f={}                    #DICCIONARIO DE ALMACENAMIENTO E IDENTIFICACION DE FILAS DE TABLA DE ROUTH
    caso_esp=0                  #IDENTIFICADOR DE CASOSO ESPECIALES
    ceros=0                     #CONTADOR DE CEROS EN CADA AREGLO
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #CICLO DE INGLRESO DE GRADO DE POLINOMIO A EVALUAR
    while True:
        grado=input("INGRESE EL GRADO DEL POLINOMIO A EVALUAR: \n")   
        #FUNCION TRY: EVITA ERRORES DE INGRESO DE VALORES NO NUMERICOS           
        try:
            grado=int(grado)
            #DISCRIMINACION DE COEFICIENTES NEGATIVOS
            if(grado>0):
                print("EL GRADO DEL POLINOMIO ES: " + str(grado))
                break
            else:
                print("EL POLINOMIO DE GRADO: " + str(grado)+" NO ES VALIDO \n")
        except:
            print("el valor ingresado no es un entero")
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::        

    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #INGRESO DE COEFICIENTES DEL POLINOMIO
    tam=grado+1               #TAMAÑO DEL ARREGLO QUE ALMACENA LOS COEFICIENTES          
    par_im=tam%2              #VERIFICACION DE PARIDAD DEL AREGLO SI ES IMPAR EL GRADO ES PAR SI NO ESIMPAR
    #CALCULO DE LA CANTIDAD DE COLUMNAS QUE REQUIERE LA TABLA DE ROUTH 
    if par_im==1:
        col=int(((tam+1)/2))  #SI ES IMPAR COLUMNAS=(TAMAÑO_DE_ARREGLO+1)/2
    else:
        col=int((tam/2))      #SI ES PAR COLUMNAS=(TAMAÑO_DE_ARREGLO)/2
    #*****************************************************************    
    #GENERACION DEL ARREGLO PARA EL ALMACENAMIENTO DE LOS FACTORES DEL POLINOMIO
    polinomio= [0 for x in range(tam)]
    for i in range(0 ,tam):
        fact_a=float(input("FATOR DE  S^"+str(grado-i)+"="))    #INGERESO DEL VALOR DEL COEFICIENTE[I]
        if(fact_a>0):                                           #SI ES MAYOR QUE CERO ES ALMACENADO EN LA POSCICION i
            polinomio[i]=fact_a
            dic_f["S"+str(grado-i)]=[0 for x in range(col)]     #SE GUARDA UN ARREGLO DE CEROS PARA LOS DISTINTOS S^n
        else:                                                   #DISCRIMINACION Y ADVERTENCIA DE VALORES CERO O NEGATIVOS
            print("LA PRECENCIA DE UN FACTOR CERO O NEGATIVO,YA HACE AL SISTEMA INESTABLE \n")
            while True:
                if i==0 and fact_a==0:                          #EL VALOR DEL PRIMER FACTOR NO PUEDE CER CERO
                    print("EL FATOR DE  S^"+str(grado-i)+" NO PUEDE SER CERO")    
                    print(".................................................")   
                    main()
                    sys.exit(1)    
                cont=input("DESEA CONTINUAR: [Y/N]")
                if(cont=="n" or cont=="N"):
                    main()
                    sys.exit(1)
                elif(cont=="y" or cont=="Y"):
                    polinomio[i]=fact_a
                    dic_f["S"+str(grado-i)]=[0 for x in range(col)]  
                    break
                else:
                    print("COMANDO NO VALIDO ")
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #CONTRUCCION DE LA TABLA DE ROUTH
    #LLENADO DE LOS DOS PRIMEROS ARREGLOS****************************************************************
    i_p=0                                               #INDICADOR DE LA POSICION DEL ARREGLO  DE S^(GRADO)
    i_i=0                                               #INDICADOR DE LA POSICION DEL ARREGLO  DE S^(GRADO-1)
    for i in range(0 ,tam): 
        if i%2==0:
            dic_f["S"+str(grado)][i_p]=polinomio[i]     #GUARDA LOS VALORES DE POSCICION PAR EN EL ARREGLO DE S^GRADO PARA LA TABLA DE ROUTH
            i_p+=1
        else:    
            dic_f["S"+str(grado-1)][i_i]=polinomio[i]   #GUARDA LOS VALORES DE POSCICION IMPAR EN EL ARREGLO DE S^(GRADO-1)n PARA LA TABLA DE ROUT
            i_i+=1
    #*****************************************************************************************************
    #CALCULO DE LOS FACTORES SIGUIENTES PARA LOS ARREGLOS RESTANTES DE LA TABLA DE ROUTH******************
    i_p=grado                                           #INDICADOR DE LA POSICION DEL ARREGLO  DE S^(GRADO) PARA EL CALCULO DE COEFICIENTES
    i_i=grado-1                                         #INDICADOR DE LA POSICION DEL ARREGLO  DE S^(GRADO-1) PARA EL CALCULO DE COEFICIENTES
    #RECORRIDO DE TODAS LOS S^N=TAMAÑO DEL ARREGLO POLINOMIO
    for i in range(2 ,tam):
        #CALCULO DE COEFICIENTES A PARTIR DE DETERMINATE DE MATRICES 2X2 PARA COMPLETAR TABLA DE ROUTH
        for j in range(0 ,col-1):
            d=dic_f["S"+str(i_i)][1+j]                  #COEFICIENTE D=COEFICIENTE[1+j] DEL AREGLO S^(I_I)
            a=dic_f["S"+str(i_i)][0]                    #COEFICIENTE A=COEFICIENTE[0] DEL AREGLO S^(I_I)
            b=dic_f["S"+str(i_p)][1+j]                  #COEFICIENTE B=COEFICIENTE[1+j] DEL AREGLO S^(I_P)    
            c=dic_f["S"+str(i_p)][0]                    #COEFICIENTE C=COEFICIENTE[0] DEL AREGLO S^(I_P)    
            det=round(determinante(a,b,c,d),2)          #CALCULO DEL DETERMINANTE DE LA MATRIZ 2X2 PARA ALMACENAR EL ARREGLO S^(GRADO-I)
            #CONTEO DE CEROS INCURRIDOS EN LA OPERACION 
            if det==0:
                ceros+=1
            else:
                dic_f["S"+str(grado-i)][j]=det
        #**********************************************************************************************       
        #A PARTIR DE CEROS EXISTENTES EN EL ANTERIOR CALCULO SE DETERMINA EL CASO ESPECIAL, SI OCURRIO
        if ceros>0:
            if dic_f["S"+str(grado-i)][0]==0:
                caso_esp=1                   #SI SOLO EXISTE UN CERO EN LA POCICION[0] SE DETERMINA CASO ESPECIAL 1
                for j in range(1 ,col-1):
                    if dic_f["S"+str(grado-i)][j]==0: #SI EXISTEN MAS CEROS SE DETERMINA CASOESPECIAL 2
                        caso_esp+=1
                    else:
                        caso_esp=caso_esp
            else:
                caso_esp=0                  #SI NO OCURRIO CASO ESPECIAL 1 SE PUEDE CONTINUAR CON EL PROCEDIMIENTO
        #*********************************************************************************************************

        #------------------------------CASOS ESPECIALES----------------------------------------------------------
        if caso_esp>0:
            #CASO 1: EL VALOR INICIAL DEL ARREGLO ES CERO POR TANTO SE REMPLAZA EL VALOR POR UN NUMERO 
            #INFINITESIMALMENTE PEQUEÑO PARA PODER CONTINUAR CON LOS CALCULOS
            if caso_esp==1:
                dic_f["S"+str(grado-i)][0]=0.000001 #REMPLAXO DEL VALOR CERO POR UN VALOR CASI CERO
                #INFORMACION DE AVISO PARA EL USUARIO DE OCURRENCIA DEL CASO ESPECIAL 1
                print("----------------------------------------------------------------------------------------")
                print("SE HA PRESENTADO UN CASO ESPECIAL PARA LA TABLA DE ROUTH")
                print("EL VALOR DE "+"S^"+str(grado-i)+"[0] = 0 (SE REMPLAZA POR UN VALOR INFINITAMENTE PEQUEÑO)")
                print("PARA EL CASO " + str(grado-i)+"[0] = 0.000001" )
                print("----------------------------------------------------------------------------------------")
            #CASO 2: EL ARREGLO COMPLETO ES NULO POR TANTO SE USA EL POLINOMIO AUXILIAR ANTERIOR
            # SE OPTIENE LA DERIVADA DE ESTE ARREGLO Y SE REMPLAZA PARA CONTINUAR CON LOS CALCULOS   
            if caso_esp>1:
                #CALCULO DE LA DERIVADA DEL ARREGLO ANTERIOR
                dic_f["S"+str(grado-i)]=deriv_casoe(dic_f["S"+str(grado-i+1)],grado-i+1)
                print("----------------------------------------------------------------------------------------")
                print("SE HA PRESENTADO UN CASO ESPECIAL PARA LA TABLA DE ROUTH")
                print("TODOS LOS VALORES DE  "+"S^"+str(grado-i) +" SON IGUALES A CERO")
                print("PARA EL CASO SE REPLAZAN POR LOS VALORES DE LA DERIVADA DE ARRAY "+ "S^"+str(grado-i+1))
                print("S^"+str(grado-i)+" = "+str(dic_f["S"+str(grado-i)]))
                print("----------------------------------------------------------------------------------------")
        ##REINICO DE VARIABLES DE CONTROL
        caso_esp=0
        ceros=0
        #DISMINUCION DE INDICADORES DE ARREGLOS S^N PARA CALCULO DE COEFICIENTES
        i_p-=1
        i_i-=1 
    #***************************************************************************************************************

    #VIZUALIZACION DEL POLINOMIO ELEGIDO PARA EL CALCULO***********************************************************
    print("\n------------------------POLINOMIO:----------------------------- ")
    print("\t  ",end="")
    for i in range(0 ,tam): 
        if grado!=i:
            print(str(polinomio[i])+"S^"+str(grado-i)+" + ",end="")
        else:    
            print(str(polinomio[i])+" = 0")

    #VIZUALIZACION DE LA TABLA DE ROUTH*****************************************************************************
    print("\n------------------------TABLA DE ROUTH : ---------------------\n")
    for i in range(0 ,tam):
        print("\t\t\tS^"+str(grado-i)+" | "+str(dic_f["S"+str(grado-i)]))
    print("\n--------------------------------------------------------------\n")   
    #***************************************************************************************************************
    

#CONDICIONAL PARA LA EJECUCION EXCLUSIVAMENTE DE LA FUNCION PRINCIPAL main()
if __name__ == "__main__":
    main()
    sys.exit(0)