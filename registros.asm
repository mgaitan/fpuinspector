;---------- control -------------
segment .bss
control_var resw 1
segment .text
    global _control_getRegistro
_control_getRegistro:
    enter 0,0
    fwait
    ;FSTCW stores the FPU control word (governing things like the 
    ;rounding mode, the precision, and the exception masks) 
    ;into a 2-byte memory area
    fstcw [control_var] 
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
    fstsw ax ;FSTSW stores the FPU status word into AX or into a 2-byte memory area.
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
    
    ;FSTENV stores the FPU operating environment (control word, status 
    ;word, tag word, instruction pointer, data pointer and last opcode) 
    ;into memory. The memory area is 14 or 28 bytes long, depending on 
    ;the CPU mode at the time.
    fstenv [entornoFPU]
    
    mov eax,[etiqueta]  ;return
    leave
    ret


;---------- pila -------------
segment .bss
pila resq 1
segment .text
    global _st0_getRegistro
_st0_getRegistro:
    enter 0,0
    fwait
    ;The FST and FSTP instructions copy the value on 
    ;the top of the floating point register stack to another 
    ;floating point register or to a 32, 64, or 80 bit memory variable
    fst qword[pila] 
    leave
    ret
    
    
