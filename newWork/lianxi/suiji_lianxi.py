class Restaurant():
    '''
    .............................................
    '''
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("the restaurant is opening")

    def increment_number_served(self, increment):
        self.number_served =+ increment


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


ince = IceCreamStand("dwedw", "dwdw", "fe")
ince.describe_restaurant()




# ret = Restaurant("cofe", "no")
# ret.describe_restaurant()
# ret.open_restaurant()
# ret.increment_number_served(9)
# print(ret.number_served)

