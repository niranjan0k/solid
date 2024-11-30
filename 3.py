# 3. L => Liskov Substitution Principle (LSP)
# Object of a superclass should be replaceable with objects of its subclasses 
# without affecting the correctness of the program.
# Example

class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine ...")

class Bicycle(Vehicle):
    def start_engine(self):
        # That doesn't make sense for bicycle
        pass

# if we try to substitute a Bicycle instance where a Vehicle instance is expected,
# it might lead to unexpected behavior or errors.
# to overcome from the problem as follow -

class Vehicle:
    def start(self):
        raise NotImplementedError
    
class Car(Vehicle):
    def start(self):
        print("Starting car engine ...")

class Bicycle(Vehicle):
    def start(self):
        print('Pedaling the bicycle ...')

# Here we replace the start_engine method with more general start method in the base class Vehicle


