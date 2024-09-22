class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f'Driving {self.model} {self.year} {self.color}')

    def stop(self):
        print(f'Stopping {self.model} {self.year} {self.color}')


car1 = Car('Toyota', 2020, 'Red')
car1.drive()
car1.stop()
