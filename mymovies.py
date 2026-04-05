import os
def create_movie(title, year, genre):

    movie = {"Jahr": year, "Titel": title, "Genre": genre}

    return movie

def ausgabe(movie_list):
    index = 1
    datei = open("Filmliste.txt", "w")
    for item in movie_list:
        datei.write(f"Film Nr.:{index} | Filmtitel: {item["Titel"]} | Erschienen: {item["Jahr"]} | Genre: {item["Genre"]}\n")
        index += 1

    exit()


def main():
    movie_list = []
    abfrage = None

    while abfrage != True:

        try:
            title = input("Wie heißt der Film?:")
            year = int(input("Wann ist der Film erschienen?:"))
            genre = input("Zu welchem Genre gehört der Film?:")


        except ValueError:
            print("Bitte nur das Jahr angeben! Bsp.: 1989")

        else:
            movie_list.append(create_movie(title, year, genre))
            eingabe = input("Enter drücken für weiteren Film - exit eingeben für beenden")

            if eingabe == "exit":
                abfrage = True
                ausgabe(movie_list)

if __name__=="__main__":
    main()