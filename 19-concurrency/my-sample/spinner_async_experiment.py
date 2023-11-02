# spinner_async_experiment.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import asyncio
import itertools
import time

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        # No animation here?
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    print('THIS WILL NEVER BE OUTPUT')

# tag::SPINNER_ASYNC_EXPERIMENT[]
async def slow() -> int:
    # <4> time.sleep(3) blocks for 3 seconds and doesn't transfer control to
    # other coroutines; nothing else can happen in the program, because the main
    # thread is blocked--and it is the only thread. The operating system will
    # continue with other activities. After 3 seconds, sleep unblocks, and the 
    # slow returns.    
    time.sleep(3) 
    return 42

async def supervisor() -> int:
    # <1> The spinner task is created, to eventually drive the execution of spin.
    spinner = asyncio.create_task(spin('thinking!')) 
    
    # <2> The display shows the Task is pending.
    print(f'spinner object: {spinner}') 
    
    # <3> The await expression transfers control to the slow coroutine.
    result = await slow() 
    
    # <5> Right after slow returns, the spinner is canceled. The flow of
    # control never reached the body of the spin coroutine.
    spinner.cancel()  
    return result
# end::SPINNER_ASYNC_EXPERIMENT[]

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
