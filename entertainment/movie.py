import datetime
from program import Program



class Movie(Program):
    """_summary_

    Args:
        Entertainment (_type_): _description_
    """

    def __init__(self, name: str, year: int, duration: datetime) -> None:
        """_summary_

        Args:
            name (str): _description_
            year (int): _description_
            duration (datetime): _description_
        """
        super().__init__(name, year)
        self.duration = duration

    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f'{self.name} - {self.year} - Duration {self.duration} - {self.like} Likes'
