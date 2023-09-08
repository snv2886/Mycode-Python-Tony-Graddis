# Класс CellPhone содержит данные о сотовом телефоне
class CellPhone:

    # Метод __init__() инициализирует атрибут.
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Method `set_manufact()` accept argument
    # for phone manufacturer.
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # Method `set_model()` accept argument
    # for phone model number.
    def set_model(self, model):
        self.__model = model

    # Method `set_retail_price()` accept argument
    # for phone retail price.
    def set_retail_price(self, price):
        self.__retail_price = price

    # Method `get_manufact()` returns
    # phone manufacturer
    def get_manufact(self):
        return self.__manufact

    # Method `get_model()` returns
    # phone model.
    def get_model(self):
        return self.__model

    # Method `get_retail_price() returns
    # phone retail price.
    def get_retail_price(self):
        return self.__retail_price
