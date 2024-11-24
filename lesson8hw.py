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

class Car(Transport):
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} {self.color} {self.issue_year} проехала {Transport.mileage} километров"

class Airplane(Transport):
    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} {self.color} {self.issue_year} пролетел {Transport.mileage} километров"

