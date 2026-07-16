"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    pass


#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates
"""Solution to Ellen's Alien Game exercise."""


from modulefinder import test


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    pass
class Alien:
    """Create an Alien object with location and health tracking."""
    
    # Class attribute to keep track of total aliens created
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize alien coordinates, starting health, and increment counter."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        
        # Increment the total alien count upon instantiation
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement alien health by 1 point."""
        self.health -= 1

    def is_alive(self):
        """Return True if the alien's health is above 0, False otherwise."""
        return self.health > 0

    def teleport(self, new_x, new_y):
        """Change the alien's current coordinates to the new coordinates."""
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        """Placeholder for collision detection functionality."""
        pass


def new_aliens_collection(positions):
    """Create a list of Alien instances given a list of position tuples.

    :param positions: list - a list of tuples containing (x, y) coordinates.
    :return: list - a list of Alien objects.
    """
    return [Alien(x, y) for x, y in positions]




