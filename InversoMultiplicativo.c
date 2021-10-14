#include <stdio.h>
#include <stdlib.h>

int modulo(int x, int mod){
  int r;
  if(x >= 0)
    return x%mod;
  while(x < 0)
    x = x+mod;
  return x;
}

int inversoMultiplicativo(int r0, int r1){
  int r2 = 1,
      q = 0,
      t0 = 0,
      t1 = 1,
      t2 = 0,
      mod = r0;

      int p;

  while(r2 != 0){
    q = r0/r1;
    r2 = r0-(q*r1);

    r0=r1;
    r1=r2;

    if(r2 != 0){
      t2 = modulo(t0-q*t1,mod);
      t0 = t1;
      t1 = t2;
    }
  }
  if(r0 == 1){
    return t2;
  }
  return -1;
}

int main(int argc, char const *argv[]) {
  int r0,
      r1,
      r;

  printf("Escribe dos numero\n");
  scanf("%d",&r0);
  scanf("%d",&r1);
  r = inversoMultiplicativo(r0,r1);
  printf("%d\n",r);
  return 0;
}
