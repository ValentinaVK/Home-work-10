from abc import ABC, abstractmethod


class Clothes(ABC):

    
    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass

class Summa(Clothes):
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height
    
    def consumptions(self):
        return f'Сумма затраченной ткани равна: {self.widht / 6.5 + 0.5 + 2 * self.height + 0.3 :.2f}'

    def abstract(self):
        pass
    

coat = Coat(5)
costume = Costume(3)
sam = Summa(5,3)
print(coat.consumption())
print(costume.consumption())
print(sam.consumptions())
