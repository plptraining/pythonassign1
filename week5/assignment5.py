# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Answer:

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call the base class constructor
        self.__storage = storage        # Encapsulated attribute
        self.__battery = battery        # Encapsulated attribute
        self.installed_apps = []        # Public attribute

    # Encapsulation: Getter and Setter
    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage

    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(f"{app_name} has been installed.")

    def show_status(self):
        return f"Storage: {self.__storage}GB, Battery: {self.__battery}%"

# Polymorphism: Different devices can have different versions of use()
def use_device(device):
    print("Using device:", device.device_info())
    print(device.show_status())

# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 128, 85)
phone1.install_app("Spotify")
phone1.set_storage(256)

# Print info
use_device(phone1)



# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Answer:

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

# Subclass 2
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

# Subclass 3
class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🚢"

# Subclass 4
class Train(Vehicle):
    def move(self):
        return "Chugging along the tracks 🚆"

# Function demonstrating polymorphism
def travel(vehicle: Vehicle):
    print(vehicle.move())

# Create instances
car = Car()
plane = Plane()
boat = Boat()
train = Train()

# Polymorphic behavior
vehicles = [car, plane, boat, train]
for v in vehicles:
    travel(v)
