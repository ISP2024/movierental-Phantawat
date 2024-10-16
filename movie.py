from dataclasses import dataclass, field
from typing import Collection

@dataclass(frozen=True)
class Movie:
    """A movie that can be rented."""
    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)
    
    def is_genre(self, genre_name: str) -> bool:
        """Check if the movie belongs to the given genre (case-insensitive)."""
        return genre_name.lower() in (g.lower() for g in self.genre)
    
    def __str__(self):
        """Return a string representation of the movie as 'Title (year)'."""
        return f"{self.title} ({self.year})"
