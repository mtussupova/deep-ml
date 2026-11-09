import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    
    v1_len = 0
    v2_len = 0
    dot = 0
    for i in range(len(v1)):
        dot += v1[i]*v2[i]
        v1_len += v1[i]**2
        v2_len += v2[i]**2
    return dot/(np.sqrt(v1_len)*np.sqrt(v2_len))