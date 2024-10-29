class Vehicle:
    def __init__(self,name,mileage,max_speed):
        self.name=name
        self.mileage=mileage
        self.max_speed=max_speed

    def seating_capacity(self, capacity):
        return f"The seatiung capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, mileage, max_speed):
        # Initialize the Vehicle class
        super().__init__(name, mileage, max_speed)
        # Call the seating_capacity function with capacity set to 50
        print(super().seating_capacity(50))

# Usage
b = Bus("Redbus", 100, 200)




