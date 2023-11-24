import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_task(task_name):
    print(f"Task {task_name} begin in {threading.current_thread().name}")
    time.sleep(.5)
    print(f"Task {task_name} end...")

# define a async function
async def my_coroutine():
    print("The coroutine starts...")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        to_do_map = {}
        for i in range(5):
            task_name = f'Task-{i}'
            print(f'Create and submit {task_name}')
            future = executor.submit(do_task, task_name)
            to_do_map[future] = task_name
        
        print('Waiting for all tasks done...')
        done_iter = as_completed(to_do_map)
        for future in done_iter:           
            print(f"{to_do_map[future]} is done.")
            print(f"Current time: {time.time()}")   

    
    print("The coroutine ends...")

# run the coroutine
asyncio.run(my_coroutine())