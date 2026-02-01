import numpy as np

def get_random_subset_of_naturals_up_to_20():
    candidates = np.arange(1, 21)
    
    mask = np.random.randint(0, 2, size=20)
    
    bool_mask = mask.astype(bool)
    
    return candidates[bool_mask]
