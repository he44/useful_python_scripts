"""
Using multi-threading to perfrom some I/O work
"""
from concurrent.futures import ThreadPoolExecutor
import os
import numpy as np
import time
import math
from multiprocessing import Pool
import shutil

def f(x):
    src_name = os.path.join('random_files', '%d.npy'%x)
    dst_name = os.path.join('random_files_moved', '%d.npy'%x)
    shutil.copyfile(src_name, dst_name)

def moving_st(input_list):
    for i in range(len(input_list)):
        f(input_list[i])

def moving_mt(input_list):
    #  max_workers, first argument of ThreadPoolExecutor
    #  if none, default to be num of processors on the machine
    with ThreadPoolExecutor() as executor:
        results = executor.map(f, input_list)

def main():
    input_list = list(range(1000))
    print(input_list)
    print("Testing single threading")
    t1 = time.perf_counter()
    ret_list = moving_st(input_list)
    t2 = time.perf_counter()
    print("Took", t2-t1)

if __name__ == "__main__":
    main()
