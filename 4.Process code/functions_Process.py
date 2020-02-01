#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kazem Gheysari
"""
import time
import weakref
import multiprocessing as mp


class StreamProcessor:
    def __init__(self, input_stream, map_function, reduce_generator=None,
                 *, number_of_processes=mp.cpu_count()):
        # We must return the results and __init___ mehtod can not return any things except None
        # and __new__ method uses cls so initialization of variable by self is not necessary 
        
        pass
    
    
    # The __new__() method is called when the class is ready to instantiate itself.   
    # The __new__ method runs earlier than the __init__ method.
    # cls represent the class that need to be instantiated, and this parameter is provided 
    # automatically by python parser at instantiating time.    
    def __new__(cls,input_stream, map_function, reduce_generator=None,
                 *, number_of_processes=mp.cpu_count()):    
        
        # Define a Queue object from multiprocessing library and start worker processes        
        q = mp.Queue()
        
        # Empty list for storing all processes
        procs = []
        
        # Empty list for storing final result
        result = []    
        
 
        for num in input_stream:   
            
            # creating processes
            pp = mp.Process(target=cls.is_prime,args=(q,num))
            
            # add current process to the process list
            procs.append(pp)
            
             # terminate when all work already assigned has completed
            pp.start()
        
        for pr in procs:
            
            # Getting data from worker function (is_prime)
            rest = q.get()
            
            # add the data to the final result
            result.append(rest)
        
        
        for pr in procs:
            
            # Wait for the worker processes to terminate
            pr.join()

        # When just is_prime method is called
        if map_function=='is_prime' and reduce_generator == None: 
             return result
        
        # When both is_prime and only_primes is called, the code must return only the prime number
        elif map_function=='is_prime' and reduce_generator == 'only_primes':
            
             # create a generator
             it = iter(result) 
            
             # call the only_primes
             result = cls.only_primes(it)
             return result
        else:
            
             # If the user enters the wrong inputs, print a message as an alert
             print("Inputs are wrong, Check your inputs")            
 
    def is_prime(q,n):
        n =n+1        
        time.sleep(1)
        
        is_valid = False
        if n < 2:
            is_valid = False
        elif n == 2:
            is_valid = True
        sqrt_n = int(n**0.5)+1 
        
        is_valid = len([i for i in range(2, sqrt_n+1) if n % i == 0]) == 0 
        
        # Put the final results on the Queue
        q.put([is_valid, n])
        

    def only_primes(stream):               
        try:
            while True:
                is_valid, value = next(stream)
                while not is_valid:
                    is_valid, value = next(stream)   
                yield value
        except StopIteration:    
            return 
        
def streaming_statistics(stream):
    
    # Define a empty list for storing the values
    values =[]
    
    try:
        
        # Infinite loop because we are creating a generator
        while True:
            
            # Read data from the generator and add it to a list (values)
            values.append(next(stream))
            
            # Mean calculation
            mean = float(sum(values)) / len(values)
            
            # Variance calculation
            variance = float(sum([((x - mean) ** 2) for x in values]) / len(values))
            
            # When the variance is zero, the value of mean and standard deviation must be NAN (Not-A-Number)
            # We can use Numpy for calculating the mean and standard deviation but importing other libraries is prohibited.
            if variance==0:
                mean,stdv = float('nan'), float('nan')
                
            else:
                
                # Standard deviation calculation
                stdv = float(variance ** 0.5)
            
            # Display the results
            print(values[-1],{'mean': mean, 'std': stdv})
            
            # Define a dictionary variable as the yield value
            yield {'mean': mean, 'std': stdv}
            
    except StopIteration:
        # when a generator stops yielding, return nothing
        return 
       


if __name__ == '__main__':
    
    from itertools import islice, tee
    
    start = time.time()
    sp =  list(islice(StreamProcessor(range(100), 'is_prime', number_of_processes=10),10))
    print(sp)
    print('Wall time:  ',round(time.time()-start,2), 's')
    print("\n")
    
    start = time.time()
    sp3 = list(StreamProcessor(range(100), 'is_prime', 'only_primes', number_of_processes=4))
    print(sp3)
    print('Wall time:  ',round(time.time()-start,2), 's')
    print("\n")
    
    start = time.time()
    sp2 = list(islice(StreamProcessor(range(100), 'is_prime', 'only_primes', number_of_processes=5), 5))
    print(sp2)
    print('Wall time:  ',round(time.time()-start,2), 's')
    print("\n")
    
    start = time.time()
    sp4 = list(StreamProcessor(range(100), 'is_prime', 'only_primes', number_of_processes=32))
    print(sp4)      
    print('Wall time:  ',round(time.time()-start,2), 's')
    print("\n")
    
    start = time.time()
    raw, stats = tee(StreamProcessor(range(100), 'is_prime', 'only_primes'))    
    out = list(islice(zip(raw, streaming_statistics(stats)), 10))
    print('Wall time:  ',round(time.time()-start,2), 's')


