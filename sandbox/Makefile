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


all:  libfld.so.1

.asm.o:
	$(AS) $(ASFLAGS) $*.asm
	

fld_w.o: fld_w.c cdecl.h
	$(CC) $(CFLAGS) fld_w.c cdecl.h

libfld.so.1: fld_w.o fld2.o 
	$(LD) $(LDFLAGS) libfld.so.1 -o libfld.so.1.0 *.o


clean :
	rm *.o
	rm *.pyc
