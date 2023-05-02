from program import Program



class Serie(Program):
    """_summary_

    Args:
        Entertainment (_type_): _description_
    """

    def __init__(self, name: str, year: int, seasons: int) -> None:
        """_summary_

        Args:
            name (str): _description_
            year (int): _description_
            seasons (int): _description_
        """
        super().__init__(name, year)
        self.seasons = seasons


    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f'{self.name} - {self.year} - Seasons {self.seasons} - {self.like} Likes'

