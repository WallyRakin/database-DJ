from models import db, Song, connect_db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:pass@localhost/playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# List of songs and artists
songs_list = [
    "Adele - Easy On Me",
    "Lil Nas X - MONTERO (Call Me By Your Name)",
    "Doja Cat ft. SZA - Kiss Me More",
    "Olivia Rodrigo - drivers license",
    "The Weeknd - Save Your Tears",
    "Dua Lipa - Levitating",
    "BTS - Butter",
    "Bruno Mars & Anderson .Paak (Silk Sonic) - Leave The Door Open",
    "Cardi B - Up",
    "Justin Bieber ft. Daniel Caesar & Giveon - Peaches",
    "Masked Wolf - Astronaut In The Ocean",
    "The Kid LAROI & Justin Bieber - STAY",
    "Olivia Rodrigo - good 4 u",
    "Ed Sheeran - Bad Habits",
    "Doja Cat - Need To Know",
    "Billie Eilish - Happier Than Ever",
    "Lizzo ft. Cardi B - Rumors",
    "Måneskin - Beggin'",
    "Saweetie ft. Doja Cat - Best Friend",
    "Glass Animals - Heat Waves",
    "The Weeknd - Take My Breath",
    "Lil Nas X & Jack Harlow - INDUSTRY BABY",
    "Megan Thee Stallion - Thot Shit",
    "Doja Cat - Woman",
    "BTS - Permission to Dance",
    "Ed Sheeran - Shivers",
    "Ariana Grande - positions",
    "Lil Nas X - THATS WHAT I WANT",
    "Olivia Rodrigo - traitor",
    "Drake ft. Future & Young Thug - Way 2 Sexy",
    "The Kid LAROI - WITHOUT YOU",
    "Justin Bieber - Hold On",
    "Billie Eilish - Therefore I Am",
    "Doja Cat - Streets",
    "Dua Lipa - Love Again",
    "BTS - Dynamite",
    "Bad Bunny & Jhay Cortez - DÁKITI",
    "Megan Thee Stallion ft. Beyoncé - Savage Remix",
    "24kGoldn ft. iann dior - Mood",
    "Chris Brown & Young Thug - Go Crazy",
    "Pop Smoke ft. Lil Baby & DaBaby - For The Night",
    "Ariana Grande - 34+35",
    "DaBaby ft. Roddy Ricch - ROCKSTAR",
    "Gabby Barrett ft. Charlie Puth - I Hope",
    "The Weeknd - Blinding Lights",
    "Harry Styles - Watermelon Sugar",
    "SZA - Good Days",
    "Roddy Ricch - The Box",
    "Future ft. Drake - Life Is Good",
    "Lewis Capaldi - Before You Go",
    "Dua Lipa - Don't Start Now",
    "Post Malone - Circles",
    "Jawsh 685 & Jason Derulo - Savage Love (Laxed – Siren Beat)",
    "Saint Jhn - Roses (Imanbek Remix)",
    "Billie Eilish - bad guy",
    "Doja Cat - Say So",
    "Lady Gaga & Ariana Grande - Rain On Me",
    "Rod Wave ft. Polo G - Richer",
    "The Weeknd ft. Ariana Grande - Save Your Tears Remix",
    "DJ Khaled ft. Drake - POPSTAR",
    "Cardi B ft. Megan Thee Stallion - WAP",
    "DaBaby - BOP",
    "Jack Harlow - WHATS POPPIN",
    "Harry Styles - Adore You",
    "Luke Combs - Forever After All",
    "Moneybagg Yo - Wockesha",
    "Pop Smoke - What You Know Bout Love",
    "Machine Gun Kelly & blackbear - my ex's best friend",
    "AJR - Bang!",
    "Internet Money & Gunna ft. Don Toliver & NAV - Lemonade",
    "Justin Bieber ft. Chance the Rapper - Holy",
    "Taylor Swift - willow",
    "Drake ft. Lil Durk - Laugh Now Cry Later",
    "BRS Kash - Throat Baby (Go Baby)",
    "Morgan Wallen - Wasted On You",
    "Luke Combs - Better Together",
    "Chris Brown & Young Thug - City Girls",
    "Pop Smoke ft. 50 Cent & Roddy Ricch - The Woo",
    "J. Cole ft. 21 Savage & Morray - m y . l i f e",
    "Dua Lipa ft. DaBaby - Levitating",
    "Megan Thee Stallion - Body",
    "Justin Bieber ft. Benny Blanco - Lonely",
    "The Weeknd - In Your Eyes",
    "Saweetie ft. Jhené Aiko - Back to the Streets",
    "Lil Baby - On Me",
    "Moneybagg Yo - Time Today",
    "Lil Tjay ft. 6LACK - Calling My Phone",
    "Pop Smoke ft. A Boogie Wit da Hoodie - Hello",
    "Coi Leray ft. Lil Durk - No More Parties",
    "Lil Baby & Lil Durk - Voice of the Heroes",
    "Morgan Wallen - Sand in My Boots",
    "Lil Baby & Lil Durk - How It Feels",
    "Lil Baby - Real As It Gets",
    "Lil Durk ft. Lil Baby - Finesse Out The Gang Way",
    "Lil Baby - Errbody",
    "Lil Durk - Backdoor",
    "Lil Baby & Lil Durk - Man of my Word",
    "Lil Baby & Lil Durk - Still Hood",
    "Lil Baby & Lil Durk - Who I Want",
    "Lil Baby & Lil Durk - Still Runnin"
]


def seed_songs():
    for song in songs_list:
        artist, title = song.split(" - ")
        new_song = Song(title=title.strip(), artist=artist.strip())
        db.session.add(new_song)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()  # Ensure tables are created
        seed_songs()  # Seed the songs
