import numpy as np
import time

if __name__ == "__main__":
    N = 2048
    A = np.random.randn(N,N).astype(np.float32)
    B = np.random.randn(N,N).astype(np.float32)    

    tik = time.monotonic()
    C = A@B
    tok = time.monotonic()


    ## matrix multiplication takes n^3 flop for a square matrix
    ## lets say we need to find C<ij> = <k>SUMATION<0,N>A<ik>B<kj>
    s = tok-tik
    print(f"{(N**3/s):.2f} FLOPS")

    ## G stands for GIGA and FLOPS stands for floating point operations per sec
    print(f"{(((N**3)/1e12)/s):.2f} GFLOPS")



