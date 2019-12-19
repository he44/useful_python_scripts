import os
import numpy as np
import time
import math
from multiprocessing import Pool
import shutil

def f(x):
    #  some computation
    fixed = x
    for i in range(1000):
        fixed += 0.1
        ret = math.log(fixed)
    #  some moving (should just be some dummy file)
    #  hopefully this dst can be generated with fixed
    src_name = os.path.join('random_files', '%d.npy'%x)
    dst_name = os.path.join('random_files_moved', '%d.npy'%x)
    shutil.copyfile(src_name, dst_name)
    return ret

def math_and_moving_sp(input_list):
    output_list = []
    for i in range(len(input_list)):
        output_list.append(f(input_list[i]))
    return output_list

def math_and_moving_mp(input_list):
    pool_threads = Pool(64)
    output_list = pool_threads.map(f, input_list)
    pool_threads.terminate()
    pool_threads.close()
    

def main():
    input_list = list(range(1000))
    print(input_list)
    print("Testing multi process")
    t1 = time.perf_counter()
    # ret_list = math_and_moving_sp(input_list)
    ret_list = math_and_moving_mp(input_list)
    t2 = time.perf_counter()
    print("Took", t2-t1)
    

if __name__ == "__main__":
    main()
