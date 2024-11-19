AGE_MAP = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}

SECONDS_IN_YEAR = 31_557_600


class SpaceAge:
    def __init__(self, seconds):
        self.age = seconds / SECONDS_IN_YEAR

    def on_mercury(self):
        return round(self.age / AGE_MAP["Mercury"], 2)

    def on_venus(self):
        return round(self.age / AGE_MAP["Venus"], 2)

    def on_earth(self):
        return round(self.age / AGE_MAP["Earth"], 2)

    def on_mars(self):
        return round(self.age / AGE_MAP["Mars"], 2)

    def on_jupiter(self):
        return round(self.age / AGE_MAP["Jupiter"], 2)

    def on_saturn(self):
        return round(self.age / AGE_MAP["Saturn"], 2)

    def on_uranus(self):
        return round(self.age / AGE_MAP["Uranus"], 2)

    def on_neptune(self):
        return round(self.age / AGE_MAP["Neptune"], 2)
