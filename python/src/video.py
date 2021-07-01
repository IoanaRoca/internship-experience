"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)
        self._is_paused = False
        self._flagged = False
        self._flag_res = None

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    
    @property
    def flag_res(self) -> str:
        if self._flag_res != None:
            return self._flag_res
    
    def set_pause(self, val):
        self._is_paused = val
        
    def get_pause(self):
        return self._is_paused
    
    def set_flag(self, val):
        self._flagged = val
        
    def get_flag(self):
        return self._flagged
    
    def set_flag_res(self, val):
        self._flag_res = val
    
    
