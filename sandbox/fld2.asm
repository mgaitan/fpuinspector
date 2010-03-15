; nasm -f elf myprog.asm
; ld -o myprog myprog.o -I/lib/ld-linux.so.2 -lc

global _start

        extern printf


section .data

fmt2 db 10, "The number is: %f", 10, 0





section .text
    global _fld
;----------
_fld:
    fld qword [ebp + 8]
    ret
;-----------

;------------
section .text
    global _get_st0
_get_st0:
    ;push ebp
    ;mov ebp, esp
    ;sub esp, 8
    fstp qword [ebp - 8]
    ;push fmt2
    ;call printf
    ;add esp, 12

    ;mov esp, ebp
    ;pop ebp
    
    ret
;-------------
section .text
    global _fadd
_fadd:
    fadd
    ret


;---------- pila -------------
segment .bss
pila resq 1     ;reserve a 64-bit word
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
