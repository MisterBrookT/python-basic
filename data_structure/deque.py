from collections import deque
from time import  time
from typing import List, Deque

# Simple use case of deque
# detail about deque can be found in https://docs.python.org/3/library/collections.html#collections.deque
# high-level speak, it is a double-ended queue, and 
# it supports efficient double-end append and pop. (O(1)),
# while insert and pop from left side for list object is O(n)  
def demonstrate_deque() -> None:
    # create a deque
    dq: Deque[int] = deque()
    # append elements to the right
    dq.append(1)
    dq.append(2)
    dq.append(3)
    # append elements to the left
    dq.appendleft(4)
    dq.appendleft(5)
    dq.appendleft(6)
    # print the deque
    print(dq)
    # pop elements from the right
    print(dq.pop())
    print(dq.pop())
    print(dq.pop())
    # pop elements from the left
    print(dq.popleft())
    print(dq.popleft())
    print(dq.popleft())
    print(dq)

# compare deque and list performance
def compare_speed() -> None:
    num_opr = 2*10**5

    dq: Deque[int] = deque()
    lst: List[int] = []
    # test append
    start_time = time()
    for i in range(num_opr):
        dq.append(i)
    print(f"deque append: {time() - start_time:.4f} seconds")
    
    start_time = time()
    for i in range(num_opr):
        lst.append(i)
    print(f"list append: {time() - start_time:.4f} seconds")

    # test pop
    start_time = time()
    for i in range(num_opr):
        dq.pop()
    print(f"deque pop: {time() - start_time:.4f} seconds")

    start_time = time()
    for i in range(num_opr):
        lst.pop()
    print(f"list pop: {time() - start_time:.4f} seconds")

    # test insert
    start_time = time()
    for i in range(num_opr):
        dq.appendleft(i)
    print(f"deque appendleft: {time() - start_time:.4f} seconds")

    start_time = time()
    for i in range(num_opr):
        lst.insert(0, i)    
    print(f"list insert: {time() - start_time:.4f} seconds")

    # test popleft
    start_time = time()
    for i in range(num_opr):
        dq.popleft()
    print(f"deque popleft: {time() - start_time:.4f} seconds")

    start_time = time()
    for i in range(num_opr):
        lst.pop(0)
    print(f"list pop(0): {time() - start_time:.4f} seconds")


    
# main function
def main() -> None:
    # demonstrate deque
    print("Demonstrating deque usage:") 
    demonstrate_deque()
    # compare speed
    print("\nCompare speed between deque and list:")
    compare_speed()
if __name__ == "__main__":
    main()