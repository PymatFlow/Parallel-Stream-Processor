#### **Streams**
There are four folders in *Streams* folder

**1.first code**
This code is my first attempt to get more familiar with available methods in the assignment

**2.First multiprocessing code**
This code is the first attempt to using multiprocessing.

**3.Final code**
This is the final code. It contains comments for easier understanding. You can find more information about the code from the comments at each line of the final code.

##### 3.1 output : 
[(False, 1), (True, 2), (True, 3), (False, 4), (True, 5), (False, 6), (True, 7), (False, 8), (False, 9), (False, 10)]
Wall time:   **12.54 s**


[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Wall time:   **28.32 s**


[2, 3, 5, 7, 11]
Wall time:   **20.41 s**


[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Wall time:   **4.71 s**


2 {'mean': nan, 'std': nan}
3 {'mean': 2.5, 'std': 0.5}
5 {'mean': 3.3333333333333335, 'std': 1.247219128924647}
7 {'mean': 4.25, 'std': 1.920286436967152}
11 {'mean': 5.6, 'std': 3.2}
13 {'mean': 6.833333333333333, 'std': 4.017323597731316}
17 {'mean': 8.285714285714286, 'std': 5.146823867043378}
19 {'mean': 9.625, 'std': 5.977823600609171}
23 {'mean': 11.11111111111111, 'std': 7.030796453136166}
29 {'mean': 12.9, 'std': 8.560957890329798}
Wall time:   **28.33 s**

**4.Process code**
This is the version of the final code with Process, Queue.
This code is faster than using Pool, approximately **ten times** faster.

##### 4.1 output : 

[[True, 1], [False, 2], [True, 3], [False, 4], [True, 5], [False, 6], [True, 7], [False, 8], [False, 9], [False, 10]]
Wall time:   **2.26 s**


[1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Wall time:   **1.67 s**


[1, 3, 5, 7, 11]
Wall time:   **1.58 s**


[1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Wall time:   **1.57 s**


1 {'mean': nan, 'std': nan}
3 {'mean': 2.0, 'std': 1.0}
5 {'mean': 3.0, 'std': 1.632993161855452}
7 {'mean': 4.0, 'std': 2.23606797749979}
11 {'mean': 5.4, 'std': 3.4409301068170506}
13 {'mean': 6.666666666666667, 'std': 4.2295258468165065}
17 {'mean': 8.142857142857142, 'std': 5.329930887479323}
19 {'mean': 9.5, 'std': 6.144102863722254}
23 {'mean': 11.0, 'std': 7.180219742846005}
29 {'mean': 12.8, 'std': 8.692525524840294}
Wall time:   **1.58 s**




####How to run :
You just need to run the code to see the result or you can import it and use in any other python code.

**Examples :**

```python
from itertools import islice, tee
%time list(islice(StreamProcessor(range(100), is_prime, number_of_processes=10), 10))
```

```python
from itertools import islice, tee
%time list(StreamProcessor(range(100), is_prime, only_primes, number_of_processes=4))
```


**Notes**
- Increase the number of processes to have faster running in Pool. 
In the following code, the number of processes is 32. 
```python
from itertools import islice, tee
%time list(StreamProcessor(range(100), is_prime, only_primes, number_of_processes=32))
```
- You need [multiprocessing](https://docs.python.org/3/library/multiprocessing.html "multiprocessing") and [time](https://docs.python.org/3/library/time.html "time") to use and run this code.


- Python 3 is used in this assignment

- The correct and accurate running of this code in Windows is not guaranteed. **Please use Linux**. I used Linux. My experience in windows showed me, windows operating system fails in most of the multiprocessing code.

