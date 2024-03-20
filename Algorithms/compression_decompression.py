import Huffman
import time
from matplotlib import pyplot as plt
from tabulate import tabulate

# List of files for compression and decompression
list = ["1_wers.txt", "3_wersy.txt", "10_wersow.txt", "25_wersow.txt", "50_wersow.txt"]

# Initialization of variables
array_before = []
array_after = []
table = []
array_len = []
times_compress = []
times_decompress = []
percent_compress = []

# Loop over the list of files
for file in list:
    with open(file, 'r') as file:
        text = file.read()

    # Text compression
    start1 = time.perf_counter_ns()
    tree, counter, codes, encoding = Huffman.compress(text)
    finish1 = time.perf_counter_ns()

    # Text decompression
    start2 = time.perf_counter_ns()
    decoding = Huffman.decompress(tree, encoding)
    finish2 = time.perf_counter_ns()

    # Calculating the number of bits before and after compression
    bits_before, bits_after = Huffman.count_bits(text, encoding)
    compression_ratio = (bits_after / bits_before) * 100
    percent_compress.append(compression_ratio)

    # Creating a table with Huffman symbols and their codes
    for symbol, count in counter.items():
        table.append([symbol, count, codes[symbol]])

    # Saving the results to the appropriate arrays
    array_before.append(bits_before)
    array_after.append(bits_after)
    length = len(text)
    array_len.append(length)

    # Saving compression and decompression time
    t = finish1 - start1
    times_compress.append(t)
    d = finish2 - start2
    times_decompress.append(d)

    # Saving the table to a text file
    with open("tables.txt", 'a') as tab:
        tab.write(tabulate(table, headers=["Symbol", "Count", "Huffman code"]))
        tab.write("\n\n\n")

# Plots
plt.subplot(1, 3, 1)
plt.plot(array_len, array_before, label="Bits before")
plt.plot(array_len, array_after, label="Bits after")
plt.title("Memory occupied before and after")
plt.legend()
plt.xlabel("Number of characters")
plt.ylabel("Number of bits")

plt.subplot(1, 3, 2)
plt.plot(array_len, times_compress, color="green", label="Times compress")
plt.plot(array_len, times_decompress, color="yellow", label="Times decompress")
plt.title("Compression and decompression execution time")
plt.legend()
plt.xlabel("Number of characters")
plt.ylabel("Times in nanoseconds")

plt.subplot(1, 3, 3)
plt.plot(array_len, percent_compress, color="red", label="Percent")
plt.ylim(0, 100)
plt.title("Compression time percentage")
plt.legend()
plt.xlabel("Number of characters")
plt.ylabel("%")

plt.show()
