from abc import ABC, abstractmethod

class Transport(ABC):
    brand: str
    model: str
    issue_year: int
    color: str
    mileage = 0

    @abstractmethod
    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    @abstractmethod
    def move(self, num_km):
        if num_km > 0:
            Transport.mileage += num_km
            return Transport.mileage
        else:
            print("ValueError: Расстояние должно быть положительным числом")

#проверка =========================================================================
# transport = Transport("Jeep", "Renegade", 2015, "Red")
# # print(Transport.mileage)
# # transport.move(10)
# # print(Transport.mileage)
# # transport.move(20)
# # print(Transport.mileage)
# transport.move(-1)
# # print(Transport.mileage)
#===================================================================================
class Car(Transport):
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(self, brand, model, issue_year, color)
        self.engine_type = engine_type


     def move(self, num_km):
         super().move()
         return f"{self.brand}, {self.model}, {self.color}, {self.issue_year},проехала {Transport.mileage} километров"

car = Car("Jeep", "Renegade", 2015, "Red", "Petrol")
# car.move(1)









