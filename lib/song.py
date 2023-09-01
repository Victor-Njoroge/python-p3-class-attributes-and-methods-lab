class Song:
    count=0
    genre_count=0
    name=[]
    genre=[]
    artist=[]
    def __init__(self,name,artist,genre):
        if genre not in Song.genre:
            Song.genre.append(genre)
            Song.add_to_genre_count()

        if name not in Song.name:
            Song.name.append(name)

        if artist not in Song.artist:
            Song.artist.append(artist)




    @classmethod
    def add_song_to_count (cls,increment=1):
        cls.count +=increment

    @classmethod
    def add_to_genres(cls,genre):
        cls.genre.append(genre)
    
    @classmethod
    def add_to_name(cls,name):
        cls.name.append(name)
    @classmethod
    def add_to_artist(cls,artist):
        cls.artist.append(artist)

    @classmethod
    def add_to_genre_count(cls,increment=1):
        cls.genre_count += increment
        print(f"{cls.genre} : {cls.genre_count}")

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

ninety_nine_problems.name


ninety_nine_problems.artist
# "Jay-Z"

ninety_nine_problems.genre
# "Rap"