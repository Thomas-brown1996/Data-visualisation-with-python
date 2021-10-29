from random import choice

class Randomdroplet:
    """a class to generate random walks."""
    def __init__(self, num_points=5000):
        """initialise attributes of a walk"""
        self.num_points = num_points

        #all molecules start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_droplets(self):
        """calculate all the positions for the droplets"""
        #water keeps moving until movement reaches desired length
        while len(self.x_values) <self.num_points:

            #decide which direction water droplets are taking and how far
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_movement = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_movement = y_direction * y_distance

            #  reject moves that go nowhere
            if x_movement == 0 and y_movement == 0:
                continue

             #calculate the new position
            x = self.x_values[-1] + x_movement
            y = self.y_values[-1] + y_movement

            self.x_values.append(x)
            self.y_values.append(y)