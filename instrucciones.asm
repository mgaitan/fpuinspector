;------------ Reset -----------
segment .text
        global _reset
_reset:
    enter 0,0
    ;EMMS sets the FPU tag word (marking which floating-point registers 
    ;are available) to all ones, meaning all registers are available for 
    ;the FPU to use. It should be used after executing MMX instructions 
    ;and before executing any subsequent floating-point operations.
    emms
    fldz   ;fld 0
    mov eax,[ebp+8] 
    ;FSAVE saves the entire floating-point unit state, 
    ;including all the information saved by FSTENV (Section A.65) plus 
    ;the contents of all the registers, to a 94 or 108 byte area of memory 
    ;(depending on the CPU mode). FRSTOR  restores the floating-point 
    ;state from the same area of memory.
    fsave [eax] 
    fwait   
    leave
    ret
;--------- Set-Get Contexto -----------
    global _restore_contexto
_restore_contexto:
    enter 0,0
    mov eax,[ebp+8]     
    emms    
    finit   
    fwait
    frstor [eax]    ;FRSTOR  restores the floating-point state from memory
    fwait
    leave
    ret
    
    global _save_contexto
_save_contexto:
    enter 0,0
    fwait
    mov eax,[ebp+8]
    fsave [eax] ;saves the entire floating-point unit state
    fwait
    leave
    ret
;------------ FINIT -------------
segment .text
    global _finit
_finit:
    ;initialises the FPU to its default state. It flags all registers as empty, 
    ;though it does not actually change their values. 
    finit  
    ret
;------------ FFREE -------------
segment .data
salto_ffree dd ffree0,ffree1,ffree2,ffree3,ffree4,ffree5,ffree6,ffree7
segment .text
    global _ffree
_ffree:
    ;FFREE marks the given register as being empty.
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
;segment .bss
;    valor resq 1

segment .text    
    global _fld
_fld:
    ;loads a floating-point value out of the given register or memory 
    ;location, and pushes it on the FPU register stack
    ;enter 0,0
    ;pusha
    ;mov eax, [ebp + 8]
    fld qword [ebp + 8] ; [ebp + 8]
    ;fwait   
    ;popa
    ;leave
    ret      

;---------------FLDxx-------------
;These instructions push specific 
;standard constants on the FPU register stack. 
;FLD1 pushes the value 1; 
;FLDL2E pushes the base-2 logarithm of e; 
;FLDL2T pushes the base-2 log of 10; 
;FLDLG2 pushes the base-10 log of 2; 
;FLDLN2 pushes the base-e log of 2; 
;FLDPI pushes pi; and FLDZ pushes zero. 

segment .text    
    global _fldz
_fldz:
    fldz
    ret
segment .text    
    global _fld1
_fld1:
    fld1
    ret
segment .text    
    global _fldl2e
_fldl2e:
    fldl2e
    ret
segment .text    
    global _fldl2t
_fldl2t:
    fldl2t
    ret
segment .text    
    global _fldlg2
_fldlg2:
    fldlg2
    ret
segment .text    
    global _fldln2
_fldln2:
    fldln2
    ret
segment .text    
    global _fldpi
_fldpi:
    fldpi
    ret


;------- FLDCW: Load Floating-Point Control Word
segment .text    
    global _fldcw
_fldcw:
    fldcw word[ebp + 2] ; 
    ret


     
;------------ FCOM -------------
segment .data
salto_fcom dd fcom0,fcom1,fcom2,fcom3,fcom4,fcom5,fcom6,fcom7
segment .text
    global _fcom
_fcom:
    ;FCOM compares ST0 with the given operand, and sets the FPU flags 
    ;accordingly. ST0 is treated as the left-hand side of the comparison, 
    ;so that the carry flag is set (for a "less-than"  result) 
    ;if ST0 is less than the given operand.    
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
    global _fxch
_fxch:
    ;FXCH exchanges ST0 with a given FPU register. 
    ;The no-operand form exchanges ST0 with ST1.
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


;------ FCHS -------
section .text
    global _fchs
_fchs:
    fchs
    ret

;------ FABS -------
section .text
    global _fabs
_fabs:
    fabs
    ret

;----- FCLEX, {FNCLEX}: Clear Floating-Point Exceptions
section .text
    global _fclex
_fclex:
    fclex
    ret


;------ FADD -------
section .text
    global _fadd
_fadd:
    fadd
    ret

;------ FSUB -------
section .text
    global _fsub
_fsub:
    fsub
    ret

;------ FMUL -------
section .text
    global _fmul
_fmul:
    ;FMUL multiplies ST0 by the given operand, and stores the result in ST0
    fmul
    ret


;------ FDIV -------
section .text
    global _fdiv
_fdiv:
    ;FDIV divides ST0 by the given operand and stores the result back in ST0
    fdiv
    ret

;------ FPREM Floating-Point Partial Remainder
section .text
    global _fprem
_fprem:
    ;produce the remainder obtained by dividing ST0 by ST1.
    fprem
    ret

;------ FSCALE Scale Floating-Point Value by Power of Two
section .text
    global _fscale
_fscale:
    ;FSCALE scales a number by a power of two: it rounds ST1 towards zero 
    ;to obtain an integer, then multiplies ST0 by two to the power of that 
    ;integer, and stores the result in ST0. 
    fscale
    ret

;------ FXTRACT Extract Exponent and Significand
section .text
    global _fxtract
_fxtract:
    fxtract
    ret



;------------ FSIN -------------
segment .text
    global _fsin
_fsin:
    ;FSINCOS does the same, but then pushes the cosine of the same value 
    ;on the register stack, so that the sine ends up in ST1 and the cosine in ST0.
    fsin 
    ret 

;------------ FCOS -------------
segment .text
    global _fcos
_fcos:
    ;FSINCOS does the same, but then pushes the cosine of the same value 
    ;on the register stack, so that the sine ends up in ST1 and the cosine in ST0.
    fcos 
    ret 


;------------ FSINCOS -------------
segment .text
    global _fsincos
_fsincos:
    ;FSINCOS does the same as FSIN, but then pushes the cosine of the same value 
    ;on the register stack, so that the sine ends up in ST1 and the cosine in ST0.
    fsincos 
    ret 

;------------ FPTAN
segment .text
    global _fptan
_fptan:
    ;FPTAN computes the tangent of the value in ST0 (in radians), and stores the result back into ST0. 
    fptan 
    ret 


;------------ FPTAN
segment .text
    global _fpatan
_fpatan:
    ;FPTAN computes the tangent of the value in ST0 (in radians), and stores the result back into ST0. 
    fpatan 
    ret 


;--------FRNDINT
segment .text
    global _frndint
_frndint:
    ;FRNDINT rounds the contents of ST0 to an integer, according to the current 
    ;rounding mode set in the FPU control word, and stores the result back in ST0.
    frndint
    ret


;------------ FYL2X -------------
segment .text
    global _fyl2x
_fyl2x:
    ;FYL2X multiplies ST1 by the base-2 logarithm of ST0, stores the result in ST1, and pops the register stack (so that the result ends up in ST0). ST0 must be non-zero and positive.
    fyl2x   
    ret 
;------------ FSQRT -------------
segment .text
    global _fsqrt
_fsqrt:
    ;FSQRT calculates the square root of ST0 and stores the result in ST0.
    fsqrt   
    ret 
