# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_THREAD_TOP[]
import itertools
import time
from threading import Thread, Event

import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: 
        return False
    
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

def spin(msg: str, done: Event) -> None:  # <1>
    for char in itertools.cycle(r'\|/-'):  # <2>
        status = f'\r{char} {msg}'  # <3>
        print(status, end='', flush=True)
        if done.wait(.1):  # <4>
            break  # <5>
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # <6>

def slow() -> int:
    # time.sleep(3)  # <7>
    is_prime(5_000_111_000_222_021)
    return 42
# end::SPINNER_THREAD_TOP[]

# tag::SPINNER_THREAD_REST[]
def supervisor() -> int:  # <1>
    done = Event()  # <2>
    spinner = Thread(target=spin, args=('thinking!', done))  # <3>
    print(f'spinner object: {spinner}')  # <4>
    spinner.start()  # <5>
    result = slow()  # <6>
    done.set()  # <7>
    spinner.join()  # <8>
    return result

def main() -> None:
    result = supervisor()  # <9>
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
# end::SPINNER_THREAD_REST[]
