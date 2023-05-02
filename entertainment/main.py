import movie
import serie
import playlist


def main():

    avengers = movie.Movie('Avengers - Infinity War', 2018, 160)
    atlanta = serie.Serie('Atlanta', 2018, 2)
    matrix = movie.Movie('Matrix', 1999, 120)

    matrix.give_like()
    matrix.give_like()
    matrix.give_like()
    avengers.give_like()
    atlanta.give_like()
    avengers.give_like()
    movies_n_series = [avengers, atlanta, matrix]

    weekend_playlist = playlist.Playlist('Weekend Playlist', movies_n_series)
    print(len(weekend_playlist))

    [print(program) for program in weekend_playlist]


if __name__ == '__main__':
    main()
