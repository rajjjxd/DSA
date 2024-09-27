# Function to add two matrices
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    
    return result

# Example matrices
matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

matrix2 = [[9, 8, 7], 
           [6, 5, 4], 
           [3, 2, 1]]

# Adding the matrices
result = add_matrices(matrix1, matrix2)

# Displaying the result
for row in result:
    print(row)