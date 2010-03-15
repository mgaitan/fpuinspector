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


all:  libfpu.so.1

.asm.o:
	$(AS) $(ASFLAGS) $*.asm
	
wrapper.o: wrapper.c cdecl.h
	$(CC) $(CFLAGS) wrapper.c

libfpu.so.1: wrapper.o registros.o instrucciones.o
	$(LD) $(LDFLAGS) libfpu.so.1 -o libfpu.so.1.0 wrapper.o registros.o instrucciones.o

clean :
	rm *.o
	rm *.pyc
