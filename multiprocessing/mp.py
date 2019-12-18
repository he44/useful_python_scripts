from multiprocessing import Pool

def f(x):
    return x ** 2

if __name__ == "__main__":
    original_list = [3, 4, 12, 20]

    print("Before:", original_list)
    
    num_processes = 12
    #  https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool
    #  processes gives the number of worker processes to use, if it's None then os.cpu_count() will be used
    pool_threads = Pool(processes=num_processes)
    return_list = pool_threads.map(f, original_list)

    print("After:", return_list)
