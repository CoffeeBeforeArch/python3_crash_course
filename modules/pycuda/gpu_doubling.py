# This program doubles the elements of a numpy array on the GPU
# By: Nick from CoffeeBeforeArch

# Import and initialize pycuda
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

import numpy as np

# Create a matrix of random numbers and set it to be
# 32-bit floats
a = np.random.randn(16)
a = a.astype(np.float32)

# Allocate space on the GPU
a_gpu = cuda.mem_alloc(a.nbytes)

# Transfer the data to the GPU
cuda.memcpy_htod(a_gpu, a)

# Write our GPU kernel inside of our script
module = SourceModule("""
        __global__ void double_array(float *a){
            int idx = blockIdx.x * blockDim.x + threadIdx.x;
            a[idx] *= 2;
        }
        """)

# Launch the kernel
function = module.get_function("double_array")
function(a_gpu, block=(16, 1, 1), grid=(1, 1, 1))

# Place holder for the result
a_doubled = np.empty_like(a)

# Copy the result back from the GPU
cuda.memcpy_dtoh(a_doubled, a_gpu)

# Print the original and result
print(a)
print(a_doubled)

