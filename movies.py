
def filter_by_genre(movies, genre):
    """
    Erstellt eine neue Liste, die aus der Gesamtliste, nach Genre gefilterte Filme,
    enthält
    """
    genre = genre.lower()
    movies_genres = [item for item in movies if genre == item["Genre"].lower()]
    return movies_genres

def create_movie(title, year, genre):
    """
        Erstellt ein Film-Dictionary.

        title: str - Filmtitel
        year: int - Erscheinungsjahr
        genre: str - Genre des Films

        Gibt zurück: dict mit Titel, Jahr und Genre
    """

    if type(title) != str:
        raise ValueError("Der Titel muss ein Text sein")
    elif type(year) != int:
        raise ValueError("Bitte nur die Jahreszahl eingeben: Bsp. 1988")
    else:
        movie = {"Titel": title, "Jahr": year, "Genre": genre}

    return movie


movies = [
    create_movie("Riddick: Chronik eines Kriegers",2004,"Skifi Action"),
    create_movie("Leon der Profi",1994,"Action"),
    create_movie("Das Leben des Brian",1979,"Komödie"),
    create_movie("Sister Act - Eine himmliche Karriere",1992,"Komödie"),
    create_movie("Matrix",1999 ,"Action"),
    create_movie("Underword",2003,"Action"),
    create_movie("Und täglich grüßt das Murmeltier",1993,"Komödie"),
    create_movie("Einer flog über das Kuckucksnest",1975,"Drama"),
    create_movie("Das Schweigen der Lämmer",1991,"Horror/Krimi"),
    create_movie("Tanz der Teufel",1981,"Horror")]


if __name__=="__main__":
    print(filter_by_genre(movies, "komödie"))
    print(filter_by_genre(movies, "SKIFY"))