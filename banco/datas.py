from datetime import date


class Data:

    def __init__(self, d, m, y) -> None:
        self.d = d
        self.m = m
        self.y = y
    

    def formatada(self):
        return date(day=self.d, month=self.m, year=self.y).strftime("%d/%m/%Y")
