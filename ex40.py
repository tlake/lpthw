class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print "\n"
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you", "I don't want to get sued", \
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", \
    "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lyrics_rainy = ["Rainy day people always seem to know when it's time to call", \
    "Rainy day people don't talk, they just listen 'till they've heard it all", \
    "Rainy day lovers don't lie when they tell you that they've been down like you", \
    "Rainy day people don't mind if you cry out a tear or two"]

lyrics_snow = ["He stared into the night, no expectations", \
    "But in his heart he wanted to believe", \
    "That somehow someone would be waiting there", \
    "Upon this Christmas Eve"]

lyrics_highwayman = ["Still on a winter's night they say", \
    "When the wind is in the trees", "When the moon is a ghostly galleon", \
    "Tossed upon the cloudy seas", "When the road is a ribbon of moonlight", \
    "Over the purple moor", "A highwayman comes riding, riding, riding", \
    "A highwayman comes riding", "Up to the old inn door"]

rainy = Song(lyrics_rainy)

snow = Song(lyrics_snow)

highwayman = Song(lyrics_highwayman)

rainy.sing_me_a_song()

snow.sing_me_a_song()

highwayman.sing_me_a_song()
