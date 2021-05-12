class Flat:

    def __init__(self, kitchen, bedroom, bathroom):
        self.kitchen = kitchen
        self.bedroom = bedroom
        self.bathroom = bathroom

    def print_rooms(self):
        print(f'Rooms: {self.kitchen.TITLE}, {self.bedroom.TITLE}, {self.bathroom.TITLE}')

    def print_flat_size(self):
        print(f'Flat size: {self._calculate_flat_size()}')

    def print_kitchen_size(self):
        print(f'Kitchen size: {self.kitchen.get_size()}')

    def print_bedroom_size(self):
        print(f'Bedroom size: {self.bedroom.get_size()}')

    def print_bathroom_size(self):
        print(f'Bathroom size: {self.bathroom.get_size()}')

    def _calculate_flat_size(self):
        return self.kitchen.get_size() + self.bedroom.get_size() + self.bathroom.get_size()


class Kitchen:

    TITLE = 'Kitchen'

    def __init__(self, size):
        self.__size = size
        self.__purpose = 'To eat'

    def get_size(self):
        return self.__size


class Bedroom:

    TITLE = 'Bedroom'

    def __init__(self, size):
        self.__size = size
        self.__purpose = 'To sleep'

    def get_size(self):
        return self.__size


class Bathroom:

    TITLE = 'Bathroom'

    def __init__(self, size):
        self.__size = size
        self.__purpose = 'To wash'

    def get_size(self):
        return self.__size


my_kitchen = Kitchen(13)
my_bedroom = Bedroom(18)
my_bathroom = Bathroom(4)

my_flat = Flat(my_kitchen, my_bedroom, my_bathroom)

my_flat.print_rooms()
my_flat.print_flat_size()
my_flat.print_kitchen_size()
my_flat.print_bedroom_size()
my_flat.print_bathroom_size()
