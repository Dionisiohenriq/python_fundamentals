

class Playlist():

    def __init__(self, name: str, programs: list) -> None:
        self.name = name
        self._programs = programs

    def __getitem__(self, item: int) -> iter:
        return self._programs[item]

    def __len__(self) -> int:
        return self._programs.__len__()

    @property
    def listing(self):
        return self._programs
