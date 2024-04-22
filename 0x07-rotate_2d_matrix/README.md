# 0x07. Rotate 2D Matrix

## Algorithm

### Language: Python

**Weight:** 1

- **Project Start:** Apr 22, 2024 5:00 AM
- **Project End:** Apr 26, 2024 5:00 AM
- **Checker Release:** Apr 23, 2024 5:00 AM
- **Auto Review:** Will be launched at the deadline

For the "0. Rotate 2D Matrix" project, the task is to implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources needed to successfully complete this project.

### Concepts Needed:

- **Matrix Representation in Python:**
  - Understanding how 2D matrices are represented using lists of lists in Python.
  - Accessing and modifying elements in a 2D matrix.

- **In-place Operations:**
  - Performing operations on data without creating a copy of the data structure.
  - Minimizing space complexity by modifying the matrix in place.

- **Matrix Transposition:**
  - Understanding the concept of transposing a matrix (swapping rows and columns).
  - Implementing matrix transposition as a step in the rotation process.

- **Reversing Rows in a Matrix:**
  - Manipulating rows of a matrix by reversing their order as part of the rotation process.

- **Nested Loops:**
  - Using nested loops to iterate through 2D data structures like matrices.
  - Modifying elements within nested loops to achieve the desired rotation.

### Resources:

- **Python Official Documentation:**
  - Data Structures (list comprehensions, nested list comprehension)
  - More on Lists

- **GeeksforGeeks Articles:**
  - Inplace rotate square matrix by 90 degrees
  - Transpose a matrix in Single line in Python

- **TutorialsPoint:**
  - Python Lists for basics of list manipulation in Python.

By understanding these concepts and utilizing the provided resources, one will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests the ability to manipulate 2D matrices but also challenges to think about optimizing the solution to operate in-place, thus improving problem-solving and algorithmic thinking skills in Python.

## Additional Resources

- Mock Technical Interview

## Requirements

### General

- **Allowed editors:** vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle style (version 2.8.0)
- Not allowed to import any module
- All modules and functions must be documented
- All files must be executable

## Tasks

### 0. Rotate 2D Matrix

**Prototype:** `def rotate_2d_matrix(matrix):`

Given an n x n 2D matrix, rotate it 90 degrees clockwise. Do not return anything. The matrix must be edited in-place. You can assume the matrix will have 2 dimensions and will not be empty.

Example:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
Output:

lua
Copy code
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Repo:

GitHub repository: alx-interview
Directory: 0x07-rotate_2d_matrix
File: 0-rotate_2d_matrix.py
