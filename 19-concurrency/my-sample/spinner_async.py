import asyncio
import itertools

#1 We don't need the Event argument that was used to
# signal that slow had completed its job in spinner_thread.py.
async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try: 
            
            #2 Use await asyncio.sleep(.1) instead of done.wait(.1)
            # to pause without blocking other coroutines.
            # await asyncio.sleep(.1)
            pass
        
        #3 asyncio.CancelledError is raised when the cancle
        # method is called on the Task controlling this coroutine.
        # Time to exit the loop.
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')
    
async def slow() -> int:
    #4 The slow coroutine also use await asyncio.sleep(3) instead 
    # of time.sleep(3), other coroutines take control and run while
    # this one is paused for 3 seconds.
    await asyncio.sleep(3)
    return 42

# Native coroutines are defined with async def.
async def supervisor() -> int:
    
    # asyncio.create_task schedules the spin coroutine to run,
    # and returns a Task object immediately.
    spinner = asyncio.create_task(spin('thinking!'))
    
    # The repr of the spinner object looks like <Task pending
    # name='Task-1' coro=<spin() running at 
    # /path/to/spinner_async.py:11>>
    print(f'spinner object: {spinner}')
    
    # The await keyword calls slow, blocking supervisor until
    # slow returns. the return value of slow will be assigned
    # to result.
    result = await slow()
    
    # The Task.cancel method raises a CancelledError exception
    # inside the spin coroutine.
    spinner.cancel()
    return result

# main is the only regular function defines in this program
# --the others are coroutines.
def main() -> None:
    # The asyncio.run function starts the event loop to drive the
    # coroutine that will eventually set the other coroutines in motion.
    # The main function will stay blocked until supervisor returns.
    # The return value of supervisor will be the return value of 
    # asyncio.run.
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


    
if __name__ == '__main__':
    main()