from multiprocessing import Pool
import time
import numpy as np
import math

def f(x):
    fixed = x
    for i in range(1000000):
        ret = math.log(fixed)
        fixed += 0.1
    return ret
        

def square_all_numbers_mp(input_list):
    """
    Declare number of processes
    https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool
    processes gives the number of worker processes to use, if it's None then os.cpu_count() will be used
    it also shouldn't matter if it's larger than cpu_count()
    """
    num_processes = 12

    """
    Create the workers
    """
    pool_threads = Pool(processes=num_processes)

    """
    Execute
    """
    return_list = pool_threads.map(f, input_list)

    pool_threads.terminate()
    pool_threads.close()
    print(return_list)
    print("Done!")

def square_all_numbers_single(input_list):
    return_list = []
    for i in range(len(input_list)):
        return_list.append(f(input_list[i]))
    print(return_list)
    print("Done!")



if __name__ == "__main__":
    #  original_list = [3, 4, 12, 20, 24, 54, 34, 88, 90, 128, 342, 453, 342, 2434]

    random_list = np.random.randint(low=0, high=1000, size=100).tolist()
    print(random_list)

    t1 = time.perf_counter()
    square_all_numbers_mp(random_list)
    t2 = time.perf_counter()

    square_all_numbers_single(random_list)

    t3 = time.perf_counter()

    print(t2-t1, t3-t2)
    

    
