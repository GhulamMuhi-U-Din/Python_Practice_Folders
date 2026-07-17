# Create Engine class
class Engine:

    # Create start method
    def start(self):

        # Display message
        print("Engine Started")


# Create Car class
class Car:

    # Initialize Car object
    def __init__(self):

        # Create an Engine object
        self.engine = Engine()


# Create Car object
car = Car()

# Access the engine inside car and call its start method
car.engine.start()