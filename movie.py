import csv
import logging
from dataclasses import dataclass, field
from typing import Collection, Optional
from datetime import datetime


class MovieCatalog:
    """A singleton class to encapsulate and manage movie creation from a CSV file."""
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self, movie_file: str = "movies.csv"):
        if not hasattr(self, "_movies"):
            self._movies = {}
            self._load_movies(movie_file)

    def _load_movies(self, movie_file: str):
        """Load movies from a CSV file into the catalog."""
        try:
            with open(movie_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line_num, row in enumerate(reader, start=1):
                    # Ignore blank lines and comments
                    if not row or row[0].startswith('#'):
                        continue

                    try:
                        movie_id, title, year, genres = row
                        year = int(year)
                        genre_list = genres.split('|')
                        movie = Movie(title, year, genre_list)
                        
                        # Store in dictionary using (title, year) as key
                        if (title.lower(), year) not in self._movies:
                            self._movies[(title.lower(), year)] = movie
                        else:
                            logging.warning(f"Duplicate movie '{title}' ({year}) on line {line_num}")

                    except ValueError as e:
                        logging.error(f"Invalid data on line {line_num}: {row} - {str(e)}")

        except FileNotFoundError:
            logging.error(f"Movie file '{movie_file}' not found.")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Retrieve a movie by title and optional year."""
        if year:
            return self._movies.get((title.lower(), year))
        else:
            # Find the first movie that matches the title
            for (movie_title, _), movie in self._movies.items():
                if movie_title == title.lower():
                    return movie
        return None
    

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
    

NEW_RELEASE = "New Release"
CHILDRENS = "Childrens"
REGULAR = "Regular"

def price_code_for_movie(movie: Movie) -> str:
    """Determine the price code for a movie based on its release year and genre."""
    current_year = datetime.now().year

    if movie.year == current_year:
        return NEW_RELEASE
    elif movie.is_genre("Children") or movie.is_genre("Childrens"):
        return CHILDRENS
    else:
        return REGULAR
