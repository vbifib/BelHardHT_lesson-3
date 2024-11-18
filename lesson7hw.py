class Phone:

    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(name):
        print(f"Звонит {name}")

    def get_info(self):
        some_tuple = tuple([self.brand, self.model, self.issue_year])
        return some_tuple

    def __str__(self):
        some_dict = {
            'Бренд': self.brand,
            'Модель': self.model,
            'Год выпуска': self.issue_year

        }
        return some_dict


# phone1 = Phone("motorolla", "model 1", 1996)
# phone2 = Phone("erricson", "model 2", 1997)
#
# Phone.receive_call('Mike')
# print(phone1.get_info())
# # b = phone1.get_info()
# # print(type(b))
# print(phone2.__str__())










