"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self, name):
        self._name = name
        self._content = []
        
    @property
    def name(self) -> str:
        return self._name
    
    def get_content(self):
        return self._content
    
    def add_content(self, cont):
        self._content.append(cont)
        
    def remove_content(self, cont):
        self._content.remove(cont)
        
    
        
