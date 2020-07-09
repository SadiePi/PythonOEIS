# PythonOEIS
Python implementation of the sequences in the OEIS

Each sequence is implemented in 2 ways, though both take an index argument. Functions labeled with 'A' (e.g. A000040) will simply return the integer at that index in the sequence. Functions labeled with 'G' (e.g. G000040) are generators that will yield every element in the sequence up to that index. This is done to abstract away optimizations to sequence implementations that rely on previous elements in the sequence, such as the primes.
