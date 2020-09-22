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
#OBJETIVO DEL PROGRAMA: PUNTO No 3:                                        # 
# implementar un algoritmo  en ASM para ARM raspberry					   #
# que permita el calculo de n numeros  de								   #
# fibonacci, n es ingresado por teclado                                    #     
############################################################################
#COMENTARIOS:               					                           #                    
#ejecutar en raspberry													   #
#sudo as -o punto3.o punto3.s											   #
#sudo gcc punto3.s -o punto3											   #	
#./punto2                                                                  #
#----------------------------inicio de programa---------------------------*/

.data
/*datos en memoria*/
.balign 4        			
n_fib: .word 0					@CANTIDAD DE NUMEROS FIBONACCI A CALCULAR

/*MENSAJES DE USUARIO*/
mens_i: .asciz "INGRESE LA CANTIDAD DE NUMEROS FIB A CALCULAR: "
mens_a: .asciz "CALCULANDO %d NUMEROS DE FIBONACCI:... \n"
mens_f: .asciz "-- %d \n"
mens_sc: .asciz "%d"

.text
/*INICIO DEL PROGRAMA PRINCIPAL*/
.global main

main: PUSH {R4,LR} 	@ALMACENAMIENTO DE REGISTROS DEL SISTEMA
	/*MENSAJE DE INICIO */
	LDR R0,=mens_i
	BL  printf
	/*ADQUISICION DE DATO CANRIDAD DE NUMEROS FIBONACCI */
	LDR R0,=mens_sc
	LDR R1,dir_n_fib
	BL scanf
	/*MENSAJE DE CONFIRMACION PARA EL USUARIO */
	LDR R0,=mens_a
	LDR R1,dir_n_fib
	LDR R1,[R1]
	BL  printf
	/*IMPRESION DEL PRIMER NUMERO FIBONACCI=0*/
	MOV R1,#0
	LDR R0,=mens_f
	BL printf
	/*CARGA DEL NUMERO INGRESADO POR EL USUARIO AL REGISTRO R3 */
	LDR R1,dir_n_fib
	LDR R3,[R1]
	SUB R3,R3,#2 				@SE RESTAN 2 PUESTO QUE UN NUMERO YA HA SIDO INGRESADO Y EL BUCLE CUENTA DESDE CERO
	/*INICIALIZACION DE REGISTROS DE CALCULO R2+R5=R5*/
	MOV  R2,#0
	MOV  R1,#1
	MOV R5,#1
	/*INICIO DE BUCLE DE SERIE DE FIBONACCI*/
LOOP:
	/*CALCULO DE VALOR FIBONACCI*/
	ADD R5, R2,R5				@R2+R5=R5	
	MOV R2,R1					@R2<=R1 CARGA EL ULTIMO VALOR DE LA SERIE A R2
	MOV R1,R5					@R1<=R5 CARGA EL RESULTADO A R1 PARA VISUALIZACION	
	PUSH {R1,R2,R3,R5}			@GUARDA LOS REGISTROS PARA EVITAR CONFLICTOS
	/*IMPRESION DEL PRIMER NUMERO FIBONACCI = R1*/
	LDR R0,=mens_f
	BL printf
	/*SE SACAN LOS VALORES GUSRDADOS*/
	POP {R1,R2,R3,R5}
	MOV R5,R1					@GUARDA EL VALOR DE RESULTADO EN R5 PARA NUEVO CALCULO
	/*CONTROL DE BUCLE*/
	SUB R3,R3,#1				@RESTA 1 A R3 Y GUARDA EN R3 R3<=r3-1
	CMP R3,#0					@COMPARA CON CERO
	BGE LOOP					@SALTA SI NO ES CERO
	/*FINAL DE PROGRAMA*/
end:
	POP {R4,LR}
	BX LR
/*APUNTADOR DE VARIABLE CANTIDAD DE NUMEROS FIB*/
dir_n_fib: .word n_fib
/*INCLUSION DE FUNCIONES PRINTF Y SCANF*/
.global printf
.global scanf
