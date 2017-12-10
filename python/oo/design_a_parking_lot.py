from abc import ABC, abstractmethod
from enum import Enum
import random


class Sizes(Enum):
    xs = 1
    s = 2
    m = 3
    l = 4
    xl = 5


class Vehicle(ABC):
    def __init__(self, size, license_plate):
        self.size = size
        self.license_plate = license_plate

    def __str__(self):
        return "Vehicle [size: {}, license: {}]".format(self.size.name, self.license_plate)


class ParkingLot(object):
    def __init__(self, zipcode, spots):
        self.spots = spots
        self.zipcode = zipcode
        self.available_spots = {}
        for size in list(Sizes):
            self.available_spots[size] = []

        for spot in spots:
            self.available_spots[spot.size].append(spot)

    def place_vehicle(self, vehicle):
        # use a hash map to keep track of which spot is any vehicle
        # in, because this is going to help with finding as quick
        # as possible the car in the parking lot
        pass

    def remove_vehicle(self, spot_id):
        pass


class Spot(object):
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size

    def __str__(self):
        return "Spot [id: {}, size: {}]".format(self.spot_id, self.size.name)


if __name__ == "__main__":
    v1 = Vehicle(Sizes.m, "SJGOO1")

    spots = [Spot(spot_id, Sizes(1 + int(random.random() * 10) % 5)) for spot_id in range(100)]

    pl = ParkingLot(283091, spots)
    for stack_name, spots in pl.available_spots.items():
        print(stack_name, len(spots))


