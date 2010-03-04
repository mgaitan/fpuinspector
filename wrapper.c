#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"

int PRE_CDECL _control_getRegistro( void ) POST_CDECL;
int PRE_CDECL _estado_getRegistro( void ) POST_CDECL;
float PRE_CDECL _st0_getRegistro( void ) POST_CDECL;

//intrucciones.asm header
void PRE_CDECL _fpu_finit( void ) POST_CDECL;
void PRE_CDECL _fpu_ffree( int ) POST_CDECL;
void PRE_CDECL _fpu_fld( int ) POST_CDECL;
void PRE_CDECL _finit( void ) POST_CDECL;


 
//cuando python carga es biblioteca ejecuta _init() automaticamente
//puede usarse para inicializar variables u otros procedimientos
void _init() {}
 
//idem _init pero al terminar el programa 
void _fini() {}
 
int getControl(){
	return _control_getRegistro();
}

int getEstado(){
	return _estado_getRegistro();
}

int getSt0(){
	return _st0_getRegistro();
}

void fpuFfree(int n){
	_fpu_ffree(n);
}

void fpuFld(int n){
	_fpu_fld(n);
}

void fpuInit(){
	_fpu_finit();
}




