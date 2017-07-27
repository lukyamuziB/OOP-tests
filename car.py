

class Car(object):
    """A car class that describes certain attributes of Cars"""
    def __init__(self, name='General', model='GM', type=None):
        self.type = type
        self.name = name 
        self.model = model

        if self.name == "Porshe":
            self.num_of_doors = 2
        elif self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4


        if self.type == "trailer":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        self.speed = 0

    def drive(self, speed):
        
        if self.name =="Mercedes":
            self.speed = 1000
        else:
            self.speed = 77

        return self

    def is_saloon(self):
        if self.type != "trailer":
            return "saloon"
        return "trailer"


# git remote add origin https://github.com/lukyamuziB/opoo.git
# git push -u origin master