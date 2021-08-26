import matplotlib.pyplot as plt
from generators import ClusterGenerator

def main():
    num_clusters = 5
    range_x = (-20,20)
    range_z = (-20,20)
    range_points = (10, 20)
    max_deviation = 3

    generator = ClusterGenerator()
    datapoints = generator.create_clusters_2D(num_clusters, range_x, range_z, range_points, max_deviation)

    c = [datapoint[0] for datapoint in datapoints]
    x = [datapoint[1] for datapoint in datapoints]
    y = [datapoint[2] for datapoint in datapoints]

    plt.scatter(x, y, c=c)
    plt.title('2D Clusters')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == "__main__":
    main()
