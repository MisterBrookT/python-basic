import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.multiprocessing as mp
import os
import numpy as np

#todo: (yinghao) 1) add more examples 2) figure out the underlying principle of primitives in distributed ml
def setup(rank, world_size):
    # Initialize the distributed environment.
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(rank)

def cleanup():
    dist.destroy_process_group()

def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    np.random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def demo_basic(rank, world_size):
    setup(rank, world_size)
    set_seed(42+rank)  # Ensure different seed for each rank

    # Simple model
    model = torch.nn.Linear(2, 2).cuda(rank)
    model = DDP(model, device_ids=[rank])

    # Simple input tensor
    input = torch.randn(3, 2).cuda(rank)

    # Forward pass
    output = model(input)
    
    # Example of all-reduce using NCCL
    print(f"Rank {rank}, Before All-Reduce,  Output Tensor: {output}")
    dist.all_reduce(output, op=dist.ReduceOp.SUM)
    print(f"Rank {rank}, After All-Reduce,  Output Tensor: {output}")

    # sync between gpus
    dist.barrier()

    # Example of broadcast using NCCL
    if rank == 0:
        tensor = torch.randn(2).cuda(rank)
    else:
        tensor = torch.zeros(2).cuda(rank)
    print(f"Rank {rank}, Before BroadCast, Tensor: {tensor}")
    dist.broadcast(tensor, src=0)
    print(f"Rank {rank}, After Broadcast, Tensor: {tensor}")

    # sync between gpus
    dist.barrier()

    # Example of scatter using NCCL
    if rank == 0:
        scatter_list = [torch.randn(2).cuda(rank) for _ in range(world_size)]
    else:
        scatter_list = [torch.zeros(2).cuda(rank) for _ in range(world_size)]
    scatter_tensor = torch.zeros(2).cuda(rank)
    print(f"Rank {rank}, Before Scatter, Tensor: {scatter_tensor}, scatter_list: {scatter_list}")
    dist.scatter(scatter_tensor, scatter_list if rank == 0 else [], src=0)
    print(f"Rank {rank}, After Scatter, Tensor: {scatter_tensor}")

    cleanup()

def main():
    world_size = 2  # Two GPUs in this example
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    mp.spawn(demo_basic, args=(world_size,), nprocs=world_size, join=True)

if __name__ == "__main__":
    main()

