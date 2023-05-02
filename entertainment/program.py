


class Program: 
    
    def __init__(self, name: str, year: int) -> None:
        self.__name = name
        self.year = year
        self.__like = 0


    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, name: str) -> None:
        self.__name = name.title()


    @property
    def like(self) -> int:
        return self.__like
    

    @like.setter
    def like(self, like: int) -> None:
        self.__like = like 


    def give_like(self) -> None:
        self.like += 1
        
    
    def __str__(self) -> str:
        return f'{self.name} - {self.year} - {self.like} Likes'
    

