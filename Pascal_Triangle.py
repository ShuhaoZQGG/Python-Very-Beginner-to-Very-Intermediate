def add_layer(triangle):
    # Add a layer to Pascal's triangle.
    # Each layer should be a tuple.
    end = triangle[-1]
    row = []
    for left, right in zip(end+(0,),(0,)+end):
        row.append(left+right)
    triangle.append(tuple(row))
    pass
    
    
pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
for _ in range(5):
    add_layer(pascals_triangle)
print(pascals_triangle)