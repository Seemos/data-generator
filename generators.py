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

    def create_clusters_3D(self, num_clusters, range_x, range_y, range_z, range_points, max_distance, seed=42):
        datapoints = []
        random.seed(seed)
        for cluster in range(num_clusters):
            center_x = random.uniform(*(range_x))
            center_y = random.uniform(*(range_y))
            center_z = random.uniform(*(range_z))
            for i in range(random.randint(*(range_points))):
                datapoint = []
                datapoint.append(cluster)
                datapoint.append(center_x + random.uniform(-max_distance, max_distance))
                datapoint.append(center_y + random.uniform(-max_distance, max_distance))
                datapoint.append(center_z + random.uniform(-max_distance, max_distance))
                datapoints.append(datapoint)
        return datapoints

class FunctionGenerator:

    def create_data_2d(self, function, range_x, num_datapoints, max_distance, seed=42):
        datapoints = []
        for i in range(num_datapoints):
            x = random.uniform(*(range_x))
            y = function(x) + random.uniform(-max_distance, max_distance)
            datapoints.append([x,y])
        return datapoints

    def create_data_3d(self, function, range_x, range_y, num_datapoints, max_distance, seed=42):
        datapoints = []
        for i in range(num_datapoints):
            x = random.uniform(*(range_x))
            y = random.uniform(*(range_y))
            z = function(x,y) + random.uniform(-max_distance, max_distance)
            datapoints.append([x,y,z])
        return datapoints