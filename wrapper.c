#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"


//*********** registros.asm header *******************
extern long PRE_CDECL _control_getRegistro( void ) POST_CDECL;
extern long PRE_CDECL _estado_getRegistro( void ) POST_CDECL;
extern long PRE_CDECL _etiqueta_getRegistro( void ) POST_CDECL; //TODO: ver tamaño de dato de retorno (6x4 bytes?)
extern float PRE_CDECL _st0_getRegistro( void ) POST_CDECL;

//************ intrucciones.asm header ***************
extern  void PRE_CDECL _reset( void ) POST_CDECL;
extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _ffree( int ) POST_CDECL;
extern void PRE_CDECL _fld( float ) POST_CDECL;
extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _fcom (int n) POST_CDECL;
extern void PRE_CDECL _fxch(int n) POST_CDECL;
extern void PRE_CDECL _faddp(int n) POST_CDECL;
extern void PRE_CDECL _fsubp(int n) POST_CDECL;
extern void PRE_CDECL _fsincos(void) POST_CDECL;
extern void PRE_CDECL _fyl2x(void) POST_CDECL;
extern void PRE_CDECL _fsqrt(void) POST_CDECL;

//********* inicializador y destructor ****************
void _init() {
    //cuando python carga es biblioteca ejecuta _init() automaticamente
    //puede usarse para inicializar variables u otros procedimientos
}
void _fini() {
    //idem _init pero al terminar el programa 
}
 

//*********** Wrapper para rutinas de registros.asm ********

long get_control(){
    return _control_getRegistro();
}

long get_estado(){
    return _estado_getRegistro();
}

long get_etiqueta(){
    return _etiqueta_getRegistro();
}

float get_st0(){
    return _st0_getRegistro();
}


// ********* wrappers a rutinas de FPU (instrucciones.asm) *********
void reset(void){
    _reset();
}

void finit(){
    _finit();
}

void ffree(int n){
    _ffree(n);
}

void fld(float n){
    _fld(n);
}

void fcom(int n){
    _fcom(n);
}

void fxch(int n){
    _fxch(n);
}

void faddp(int n){
    _faddp(n);
}

void fsubp(int n){
    _fsubp(n);
}

void fsincos(){
    _fsincos();
}

void fyl2x(){
    _fyl2x();
}

void fsqrt(){
    _fsqrt();
}




