import numpy as np
import random

class ClusterGenerator:

    def create_clusters_2D(self, num_clusters, range_x, range_y, range_points, max_distance, seed=42):
        datapoints = []
        random.seed(seed)
        for cluster in range(num_clusters):
            center_x = random.uniform(*(range_x))
            center_y = random.uniform(*(range_y))
            for i in range(random.randint(*(range_points))):
                datapoint = []
                datapoint.append(cluster)
                datapoint.append(center_x + random.uniform(-max_distance, max_distance))
                datapoint.append(center_y + random.uniform(-max_distance, max_distance))
                datapoints.append(datapoint)
        return datapoints
