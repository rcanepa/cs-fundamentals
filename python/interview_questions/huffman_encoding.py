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
import struct
from collections import Counter
from queue import PriorityQueue


class HuffmanCoder(object):
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
        self._huffman_tree = None
        self._huffman_encoding_table = None
        self.original_text_size = 0  # original data in bits
        self.encoded_text_size = 0  # encoded data in bits
        self.compression_rate = 0.0  # ratio between both
        self.padding_bits = 0  # bits added at the end to complete a byte

    def generate_tree(self, text):
        char_frequencies = Counter(text)

        # n = the number of unique chars.
        # Load the priority queue O(n * log(n)).
        pq = PriorityQueue()
        for char, weight in char_frequencies.items():
            node = HuffmanCoder.HoffmanLeafNode(char, weight)
            pq.put((node.weight, node))

        # Constructing the tree with a priority queue is O(n log(n)).
        # For every char O(n) put O(log(n)) must be executed.
        while pq.qsize() > 1:
            (w1, n1) = pq.get()
            (w2, n2) = pq.get()
            parent_node = HuffmanCoder.HoffmanNode(n1.weight + n2.weight)
            parent_node.left = n1
            parent_node.right = n2
            pq.put((parent_node.weight, parent_node))

        (_, encoding_tree) = pq.get()
        self._huffman_tree = encoding_tree
        return encoding_tree

    def generate_codes_table(self):
        """O(n)"""
        codes_table = dict()

        def generate_path(tree, path=""):
            if isinstance(tree, HuffmanCoder.HoffmanLeafNode):
                codes_table[tree.char] = path
            else:
                generate_path(tree.left, path + "0")
                generate_path(tree.right, path + "1")

        generate_path(self._huffman_tree)
        self._huffman_encoding_table = codes_table
        return codes_table

    def encode_text(self, text):
        self.original_text_size = len(text) * 8
        encoded_text = ""
        for c in text:
            encoded_text += self._huffman_encoding_table[c]
        encoded_bits = len(encoded_text)

        # Make sure that we have complete bytes. If not, pad at the end
        # with zeros.
        if (encoded_bits % 8) != 0:
            padding_zeros = 8 - (encoded_bits % 8)
            encoded_text += "0" * padding_zeros
            self.padding_bits = padding_zeros

        self.encoded_text_size = len(encoded_text)
        self.compression_rate = len(encoded_text) / (len(text) * 8)
        return encoded_text

    def encoded_text_to_bytes(self, encoded_text):
        if self.encoded_text_size % 8 != 0:
            raise Exception("The number of encoded bits isn't a multiple of 8.")

        encoded_bytes = bytearray()
        for starting_point in range(0, self.encoded_text_size, 8):
            encoded_bytes.append(int(encoded_text[starting_point: starting_point + 8], 2))

        print("### Encoded bytes:", encoded_bytes)
        return encoded_bytes

    def compress_text(self, text):
        self.generate_tree(text)
        self.generate_codes_table()
        encoded_text = self.encode_text(text)
        self.encoded_text_to_bytes(encoded_text)
        return encoded_text


data = ["happy hip hop", "abracadabra"]


if __name__ == "__main__":
    coder = HuffmanCoder()
    for index, text in enumerate(data):
        encoded_text = coder.compress_text(text)

        print("Original text length:", coder.original_text_size, "bits")
        print("Encoded text length:", coder.encoded_text_size, "bits")
        print("Compression rate:", coder.compression_rate * 100, "%")
        print(coder._huffman_encoding_table)
        print("Encoded text:", encoded_text)

        output_file = open("compressed_data_{}".format(index), "wb")

        bytes_to_write = (len(encoded_text) + 7) // 8
        print("Bytes to write:", bytes_to_write)
        starting_bit = 0
        output_file.flush()

        for byte in range(1, bytes_to_write + 1):
            ending_bit = (starting_bit // 8 + 1) * 8
            print("Writing from bit", starting_bit, "to bit", ending_bit - 1, ":", encoded_text[starting_bit:ending_bit])
            packed = struct.pack("<c", int(encoded_text[starting_bit:ending_bit], 2).to_bytes(1, 'little'))
            output_file.write(packed)
            output_file.flush()
            starting_bit = ending_bit

        output_file.close()
