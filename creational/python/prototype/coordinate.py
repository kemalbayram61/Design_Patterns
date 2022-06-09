import copy

class coordinate:
    ___x = 0
    ___y = 0
    ___z = 0

    def get_coordinate_clone(self):
        return copy.copy(self)

    def get_x(self):
        return self.___x

    def set_x(self, new_x):
        self.___x = new_x
        pass

    def get_y(self):
        return self.___y

    def set_y(self, new_y):
        self.___y = new_y
        pass

    def get_z(self):
        return self.___z

    def set_z(self, new_z):
        self.___z = new_z
        pass

    def __str__(self):
        return "X:" + str(self.___x) + " Y:" + str(self.___y) + " Z:" + str(self.___z)


coordinate1 = coordinate()
print(coordinate1)
coordinate2 = coordinate1.get_coordinate_clone()
print(coordinate2)
coordinate2.set_x(1)
print("################")
print(coordinate1)
print(coordinate2)