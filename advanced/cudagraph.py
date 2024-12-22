import torch
import time

# Parameters
N, D_in, D_out = 128, 1024, 512  # Batch size, input dimension, output dimension
device = torch.device("cuda")

# Initialize tensors
x = torch.randn(N, D_in, device=device)
w = torch.randn(D_in, D_out, device=device)
b = torch.randn(D_out, device=device)
y = torch.empty(N, D_out, device=device)

# Warm-up
y = x @ w + b
torch.cuda.synchronize()

# Without CUDA Graphs
start = time.time()
for _ in range(10000):  # Run for 1000 iterations
    y = x @ w + b
torch.cuda.synchronize()
end = time.time()
time_without_cudagraph = end - start

# With CUDA Graphs
# Create a CUDA graph
static_x = torch.randn_like(x)
static_y = torch.empty_like(y)
graph = torch.cuda.CUDAGraph()

# Capture the graph
with torch.cuda.graph(graph):
    static_y = static_x @ w + b

# Replay the graph
start = time.time()
for _ in range(1000):  # Run for 1000 iterations
    static_x.copy_(x)  # Update static input
    graph.replay()
torch.cuda.synchronize()
end = time.time()
time_with_cudagraph = end - start

# Print results
print(f"Time without CUDA Graphs: {time_without_cudagraph:.6f} seconds")
print(f"Time with CUDA Graphs: {time_with_cudagraph:.6f} seconds")
print(f"Speedup: {time_without_cudagraph / time_with_cudagraph:.2f}x")