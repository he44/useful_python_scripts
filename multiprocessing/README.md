# Multiprocessing In Python

### Code

```python
num_processes = 12
pool_threads = Pool(processes=num_processes)
return_list = pool_threads.map(f, input_list)
pool_threads.terminate()
pool_threads.close()
```

- It's okay to just call ```Pool()```. By default, processes will be filled in with whatever ```os.cpu_count()``` returns. For my laptop, this number is 8. I fed in 12, which is more than my machine has, there's no error/warning. Probably the interpreter filtered the number and picked the best one.

- ```return_list = pool_threads.map(f, input_list)``` is equivalent to ```output = f(input)``` in a single-process setting.

  - f is the function to execute in parallel

  - input_list is a Python list [], each entry is one input to the funciton f

### Some Testing

If I define ```f``` to be s really simple function, e.g. returning the square of a number, there will not be too much speed-up. In fact, from my experiemnts, it is actually faster to iterate through a list and compute the square of each entry than to invoke multi-processing.

```python
def f(x):
    return x*x

def square_all_numbers_single(input_list):
    return_list = []
    for i in range(len(input_list)):
        return_list.append(f(input_list[i]))
    print(return_list)
    print("Done!")

    random_list = np.random.randint(low=0, high=1000, size=100).tolist()
    print(random_list)

    t1 = time.perf_counter()
    square_all_numbers_mp(random_list)
    t2 = time.perf_counter()

    square_all_numbers_single(random_list)

    t3 = time.perf_counter()

    print(t2-t1, t3-t2)
```

The output from the terminal is as followed. The first number indicates the run time (in seconds) of the multiprocessing method. The second number indicates the run time of the single-process for-loop method.

```bash
0.4718587999999999 0.0024996000000000462
```

I think the reason is that starting up additional process will take time as well. And if this function is not complex enough, the speed up we get will not be enough to cancel out those additional starting up time. A more detailed explanation can be found on Stackoverflow: https://stackoverflow.com/questions/20727375/multiprocessing-pool-slower-than-just-using-ordinary-functions

If I add more computation inside ```f(x)```, I can see there is speed-up by invoking multiprocessing.

```python
def f(x):
    fixed = x
    for i in range(100000):
        ret = math.log(fixed)
        fixed += 0.1
    return ret
```

```bash
1.3905964 1.9909054
```

If we increase the loop size inside ```f(x)```, the speed up will be more evident.

```
def f(x):
    fixed = x
    for i in range(10000000):
        ret = math.log(fixed)
        fixed += 0.01
    return ret
```

```bash
12.5859854 53.500728800000005
```