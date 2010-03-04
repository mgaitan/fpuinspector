;---------- control -------------
segment .bss
control_var resw 1
segment .text
	global _control_getRegistro
_control_getRegistro:
	enter 0,0
	fwait
	fstcw [control_var]	 ;
	mov ax,[control_var]
	fwait
	leave
	ret	

;------------ estado -------------
segment .text
	global _estado_getRegistro
_estado_getRegistro:
	enter 0,0
	fwait
	fstsw ax
	fwait
	leave
	ret
;------------ etiqueta -------------
segment .bss
entornoFPU  resd 2
etiqueta    resd 6

segment .text
	global _etiqueta_getRegistro
_etiqueta_getRegistro:
	enter 0,0
	fwait
	fstenv [entornoFPU]
	mov eax,[etiqueta]	
	leave
	ret


;---------- pila -------------
segment .bss
pila resq 1
segment .text
	global _st0_getRegistro ;ver sto
_st0_getRegistro:
	enter 0,0
	fwait
	fst qword[pila]	;The FST and FSTP instructions copy the value on 
					;the top of the floating point register stack to another 
					;floating point register or to a 32, 64, or 80 bit memory variable
	leave
	ret
	
	
