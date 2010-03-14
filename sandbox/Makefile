#
# Linux makefile
# Use with make 
#

.SUFFIXES: .o .asm .c

AS=nasm 
ASFLAGS = -f elf
CC=gcc
CFLAGS= -fPIC -c
LD=ld 
LDFLAGS= -shared -soname


all:  libpila.so.1

.asm.o:
	$(AS) $(ASFLAGS) $*.asm
	

wrapper_pila.o: wrapper_pila.c cdecl.h
	$(CC) $(CFLAGS) wrapper_pila.c

libpila.so.1: wrapper_pila.o registros.o instrucciones.o
	$(LD) $(LDFLAGS) libpila.so.1 -o libpila.so.1.0 wrapper_pila.o registros.o instrucciones.o


clean :
	rm *.o
	rm *.pyc
