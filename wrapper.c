#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"


//*********** registros.asm header *******************
extern int PRE_CDECL _get_control( void ) POST_CDECL;
extern int PRE_CDECL _get_estado( void ) POST_CDECL;
extern int PRE_CDECL _get_etiqueta( void ) POST_CDECL; //TODO: ver tamaño de dato de retorno (6x4 bytes?)
extern double PRE_CDECL _get_pila( void ) POST_CDECL;

//************ intrucciones.asm header ***************
extern  void PRE_CDECL _reset( void ) POST_CDECL;
extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _ffree( int ) POST_CDECL;
extern void PRE_CDECL _fld( double ) POST_CDECL;
extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _fcom (int n) POST_CDECL;
extern void PRE_CDECL _fxch(int n) POST_CDECL;
extern void PRE_CDECL _faddp(int n) POST_CDECL;
extern void PRE_CDECL _fadd( void ) POST_CDECL;
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
    return _get_control();
}

long get_estado(){
    return _get_estado();
}

long get_etiqueta(){
    return _get_etiqueta();
}

int get_pila(double * pila){
  int i;
  for(i=0;i<8;i++){
        pila[i]=_get_pila(); //pop de los registros
        //printf("%f\n", pila[i]);
    }
return 0;
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

void fld(double val){
    _fld(val);
}

void fcom(int n){
    _fcom(n);
}

void fxch(int n){
    _fxch(n);
}

void fadd(){
    _fadd();
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




