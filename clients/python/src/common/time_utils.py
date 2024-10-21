from time import perf_counter
import logging

logger = logging.getLogger(__name__)

def function_timer(func): 
    def wrapper_function(*args, **kwargs): 
        start_time = perf_counter() 
        func(*args,  **kwargs) 
        end_time = perf_counter()
        elapsed_time_in_sec =  end_time - start_time 

        logger.info(f"function {func.__name__} elapsed execution time: {elapsed_time_in_sec} sec(s)")

    return wrapper_function 