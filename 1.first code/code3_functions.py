#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kazem
"""
import time


def is_prime(n):
    time.sleep(1)

    if n < 2:
        return False, n
    elif n == 2:
        return True, n
    sqrt_n = int(n**0.5)+1
    return len([i for i in range(2, sqrt_n+1) if n % i == 0]) == 0, n

def only_primes(stream):
    try:
        while True:
            is_valid, value = is_prime(next(stream))
            while not is_valid:
                is_valid, value = is_prime(next(stream))
            yield value
    except StopIteration:    
        return

def streaming_statistics(stream):
    values =[]
    try:
        while True:
            values.append(next(stream))
            mean = float(sum(values)) / len(values)
            variance = float(sum([((x - mean) ** 2) for x in values]) / len(values))
            stdv = float(variance ** 0.5)
            print(values[-1],{'mean': mean, 'std': stdv})
            yield {'mean': mean, 'std': stdv}
    except StopIteration:
        return 0


if __name__ == '__main__':
    from itertools import islice, tee
    list_in = range(100)
         
    it = iter(list_in)

    L = only_primes(it)
    
    raw, stats = tee(L)
    
    out = list(islice(zip(raw, streaming_statistics(stats)), 30))



