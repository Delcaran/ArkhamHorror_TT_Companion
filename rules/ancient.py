import board

class Ancient():
    def __init__(self, doom_track_size:int=20) -> None:
        self._doom_track_size : int = doom_track_size
        self._doom_tokens : int = 0

    def doom_track_full(self) -> bool:
        return self._doom_tokens == self._doom_track_size
