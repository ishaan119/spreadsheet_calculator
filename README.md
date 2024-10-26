# Fiddler Labs Spreadsheet Calculator

A spreadsheet consists of a two-dimensional array of cells, labeled A1, A2, etc. Rows are identified using letters, columns by numbers. Each cell contains either an integer (its value) or an expression. Expressions contain integers, cell references, and the operators `+`, `-`, `*`, `/` with the usual rules of evaluation. Note that the input is in **Reverse Polish Notation (RPN)** and should be evaluated in stack order.

## Problem Statement

Write a program (in Python, C, C++, or Java) to read a spreadsheet from `stdin`, evaluate the values of all the cells, and write the output to `stdout`.

### Input

- Line 1: Two integers, defining the width and height of the spreadsheet (`n`, `m`).
- `n * m` lines, each containing an expression which is the value of the corresponding cell (cells enumerated in the order A1, A2, ... A<n>, B1, …).

### Output

- The output should have the same format but with each cell reduced to a single floating-point value.

