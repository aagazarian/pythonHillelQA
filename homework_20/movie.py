from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format: str,
        year: int,
        rating: str,
        description: str,
        category: str,
        favorite: bool
    ):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category
        self.favorite = favorite

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies_in_xml = []

        for category in collection:
            for decade in category:
                for movie in decade:
                    item_title = movie.attrib["title"] if movie.attrib["title"] != "None provided." else None
                    item_favorite = movie.attrib["favorite"] if movie.attrib["favorite"] != "None provided." else None
                    item_format = movie.find("format").text if movie.find("format").text != "None provided." else None
                    item_year = movie.find("year").text if movie.find("year").text != "None provided." else None
                    item_rating = movie.find("rating").text if movie.find("rating").text != "None provided." else None
                    item_description = " ".join(movie.find("description").text.split()) \
                        if " ".join(movie.find("description").text.split()) != "None provided." else None
                    item_category = category.get("category") if category.get("category") != "None provided." else None

                    item = Movie(
                        item_title,
                        item_format,
                        item_year,
                        item_rating,
                        item_description,
                        item_category,
                        item_favorite
                    ) if movie.attrib["title"] != "None provided." else None

                    movies_in_xml.append(item)
        return movies_in_xml
