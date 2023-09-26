# from clockdeco import clock
# from clock import clockdeco
import sys

# In VSCode environment, "." represent the root directory of the project.
sys.path.append('./09-closure-deco')

# import clock decorator function from clockdeco module of clock sub directory
from clock.clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))

