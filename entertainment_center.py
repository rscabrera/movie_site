import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=iguEy4fFQAw")

star_wars = media.Movie("Star Wars: A Force Awakens",
                        "Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=gAUxw4umkdY")

school_of_rock = media.Movie("School of Rock",
                            "Using rock music to learn",
                            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                        "A rat is a chef in Paris",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                            "A really real reality show",
                            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, star_wars, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)
