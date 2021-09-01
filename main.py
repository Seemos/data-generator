import matplotlib.pyplot as plt
from generators import ClusterGenerator
from generators import FunctionGenerator

def main():
    example_cluster_2D()
    example_cluster_3D()
    example_function_data_2D()
    example_function_data_3D()

def example_cluster_2D():
    num_clusters = 5
    range_x = (-20,20)
    range_y = (-20,20)
    range_z = (-20,20)
    range_points = (10, 20)
    max_deviation = 3

    generator = ClusterGenerator()
    datapoints = generator.create_clusters_2D(num_clusters, range_x, range_y, range_points, max_deviation)

    c = [datapoint[0] for datapoint in datapoints]
    x = [datapoint[1] for datapoint in datapoints]
    y = [datapoint[2] for datapoint in datapoints]

    plt.scatter(x, y, c=c)
    plt.title('2D Clusters')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("clusters_2D")
    plt.show()

def example_cluster_3D():
    num_clusters = 5
    range_x = (-20,20)
    range_y = (-20,20)
    range_z = (-20,20)
    range_points = (10, 20)
    max_deviation = 3

    generator = ClusterGenerator()
    datapoints = generator.create_clusters_3D(num_clusters, range_x, range_y, range_z, range_points, max_deviation)

    c = [datapoint[0] for datapoint in datapoints]
    x = [datapoint[1] for datapoint in datapoints]
    y = [datapoint[2] for datapoint in datapoints]
    z = [datapoint[3] for datapoint in datapoints]

    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(x, y, z, c=c)
    plt.title("3D Clusters")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("clusters_3D")
    plt.show()

def example_function_data_2D():
    def parabula(x):
        return x**2 - 3

    generator = FunctionGenerator()
    datapoints = generator.create_data_2d(parabula, (-5,5), 30, 3)

    x = [datapoint[0] for datapoint in datapoints]
    y = [datapoint[1] for datapoint in datapoints]

    plt.scatter(x, y)
    plt.title("2D Function Data")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("function_2D")
    plt.show()

def example_function_data_3D():
    def function_3d(x,y):
        return x**2 - y**2
    
    generator = FunctionGenerator()
    datapoints = generator.create_data_3d(function_3d, (-8,8), (-8,8), 500, 3)

    x = [datapoint[0] for datapoint in datapoints]
    y = [datapoint[1] for datapoint in datapoints]
    z = [datapoint[2] for datapoint in datapoints]
    
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(x, y, z, c = z)
    plt.title("3D Function Data")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("function_3D")
    plt.show()

if __name__ == "__main__":
    main()
