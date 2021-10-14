#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "exponenciacion.h"

int MillerRabin(long int n){
  int k = 0,
      i;
  long int m = n-1,
           a,
           b;

  while (m%2 == 0) {
    m = m/2;
    k++;
  }

  srand(time(NULL));
  a = rand()%(n-1)+1;
  b = exponenciacion(a,m,n);
  if(b == 1){
    return 1;
  }
  for(i = 0; i < k; i++){
    if(b == n-1){
      return 1;
    }
    b = exponenciacion(b,2,n);
  }
  return 0;
}

int main(void) {
  long int n;
  printf("Introduce un número: \n");
  scanf("%ld",&n);
  if(MillerRabin(n)){
    printf("Es primo\n");
  }
  else{
    printf("No es primo\n");
  }

  return 0;
}
