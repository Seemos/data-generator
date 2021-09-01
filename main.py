import matplotlib.pyplot as plt
from generators import ClusterGenerator
from generators import FunctionGenerator

def main():
    num_clusters = 5
    range_x = (-20,20)
    range_y = (-20,20)
    range_z = (-20,20)
    range_points = (10, 20)
    max_deviation = 3

    generator = ClusterGenerator()
    datapoints_2D = generator.create_clusters_2D(num_clusters, range_x, range_y, range_points, max_deviation)

    c_2D = [datapoint[0] for datapoint in datapoints_2D]
    x_2D = [datapoint[1] for datapoint in datapoints_2D]
    y_2D = [datapoint[2] for datapoint in datapoints_2D]

    datapoints_3D = generator.create_clusters_3D(num_clusters, range_x, range_y, range_z, range_points, max_deviation)

    c_3D = [datapoint[0] for datapoint in datapoints_3D]
    x_3D = [datapoint[1] for datapoint in datapoints_3D]
    y_3D = [datapoint[2] for datapoint in datapoints_3D]
    z_3D = [datapoint[3] for datapoint in datapoints_3D]

    plt.scatter(x_2D, y_2D, c=c_2D)
    plt.title('2D Clusters')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("clusters_2D")
    plt.show()


    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(x_3D, y_3D, z_3D, c=c_3D)
    plt.title("3D Clusters")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("clusters_3D")
    plt.show()

    def parabula(x):
        return x**2 - 3

    generator = FunctionGenerator()
    datapoints = generator.create_data_2d(parabula, (-5,5), 30, 3)
    data_x = [datapoint[0] for datapoint in datapoints]
    data_y = [datapoint[1] for datapoint in datapoints]
    plt.scatter(data_x, data_y)
    plt.title("2D Function Data")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("function_2D")
    plt.show()

    def function_3d(x,y):
        return x**2 - y**2
    
    datapoints = generator.create_data_3d(function_3d, (-8,8), (-8,8), 500, 3)
    data_x = [datapoint[0] for datapoint in datapoints]
    data_y = [datapoint[1] for datapoint in datapoints]
    data_z = [datapoint[2] for datapoint in datapoints]
    
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(data_x, data_y, data_z, c = data_z)
    plt.title("3D Function Data")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig("function_3D")
    plt.show()

if __name__ == "__main__":
    main()
