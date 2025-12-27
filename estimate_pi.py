import numpy as np

def estimate_pi(num_samples):
    points = np.random.rand(num_samples, 2)
    
    squared_distances = (points[:, 0] ** 2) + (points[:, 1] ** 2)
    inside_circle_count = np.sum(squared_distances <= 1)
    
    return 4 * inside_circle_count / num_samples
