## Huffman Coding

### How to use

* First, make sure the user has permission to execute the script.
* Run with flag -c to compress data and -d to the compress.

Examples:

*Compress the program itself.*
````
cat huffman_encoding.py | ./huffman_encoding.py -c
````
*Compress and decompress the program itself.*
````
cat huffman_encoding.py | ./huffman_encoding.py -c | ./huffman_encoding.py -d
````
*Assert the output is equal to the source data.*

````
diff <(cat huffman_encoding.py | ./huffman_encoding.py -c | ./huffman_encoding.py -d) huffman_encoding.py
````

### Things to improve
* Allow the user to specify a file as input and another one as output.
* Implement the DEFLATE algorithm based on [RFC 1951](http://tools.ietf.org/html/rfc1951)
* About the code:
    * Improve variable names.
    * Comment functions.
    * Add a draw of the memory layout used by the algorithm.
