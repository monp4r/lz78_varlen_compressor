<h1 align="center"><p align="center">LZ78 Variable-Length Compressor</h1></h1>
<p align="center" id="badges">
    <a href="https://github.com/monp4r/lz78_varlen_compressor/blob/master/LICENSE"><img src="https://img.shields.io/github/license/monp4r/lz78_varlen_compressor" alt="License"></a>
    <a href="#"><img src="https://img.shields.io/github/languages/code-size/monp4r/lz78_varlen_compressor" alt="Code size"></a>
    <a href="https://github.com/monp4r/lz78_varlen_compressor/commits"><img src="https://img.shields.io/github/last-commit/monp4r/lz78_varlen_compressor" alt="Last commit"></a>
</p>

> Created by **Juan Francisco Montero** (<https://github.com/monp4r/>)

## Introduction
Welcome to the LZ78 Variable-Length Compressor, where efficiency meets simplicity in the world of text file compression. 

Based on the LZ78 lossless data compression algorithm published by Abraham Lempel and Jacob Ziv, it consists of a single executable program that can be used both as a compressor and decompressor, depending on the selected menu options. It provides optimal compression ratios while maintaining ease of use.

The LZ78 Variable-Length Compressor has been developed as the final project for the Automatic Information Processing exam in the Double Degree program in Mathematics and Computer Science at the University of Valladolid.

## Features:
- **Efficient Compression:** Utilizes advanced LZ78 algorithm to achieve high compression ratios.
- **Up to 12-Bit Support:** Precision handling of variable-length encoding, accommodating up to 12 bits for optimal compression.
- **User-Friendly Interface:** Simple command-line interface for seamless compression operations.
- **Robust Error Handling:** Ensures reliability and robustness during compression, giving you peace of mind.

Ready to experience lightning-fast compression without compromising quality? Let's get started!

## How it works?:

The LZ78 Variable-Length Compressor works by analyzing the input text file and identifying recurring patterns. Here's a step-by-step overview of the compression and decompression process:

1. **Compression:**
   - **Building the Dictionary:** The compressor reads the input text file and builds a dictionary of phrases encountered in the text.
   - **Variable-Length Encoding:** Each phrase in the dictionary is assigned a unique index, and the compressor replaces each occurrence of a phrase with its corresponding index. The indices are encoded using variable-length encoding to optimize storage efficiency.
   - **Output Generation:** The compressor generates the compressed output, consisting of a sequence of indices representing the phrases in the input text.

2. **Decompression:**
   - **Dictionary Reconstruction:** During decompression, the compressor reconstructs the dictionary using the indices provided in the compressed file.
   - **Decoding Indices:** The decompressor reads the sequence of indices from the compressed file and decodes them using variable-length decoding to retrieve the original phrases.
   - **Output Reconstruction:** As the indices are decoded, the decompressor reconstructs the original text by replacing each index with its corresponding phrase from the dictionary.

The LZ78 Variable-Length Compressor utilizes this process to achieve efficient compression and decompression of text files while maintaining data integrity.

## Example

Let's observe the decoding process with this example.

Given a dictionary and the tuples of a message, it is possible to decode it in an orderly manner to obtain the message. For example, the first entry in the dictionary is A, so its decoding will be A itself. The same applies to the second and third entries in the dictionary, being single letters.

For the fourth entry in the dictionary, it is decoded as AC, and so on for all entries. The final message in this case is the result of concatenating all the entries in the dictionary, for this example it is 'ABRACADABRA'.

As we can see, the presence of dictionary entries greatly facilitates decoding, making it almost trivial. It could happen that we are unaware of the entries in our dictionary and only know the relationship between each tuple and its dictionary index. In this case, the easiest way would be to obtain the entry of each dictionary position similarly to how it was done in the previous example.

<div align="center">

| Decoding      | Tuple         | Dictionary[Index] | Dictionary Entry |
|---------------|---------------|-------------------|------------------|
| A             | (0,a)         | 1                 | A                |
| B             | (0,b)         | 2                 | B                |
| R             | (0,r)         | 3                 | R                |
| AC            | (1,c)         | 4                 | AC               |
| AD            | (1,d)         | 5                 | AD               |
| AB            | (1,b)         | 6                 | AB               |
| RA            | (3,a)         | 7                 | RA               |

</div >

## How it really works?:

## Usage:

## Getting Started:

## Examples:

## Metrics:

## Caution:

## Evaluation of Dictionary-based Compressor Performance:

To assess the performance of our dictionary-based compressor, we conducted compression tests on several books from the Gutenberg Project, including Philosophiae Naturalis Principia Mathematica, War and Peace, as well as the file of the book El ingenioso hidalgo don Quijote de la Mancha provided in the virtual campus of the subject.

We've created a comparative table to illustrate the tests conducted with the program, analyzing the uncompressed size, compressed size, and compression factor of each file. The compression factor is defined as the ratio of the compressed size of a file to its uncompressed size, allowing us to understand the percentage of the original size occupied by the compressed file.

<div align="center">

| File                     | Uncompressed Size | Compressed Size | Compression Factor |
|--------------------------|-------------------|-----------------|--------------------|
| quijote.txt              | 2100 KB           | 978 KB          | 0.466              |
| philosophiae_mathematica.txt | 852 KB         | 420 KB          | 0.493              |
| war_and_peace.txt        | 3400 KB           | 1500 KB         | 0.441              |
| a_reptidas.txt           | 1000 KB           | 3 KB            | 0.003              |
| checkmates_data.txt      | 18800 KB          | 3700 KB         | 0.197              |

</div>

Upon analyzing these data, we observe that the dictionary-based compressor shows significant efficiency in most cases, with compression factors ranging between 0.003 and 0.493. This suggests that the existence of patterns in the character string of the text significantly contributes to the compression capability. However, we also note that the compression factor varies widely depending on the file content, as evidenced by the file "a_reptidas.txt," which contains repeated characters, resulting in extremely efficient compression. In conclusion, these results support the effectiveness of the dictionary-based compressor and underscore the importance of considering the content nature when evaluating data compression techniques.

## Future Development:

## Acknowledgements:

## References:
Angel, P. (2022, April 28). Un Poco de Historia: Algoritmos LZ77, LZ78 y lzw - INCUBAWEB - software y web 2.0. Incubaweb. [https://www.incubaweb.com/un-poco-de-historia-algoritmos-lz77-lz78-y-lzw/](https://www.incubaweb.com/un-poco-de-historia-algoritmos-lz77-lz78-y-lzw/)

Hmong.wiki. (n.d.). LZ77 y lz78 Contenido y eficiencia Teórica [https://hmong.es/wiki/LZ77_and_LZ78](https://hmong.es/wiki/LZ77_and_LZ78)

Ignacio, F. M. J. (2020). Computación Matemática Con Python: Introducción Al Lenguaje python para Científicos e Ingenieros. Ediciones Universidad de Valladolid.
