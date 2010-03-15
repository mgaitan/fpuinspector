#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"


extern double PRE_CDECL _get_st0(double val ) POST_CDECL;
extern int PRE_CDECL _fld( double val) POST_CDECL;
extern int PRE_CDECL _fadd( void ) POST_CDECL;
extern double PRE_CDECL _st0_getRegistro( void ) POST_CDECL;

int i;
double get_st0(){
    double val;
    _get_st0(val);
    return val;
}

int fld(double val){
    _fld(val);
    return 0;
}


int fadd(){
    _fadd();
    return 0;
}

//int get_pila(double * pila){
int get_pila(double * pila){
  for(i=0;i<8;i++){
        pila[i]=_st0_getRegistro(); //pop de los registros
        //printf("%f\n", pila[i]);
    }
return 0;
}
