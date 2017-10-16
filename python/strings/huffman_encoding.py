#!/usr/bin/env python

"""Hoffman Encoding

Steps:
1. Create a collection of singleton trees, one for each character, with weight equal to
    the character frequency.
2. From the collection, pick out the two trees with the smallest weights and remove them.
    Combine them into a new tree whose root has a weight equal to the sum of the weights
    of the two trees and with the two trees as its left and right subtrees.
3. Add the new combined tree back into the collection.
4. Repeat steps 2 and 3 until there is only one tree left.
5. The remaining node is the root of the optimal encoding tree.
6. Create a HashTable (dict) between characters and their path on the tree.
7. Encode the text with the HashTable.
8. Write the bytes to a file.
"""
import argparse
import math
import sys
from collections import Counter
from queue import PriorityQueue


def _pack_bits_string(bits_string, bytes_package):
    """Append a string of bits into a bytearray. It handle cases in which
    the string requires more than one byte."""
    number_of_bytes = int(math.ceil(len(bits_string) / 8))

    # Check if there is an 'incomplete'. If that is the case, complete it
    # adding zeros to the left. A bit string like 0 0010 0001 would be
    # mapped to 0000 0000 0010 0001.
    if len(bits_string) % 8 != 0:
        bits_string = bits_string.zfill(number_of_bytes * 8)

    # Pack byte by byte.
    for starting_bit in range(0, number_of_bytes * 8, 8):
        bytes_package.append(int(bits_string[starting_bit: starting_bit + 8], 2))
    return bytes_package


class HuffmanEncoder(object):
    class HoffmanNode(object):
        def __init__(self, weight):
            self.weight = weight
            self.left = None
            self.right = None

        def __str__(self):
            return "Node [{}]".format(self.weight)

        def __lt__(self, other):
            return self.weight < other.weight

    class HoffmanLeafNode(HoffmanNode):
        def __init__(self, char, weight):
            super().__init__(weight)
            self.char = char

        def __str__(self):
            return "Leaf [{}, {}]".format(self.char, self.weight)

    def __init__(self):
        self._encoding_tree = None  # huffman binary tree
        self._encoding_table = None  # mapping from char to binary representation
        self._reversed_encoding_table = None  # mapping from binary representation to char
        self.source_bits = 0  # original data in bits
        self.n_encoded_bytes = 0  # encoded data in bytes
        self.compression_rate = 0.0  # ratio between both
        self.padding_bits = 0  # bits added at the end to complete a byte

    def generate_tree(self, source):
        """Generate a Huffman Tree according to the frequency of each character
        present in the `source` text.

        This operation is O(n * log(n))."""
        char_frequencies = Counter(source)

        # n = the number of unique chars.
        # Load the priority queue O(n * log(n)).
        pq = PriorityQueue()
        for char, weight in char_frequencies.items():
            node = HuffmanEncoder.HoffmanLeafNode(char, weight)
            pq.put((node.weight, node))

        # Constructing the tree with a priority queue is O(n log(n)).
        # For every char O(n) put O(log(n)) must be executed.
        while pq.qsize() > 1:
            (w1, n1) = pq.get()
            (w2, n2) = pq.get()
            parent_node = HuffmanEncoder.HoffmanNode(n1.weight + n2.weight)
            parent_node.left = n1
            parent_node.right = n2
            pq.put((parent_node.weight, parent_node))

        (_, encoding_tree) = pq.get()
        self._encoding_tree = encoding_tree
        return encoding_tree

    def generate_encoding_table(self):
        """Generate an encoding table given a Huffman Tree. It maps characters to
        strings of bits.
        E.g.: 'a' -> '001', 'b' -> '11'.

        This operation is O(n).
        """
        encoding_table = dict()
        reversed_encoding_table = dict()

        def generate_path(tree, path=""):
            if isinstance(tree, HuffmanEncoder.HoffmanLeafNode):
                encoding_table[tree.char] = path or "0"
            else:
                generate_path(tree.left, path + "0")
                generate_path(tree.right, path + "1")

        if isinstance(self._encoding_tree, HuffmanEncoder.HoffmanNode):
            generate_path(self._encoding_tree)
        else:
            encoding_table[self._encoding_tree.char] = "0"

        for char, path in encoding_table.items():
            reversed_encoding_table[path] = char
        self._encoding_table = encoding_table
        self._reversed_encoding_table = reversed_encoding_table
        return encoding_table

    def encode(self, source):
        """Encode a text string `source` into a string of 0s and 1s according to
        the `_encoding_table`."""
        self.source_bits = len(source) * 8
        encoded_data = ""
        for c in source:
            encoded_data += self._encoding_table[c]
        encoded_bits = len(encoded_data)

        # Make sure that we have complete bytes. If not, pad at the end
        # with zeros.
        if (encoded_bits % 8) != 0:
            padding_zeros = 8 - (encoded_bits % 8)
            encoded_data += "0" * padding_zeros
            self.padding_bits = padding_zeros

        self.n_encoded_bytes = len(encoded_data) // 8
        self.compression_rate = len(encoded_data) / (len(source) * 8)
        return encoded_data

    def pack_data(self, encoded_data):
        """Create a `bytearray` with two main pieces of information: the encoding
        table and the compressed data. The encoding table is needed to decompress
        the data.

        - Pack encoding table
            1. int with number of entries
            2. encoding table
                1. int with char representation
                2. int with number of bites used by the path (implicitly the numbers of bytes too)
                3. bytes of the path
            3. int with the number of padding bits
        - Pack the compressed data
        """
        bytes_package = bytearray()

        # Save the number of entries of the encoding table.
        bytes_package.append(len(self._encoding_table.keys()))

        # Save the encoding table. This implies saving first an integer with the
        # ASCII code of the represented char (99 = "c"); another integer with number of bits used
        # by the bit_code (eg.: 011 = 3); and the bit_code itself.
        for char, bit_code in self._encoding_table.items():
            ascii_char_code = ord(char)
            number_of_bits = len(bit_code)

            bytes_package.append(ascii_char_code)
            bytes_package.append(number_of_bits)
            _pack_bits_string(bit_code, bytes_package)

        # Save the total bits used and the total padding bits used.
        _pack_bits_string(bin(self.n_encoded_bytes * 8)[2:].zfill(4 * 8), bytes_package)

        # bytes_package.append(self.n_encoded_bytes)  # data + padding
        bytes_package.append(self.padding_bits)

        # Save compressed data.
        for starting_point in range(0, self.n_encoded_bytes * 8, 8):
            bytes_package.append(int(encoded_data[starting_point: starting_point + 8], 2))

        return bytes_package

    def compress_data(self, source):
        """Compress a text string `source` according to the Huffman Coding algorithm."""
        self.generate_tree(source)
        self.generate_encoding_table()
        encoded_data = self.encode(source)
        encoded_bytes = self.pack_data(encoded_data)
        return encoded_bytes

    def decode_data(self, encoded_bytes):
        """Decode the compressed data from `encoded_bytes` into a string."""
        encoding_table_entries = encoded_bytes[0]
        decoding_table = dict()

        pos = 1
        for i in range(encoding_table_entries):
            char = chr(encoded_bytes[pos])
            pos += 1
            number_of_bits = encoded_bytes[pos]
            pos += 1
            if number_of_bits % 8 == 0:
                number_of_bytes = number_of_bits // 8
            else:
                number_of_bytes = (number_of_bits // 8) + 1
            bit_code_bytes = encoded_bytes[pos: pos + number_of_bytes]
            pos += number_of_bytes
            bit_code = format(
                int.from_bytes(bit_code_bytes, byteorder="big"),
                "0{}b".format(number_of_bits)
            )
            decoding_table[bit_code] = char

        # Read the number of padding bits.
        number_of_encoded_bits = int.from_bytes(encoded_bytes[pos:pos + 4], byteorder="big")
        pos += 4
        number_of_padding_bits = encoded_bytes[pos]
        pos += 1

        # Read the compressed data bytes.
        compressed_data = encoded_bytes[pos:]

        reading_format = "0{}b".format(len(compressed_data) * 8)
        encoded_bits = format(int.from_bytes(compressed_data, byteorder="big"), reading_format)
        key = ""
        decoded_data = ""
        for bit in encoded_bits[:number_of_encoded_bits - number_of_padding_bits]:
            key += bit
            if key in decoding_table:
                decoded_data += decoding_table[key]
                key = ""
        return decoded_data


def main(args=None):
    coder = HuffmanEncoder()
    # print("------------------------------------------------------------------------")
    # print("# Original bytes:", len(text))

    if args.compress or not args.decompress:
        data = ""
        for line in sys.stdin:
            data += line
        encoded_bytes = coder.compress_data(data)
        sys.stdout.buffer.write(encoded_bytes)

    if args.decompress:
        source = sys.stdin.buffer
        data = source.read()
        sys.stdout.write(coder.decode_data(data))

    # decompressed_data = coder.decode_data(encoded_bytes)
    # sys.stdout.write(decompressed_data)
    # print("# Compressed bytes:", len(encoded_bytes))
    # print("# Compression rate: {:.2f}%".format(len(encoded_bytes) / len(text) * 100))
    # assert text == decompressed_data
    # print(decompressed_data)
    # print("------------------------------------------------------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--compress", help="compress data", action="store_true")
    group.add_argument("-d", "--decompress", help="decompress data", action="store_true")
    args = parser.parse_args()
    status = main(args)
    sys.exit(status)
