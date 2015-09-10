
import fresh_tomatoes
import media


toy_story = media.Movie('Toy Story',
                         'A story of a boy',
                         'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                         'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                      'A marine on planet',
                      'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                      'https://www.youtube.com/watch?v=cRdxXPV9GNQ')
                     
dragonballz = media.Movie('Dragon Ball Z: Battle of Gods',
                           'Adventures of Z fighters',
                           'http://upload.wikimedia.org/wikipedia/en/d/da/DragonBallZ-BattleofGods-poster.jpeg',
                           'https://www.youtube.com/watch?v=imiryMHYPB0')

inglorious = media.Movie('Inglorious Basterds',
                          'Nazi fighting Bear Jew and all that...',
                          'http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg',
                          'https://www.youtube.com/watch?v=prj3URvxcHU')

movies = [toy_story, avatar, dragonballz, inglorious]
print (media.Movie.__name__)

