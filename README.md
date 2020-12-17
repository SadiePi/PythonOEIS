# PythonOEIS
Python implementation of the sequences in the [OEIS](https://oeis.org). Pull requests welcome!

Each sequence is implemented in 2 ways, though both take an index argument. Functions labeled with 'A' (e.g. A000040) will simply return the integer at that index in the sequence. Functions labeled with 'G' (e.g. G000040) are generators that will yield every element in the sequence up to that index. This is done to abstract away optimizations to sequence implementations that rely on previous elements in the sequence, such as the primes.

Sequences are being implemented in order of increasing index, with the following exceptions:

Skipped sequences:
 * A000001 - No full formula, subject not sufficiently understood
 * A000003 - No full formula, subject not sufficiently understood
 * A000009 - No understood formula, will look again later

Preempted sequences: 
 * A000040 - Primes, very useful
 * A000115 - Used in 000008
 * A000196 - Previously used in another sequence
 * A005132 - Recaman's Sequence, just fun

Once many more sequences are implemented, I'll be refactoring many of them to use crossref formulas, hopefully simplifying them.

I'm not sure what the best way to structure this is. Currently my plan is to have one monolithic file with every function, making imports easy (from OEIS import G000040 as primes) but making the file huge. One possibility is to split it into multiple modules with maybe a few thousand each, making imports a bit less nice (from OEIS03 import A031245), but making the files smaller. I've also considered trying to group them into more specific submodules, like OEIS.GroupTheory, OEIS.NumberTheory, etc but that seems unfeasible due to it basically entailing categorizing all of mathematics into a tree structure instead of the highly connected graph it certainly is. 
