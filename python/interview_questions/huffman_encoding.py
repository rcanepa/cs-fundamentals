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
import sys
from collections import Counter
from queue import PriorityQueue


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
        self.encoded_bits = 0  # encoded data in bits
        self.compression_rate = 0.0  # ratio between both
        self.padding_bits = 0  # bits added at the end to complete a byte

    def generate_tree(self, source):
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
        """O(n)"""
        encoding_table = dict()
        reversed_encoding_table = dict()

        def generate_path(tree, path=""):
            if isinstance(tree, HuffmanEncoder.HoffmanLeafNode):
                encoding_table[tree.char] = path
            else:
                generate_path(tree.left, path + "0")
                generate_path(tree.right, path + "1")

        generate_path(self._encoding_tree)

        for char, path in encoding_table.items():
            reversed_encoding_table[path] = char
        self._encoding_table = encoding_table
        self._reversed_encoding_table = reversed_encoding_table
        return encoding_table

    def encode(self, source):
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

        self.encoded_bits = len(encoded_data)
        self.compression_rate = len(encoded_data) / (len(source) * 8)
        return encoded_data

    def encoded_data_to_bytes(self, encoded_data):
        if self.encoded_bits % 8 != 0:
            raise Exception("The number of encoded bits isn't a multiple of 8.")

        encoded_bytes = bytearray()
        for starting_point in range(0, self.encoded_bits, 8):
            # print("### Encoding bytes:", encoded_data[starting_point: starting_point + 8])
            encoded_bytes.append(int(encoded_data[starting_point: starting_point + 8], 2))

        # print("### Encoded bytes:", encoded_bytes)
        # print("### Number of encoded bytes:", len(encoded_bytes))
        return encoded_bytes

    def compress_text(self, source):
        self.generate_tree(source)
        self.generate_encoding_table()
        encoded_data = self.encode(source)
        print("# Encoded data:", encoded_data)
        encoded_bytes = self.encoded_data_to_bytes(encoded_data)
        return encoded_bytes

    def decode_data(self, encoded_bytes):
        reading_format = "0{}b".format(len(encoded_bytes) * 8)
        encoded_bits = format(int.from_bytes(read_bytes, byteorder='big'), reading_format)
        key = ""
        decoded_data = ""
        for bit in encoded_bits[:self.encoded_bits - self.padding_bits]:
            key += bit
            if key in self._reversed_encoding_table:
                decoded_data += self._reversed_encoding_table[key]
                key = ""
        # print(decoded_data)
        return decoded_data


# data = ["happy hip hop", "abracadabra"]
data = ["happy hip hop"]

if __name__ == "__main__":
    coder = HuffmanEncoder()
    for index, text in enumerate(data):
        encoded_bytes = coder.compress_text(text)
        # sys.stdout.buffer.write(encoded_bytes)
        with open("compressed_data_2", "rb") as f:
            read_bytes = f.read()
            print("# Decoded data:", coder.decode_data(read_bytes))
