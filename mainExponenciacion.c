#include <stdlib.h>
#include <stdio.h>
#include "exponenciacion.h"

int main(void){
  long int x,
           a,
           m,
           r;
  printf("Escriba el número x\n");
  scanf("%ld",&x);
  printf("Escriba el número a\n");
  scanf("%ld",&a);
  printf("Escriba el número m\n");
  scanf("%ld",&m);
  r = exponenciacion(x,a,m);
  printf("El resultado es: %ld\n",r);
}
