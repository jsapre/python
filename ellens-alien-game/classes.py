"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        """Create instance of Alien

        Args:
            x (_type_): _description_
            y (_type_): _description_
            health (_type_): _description_
        """
        Alien.total_aliens_created += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health

    def hit(self):
        """Register hit to decrement health"""
        self.health -= 1

    def is_alive(self):
        """Check if the Alien is alive with positive health

        Returns:
            _type_: _description_
        """
        return self.health > 0

    def teleport(self, new_x, new_y):
        """teleport the Alien to new coordinates

        Args:
            new_x (_type_): _description_
            new_y (_type_): _description_
        """
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other):
        pass


# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


def new_aliens_collection(alien_start_positions):
    result = []
    for position in alien_start_positions:
        result.append(Alien(*position))

    return result
