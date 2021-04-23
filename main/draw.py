import matplotlib.pyplot as plt

def draw_infected_points(points):
    patches = []
    for point in points:
        circle = plt.Circle((point), 5, fc='None', ec='r')
        plt.gca().add_patch(circle)
        patches.append(circle)
    for point in points:
        circle = plt.Circle((point), 5, fc='#edc', ec='None')
        plt.gca().add_patch(circle)
        patches.append(circle)
    return patches


def draw_the_infection_source_point(point):
    circle = plt.Circle((point), 5, fc='y', ec='r')
    plt.gca().add_patch(circle)
    return [circle]

def draw_normal_points(points):
    patches = []
    for point in points:
        circle = plt.Circle((point), 5, fc='None', ec='b')
        plt.gca().add_patch(circle)
        patches.append(circle)
    for point in points:
        circle = plt.Circle((point), 5, fc='#abe', ec='None')
        plt.gca().add_patch(circle)
        patches.append(circle)
    return patches