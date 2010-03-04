;------------ Reset -----------
segment .text
		global _reset
_reset:
	enter 0,0
	emms
	;finit
	fldz
	mov eax,[ebp+8]
	fsave [eax]	
	fwait	
	leave
	ret
;--------- Set-Get Contexto -----------
	global _setContexto
_setContexto:
	enter 0,0
	mov eax,[ebp+8]		
	emms	
	finit	
	fwait
	frstor [eax]
	fwait
	leave
	ret
	
	global _getContexto
_getContexto:
	enter 0,0
	fwait
	mov eax,[ebp+8]
	fsave [eax]
	fwait
	leave
	ret
;------------ FINIT -------------
segment .text
	global _fpu_finit
_fpu_finit:
	finit	
	ret
;------------ FFREE -------------
segment .data
salto_ffree dd ffree0,ffree1,ffree2,ffree3,ffree4,ffree5,ffree6,ffree7
segment .text
	global _fpu_ffree
_fpu_ffree:
	enter 0,0
	pusha
	mov eax,[ebp + 8] ; cargo en num de registro
	shl eax, 2 ;multimplico por 4
	jmp [salto_ffree+eax]	
ffree0:	
	ffree st0
	jmp fin_ffree
ffree1:	
	ffree st1
	jmp fin_ffree
ffree2:	
	ffree st2
	jmp fin_ffree
ffree3:	
	ffree st3
	jmp fin_ffree
ffree4:	
	ffree st4
	jmp fin_ffree
ffree5:	
	ffree st5
	jmp fin_ffree
ffree6:	
	ffree st6
	jmp fin_ffree
ffree7:	
	ffree st7
	
fin_ffree:		
	popa
	leave		
	ret
;------------ FLD -------------
segment .bss
valor resq 1
segment .text
	global _fpu_fld
_fpu_fld:
	enter 0,0
	pusha
	mov eax,[ebp + 8]
	fld qword[eax]	
	fwait	
	popa
	leave		
	ret	
;------------ FCOM -------------
segment .data
salto_fcom dd fcom0,fcom1,fcom2,fcom3,fcom4,fcom5,fcom6,fcom7
segment .text
	global _fpu_fcom
_fpu_fcom:
	enter 0,0
	pusha
	mov eax,[ebp + 8] ; cargo en num de registro
	shl eax, 2 ;multimplico por 4
	jmp [salto_fcom+eax]	
fcom0:	
	fcom st0
	jmp fin_fcom
fcom1:	
	fcom st1
	jmp fin_fcom
fcom2:	
	fcom st2
	jmp fin_fcom
fcom3:	
	fcom st3
	jmp fin_fcom
fcom4:	
	fcom st4
	jmp fin_fcom
fcom5:	
	fcom st5
	jmp fin_fcom
fcom6:	
	fcom st6
	jmp fin_fcom
fcom7:	
	fcom st7	
fin_fcom:		
	popa
	leave		
	ret
;------------ FXCH -------------
segment .data
salto_fxch dd fxch0,fxch1,fxch2,fxch3,fxch4,fxch5,fxch6,fxch7
segment .text
	global _fpu_fxch
_fpu_fxch:
	enter 0,0
	pusha
	mov eax,[ebp + 8] ; cargo en num de registro
	shl eax, 2 ;multimplico por 4
	jmp [salto_fxch+eax]	
fxch0:	
	fxch st0
	jmp fin_fxch
fxch1:	
	fxch st1
	jmp fin_fxch
fxch2:	
	fxch st2
	jmp fin_fxch
fxch3:	
	fxch st3
	jmp fin_fxch
fxch4:	
	fxch st4
	jmp fin_fxch
fxch5:	
	fxch st5
	jmp fin_fxch
fxch6:	
	fxch st6
	jmp fin_fxch
fxch7:	
	fxch st7	
fin_fxch:		
	popa
	leave		
	ret
;------------ FADDP -------------
segment .data
salto_faddp dd faddp0,faddp1,faddp2,faddp3,faddp4,faddp5,faddp6,faddp7
segment .text
	global _fpu_faddp
_fpu_faddp:
	enter 0,0
	pusha
	mov eax,[ebp + 8] ; cargo en num de registro
	shl eax, 2 ;multimplico por 4
	jmp [salto_faddp+eax]	
faddp0:	
	faddp st0
	jmp fin_faddp
faddp1:	
	faddp st1
	jmp fin_faddp
faddp2:	
	faddp st2
	jmp fin_faddp
faddp3:	
	faddp st3
	jmp fin_faddp
faddp4:	
	faddp st4
	jmp fin_faddp
faddp5:	
	faddp st5
	jmp fin_faddp
faddp6:	
	faddp st6
	jmp fin_faddp
faddp7:	
	faddp st7	
fin_faddp:		
	popa
	leave		
	ret	
;------------ FSUBP -------------
segment .data
salto_fsubp dd fsubp0,fsubp1,fsubp2,fsubp3,fsubp4,fsubp5,fsubp6,fsubp7
segment .text
	global _fpu_fsubp
_fpu_fsubp:
	enter 0,0
	pusha
	mov eax,[ebp + 8] ; cargo en num de registro
	shl eax, 2 ;multimplico por 4
	jmp [salto_fsubp+eax]	
fsubp0:	
	fsubp st0
	jmp fin_fsubp
fsubp1:	
	fsubp st1
	jmp fin_fsubp
fsubp2:	
	fsubp st2
	jmp fin_fsubp
fsubp3:	
	fsubp st3
	jmp fin_fsubp
fsubp4:	
	fsubp st4
	jmp fin_fsubp
fsubp5:	
	fsubp st5
	jmp fin_fsubp
fsubp6:	
	fsubp st6
	jmp fin_fsubp
fsubp7:	
	fsubp st7	
fin_fsubp:		
	popa
	leave		
	ret
;------------ FSINCOS -------------
segment .text
	global _fpu_fsincos
_fpu_fsincos:
	fsincos	
	ret	
;------------ FYL2X -------------
segment .text
	global _fpu_fyl2x
_fpu_fyl2x:
	fyl2x	
	ret	
;------------ FSQRT -------------
segment .text
	global _fpu_fsqrt
_fpu_fsqrt:
	fsqrt	
	ret	
