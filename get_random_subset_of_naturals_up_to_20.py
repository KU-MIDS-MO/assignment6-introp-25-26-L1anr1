import numpy as np

def get_random_subset_of_naturals_up_to_20():
    mask = np.random.randint(0, 2**20)
    
    candidates = np.arange(1, 21)
    
    shifts = np.arange(20)
    
    bool_index = ((mask >> shifts) & 1).astype(bool)

    return candidates[bool_index]
