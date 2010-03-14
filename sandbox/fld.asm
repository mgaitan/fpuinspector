; nasm -f elf myprog.asm
; ld -o myprog myprog.o -I/lib/ld-linux.so.2 -lc


global _start

    extern scanf
    extern printf

section .data
fmt1 db "%lf", 0
fmt2 db 10, "The number is: %f", 10, 0

section .text
_start:

    nop
    call getfloat
    call getfloat
    call _fadd
    call putfloat
    call putfloat
exit:
    xor ebx, ebx
    mov eax, 1
    int 80h
;----------

;----------
getfloat:
    push ebp
    mov ebp, esp
    sub esp, 8
    lea eax, [ebp - 8]
    push eax
    push fmt1
    call scanf
    add esp, 8

; (probably be a good idea to check the return from scanf here, before
; proceeding...)

    fld qword [ebp - 8]
    mov esp, ebp
    pop ebp
    ret
;-----------

;------------
putfloat:
    push ebp
    mov ebp, esp
    sub esp, 8
    fstp qword [ebp - 8]
    push fmt2
    call printf
    add esp, 12

    mov esp, ebp
    pop ebp
    ret
;-------------
_fadd:
    fadd
    ret
