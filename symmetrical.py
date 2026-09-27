def set_symmetric_difference(set1, set2):
    """
    Function to calculate symmetric difference between two sets.
    Arguments:
        set1 (set): First set
        set2 (set): Second set
    Returns:
        set: Elements present in either set1 or set2 but not both
    """
    return set1.symmetric_difference(set2)

# Example usage
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print("Set A:", A)
print("Set B:", B)
print("Symmetric Difference =", set_symmetric_difference(A, B))
