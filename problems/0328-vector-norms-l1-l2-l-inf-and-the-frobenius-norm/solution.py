import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    res = float(0)
    if arr.ndim == 1:
        new_arr = arr
        if norm_type == 'frobenius':
            raise ValueError("Only 2D arrays are allowed")
    else:
        new_arr = arr.flatten()
    
    if norm_type == 'l1':
        for n in new_arr:
            res += np.abs(n)
    elif norm_type == 'l2':
        for n in new_arr:
            res += n**2
        res = np.sqrt(res)
    elif norm_type == 'linf':
        res = max(np.abs(new_arr))
    elif norm_type == 'frobenius':
        for n in new_arr:
            res += n**2
        res = np.sqrt(res)
    else:
        raise ValueError("There are no other norm types available")
    return float(res)
    
