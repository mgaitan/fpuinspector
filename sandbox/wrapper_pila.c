#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"


extern int PRE_CDECL _st0_getRegistro( void ) POST_CDECL;
void PRE_CDECL _fld(double * n) POST_CDECL;


int i;
int get_pila(double * pila){
  for(i=0;i<8;i++){
        pila[i]=_st0_getRegistro(); //pop de los registros
   }
return 0;
}

void fld(double * n){
    _fld(&n);
}
