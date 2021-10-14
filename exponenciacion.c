#include <stdlib.h>
#include <stdio.h>

long int exponenciacion(long int x, long int a, long int n){
  int i,
      l = 0;
  short int bin[100];
  long int z = 1;

  for(i = 0; a > 0; i++){
    bin[i] = a%2;
    a = a/2;
    l++;
  }

  for(i = l-1; i >= 0; i--){
    z = (z*z) % n;
    if(bin[i] == 1)
      z = (z*x) % n;
  }

  return z;
}
