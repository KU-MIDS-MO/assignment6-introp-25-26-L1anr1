import numpy as np

def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)
    
    norms = np.linalg.norm(M, axis=1, keepdims=True)
    
    M_normalized = M / norms
    
    return M_normalized
