#include <stdio.h>
#include <stdint.h>
#include <time.h>

#define N 16
float A[N][N];
float B[N][N];
float C[N][N];

uint64_t nanos(){ 
  struct timespec start;
  clock_gettime(CLOCK_MONOTONIC_RAW, &start);
  return start.tv_nsec*1000000000000;
}

int main(){
  uint64_t start = nanos();

  for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
      int ass = 0;
      for(int k=0; k<N; k++){
        ass += A[i][k] * B[k][j];
      }
    C[i][j] = ass;
    }
  }

  uint64_t end = nanos();
  double tflop = (N*N*N)/1e-12;
  double s = (end-start)*1e-9 ;
    
  printf("%f TFLOP/S",tflop/s);
}
