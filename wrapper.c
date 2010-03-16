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

extern void _restore_contexto(int contexto[512]) POST_CDECL;
extern void _save_contexto(int contexto[512]) POST_CDECL;


extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _ffree( int ) POST_CDECL;



extern void PRE_CDECL _fld1( void) POST_CDECL;
extern void PRE_CDECL _fldl2e( void ) POST_CDECL;
extern void PRE_CDECL _fldl2t( void ) POST_CDECL;
extern void PRE_CDECL _fldlg2( void ) POST_CDECL;
extern void PRE_CDECL _fldln2( void ) POST_CDECL;
extern void PRE_CDECL _fldlpi( void ) POST_CDECL;
extern void PRE_CDECL _fldz( void ) POST_CDECL;


extern void PRE_CDECL _finit( void ) POST_CDECL;
extern void PRE_CDECL _fcom (int n) POST_CDECL;
extern void PRE_CDECL _fxch(int n) POST_CDECL;
extern void PRE_CDECL _faddp(int n) POST_CDECL;
extern void PRE_CDECL _fadd( void ) POST_CDECL;
extern void PRE_CDECL _fsubp(int n) POST_CDECL;
extern void PRE_CDECL _fsub( void ) POST_CDECL;
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

//****************** contexto *****************************

int contexto[512];
void restore_contexto(){
    _restore_contexto(contexto);
}

void save_contexto(){
    _save_contexto(contexto);
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
  //save_contexto();
  for(i=0;i<8;i++){
        pila[i]=_get_pila(); //pop de los registros
        //printf("%f\n", pila[i]);
    }
    //restore_contexto();
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
    //restore_contexto();
    _fld(val);
    //save_contexto();
}

void fld1(){ _fld1();}
void fldl2e(){ _fldl2e();}
void fldl2t(){ _fldl2t();}
void fldlg2(){ _fldlg2();}
void fldln2(){ _fldln2();}
void fldpi(){ _fldpi();}
void fldz(){ _fldz();}




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

void fsub(){
    _fsub();
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




