import torch 
import time
import os 

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
size = (1024, 1024, 1024) # 4GB for tensor with float32]

## without pinned memory
cpu_tensor = torch.randn(size)
gpu_tensor = torch.empty(size, device= "cuda")
cpu_tensor_pinned = torch.randn(size, pin_memory=True)


# measure time without pinned memory
start_time = time.time()
gpu_tensor.copy_(cpu_tensor)
time_without_pinned_memory = time.time() - start_time
print(f"time without pinned memory: {time_without_pinned_memory:.4f} seconds")

# measure time with pinned memory
start_time = time.time()
gpu_tensor.copy_(cpu_tensor_pinned)
time_with_pinned_memory = time.time() - start_time
print(f"time with pinned memory: {time_with_pinned_memory:.4f} seconds")

#comparison
print(f"speedup: {time_without_pinned_memory/time_with_pinned_memory:.2f}x")