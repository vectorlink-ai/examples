import matplotlib.pyplot as plt
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--distance-file", help="location of distance sample", required=True)
    args = parser.parse_args()

    with open(args.distance_file) as f:
        distances = json.load(f)

    plt.plot(distances[:5000])
    plt.ylabel('distance')
    plt.xlabel('distance ordered examples')
    plt.show()

    first_derivative = []
    for (d1,d2) in zip(distances[:5000-1],distances[1:5000]):
        first_derivative.append(d2-d1)

    plt.plot(first_derivative)
    plt.ylabel('rate of change of distance')
    plt.xlabel('distance ordered examples')
    plt.show()
