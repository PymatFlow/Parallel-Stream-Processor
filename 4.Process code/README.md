#### **Streams**
There are three folders in *Streams* folder

**1.first code**
This code is my first attempt to get more familiar with available methods in the assignment

**2.First multiprocessing code**
This code is the first attempt to using multiprocessing.

**3.Final code**
This is the final code. It contains comments for easier understanding. You can find more information about the code from the comments at each line of the final code.


**4.Process code**
This is the version of the final code with Process, Queue.
This code is faster than using Pool, approximately ten times faster.



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
- Increase the number of processes to have faster running. 
In the following code, the number of processes is 32. 
```python
from itertools import islice, tee
%time list(StreamProcessor(range(100), is_prime, only_primes, number_of_processes=32))
```
- You need [multiprocessing](https://docs.python.org/3/library/multiprocessing.html "multiprocessing") and [time](https://docs.python.org/3/library/time.html "time") to use this code. 


- Python 3 is used in this assignment

- The correct and accurate running of this code in Windows is not guaranteed. **Please use Linux**. I used Linux. My experience in windows showed me, windows operating system fails in most of the multiprocessing code.

