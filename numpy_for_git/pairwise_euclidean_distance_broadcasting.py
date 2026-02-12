# Pairwise Euclidean Distance

import numpy as np
print('-'*100)
print("-------------Calculate pairwise Euclidean distance matrix for N points in D dimensions--------------")
print('-'*100)
def main3():

    try:
        num_points = int(input("Enter number of points (N): "))
        num_dimensions = int(input("Enter number of dimension (D): "))
        
        print(f"Enter {num_points*num_dimensions} elements (separated by space or comma):")
        input_str = input()
        
        if ',' in input_str:
            numbers = [int(x.strip()) for x in input_str.split(',')]
        else:
            numbers = [int(x) for x in input_str.split()]
            
        coords = np.array(numbers).reshape(num_points, num_dimensions)
        print('\n' )
        print("Original coordinates:")
        print('-'*30)
        for i in range(num_points):
            print(f"Point {i+1}: {', '.join(map(str, coords[i]))}")
        
        diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
        sqrd_diff = diff**2
        sumof_sqrd_diff = np.sum(sqrd_diff, axis=-1)
        pairwise_dist = np.sqrt(sumof_sqrd_diff)
        
        print(f"\nPairwise distance matrix (broadcasting) N X N = {num_points*num_points}:\n\n\n", pairwise_dist)
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        
        

main3()    