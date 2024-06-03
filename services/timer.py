import time

start_time = time.time()

def start():
    global start_time
    start_time = time.time()
    
def end():
    end_time = time.time()
    execution_time = end_time - start_time
    return round(execution_time, 2)