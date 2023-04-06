from pydantic import BaseModel, PrivateAttr

class Ancient(BaseModel):
    _doom_track_size : int = PrivateAttr()
    _doom_tokens : int = PrivateAttr()

    @property
    def doom_track_full(self) -> bool:
        return self._doom_tokens == self._doom_track_size
