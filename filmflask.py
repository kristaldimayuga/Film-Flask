movie_library={
'name':"20 Days in Mariupol",'name':"A Haunting in Venice",
'name':"American Fiction",
'name':"American Symphony",
'name':"Anatomy of a Fall",
'name':"Ant-Man and the Wasp: Quantumania",
'name':"Anyone But You",
'name':"Aquaman and the Lost Kingdom",
'name':"Barbie",
'name':"Blue Beetle",
'name':"Bobi Wine: The People's President",
'name':"Creed III",
'name':"Detective Conan: Black Iron Submarine",
'name':"Dungeons & Dragons: Honor Among Thieves",
'name':"El Conde",
'name':"Elemental",
'name':"Evil Dead Rise",
'name':"Fast X",
'name':"Five Nights at Freddy's",
'name':"Flamin' Hot",
'name':"Four Daughters",
'name':"Godzilla Minus One",
'name':"Golda",
'name':"Gran Turismo",
'name':"Guardians of the Galaxy Vol. 3",
'name':"Haunted Mansion",
'name':"Indiana Jones and the Dial of Destiny",
'name':"Insidious: The Red Door",
'name':"Invincible",
'name':"Io Capitano",
'name':"Island in Between",
'name':"John Wick: Chapter 4",
'name':"Killers of the Flower Moon",
'name':"Knight of Fortune",
'name':"Letter to a Pig",
'name':"Maestro",
'name':"May December",
'name':"Meg 2: The Trench",
'name':"Migration",
'name':"Mission: Impossible - Dead Reckoning Part One",
'name':"Napoleon",
'name':"Nimona",
'name':"Ninety-Five Senses",
'name':"Nyad",
'name':"Nǎi Nai & Wài Pó",
'name':"Oppenheimer",
'name':"Our Uniform",
'name':"PAW Patrol: The Mighty Movie",
'name':"Pachyderme",
'name':"Past Lives",
'name':"Pathaan",
'name':"Perfect Days",
'name':"Poor Things",
'name':"Red, White and Blue",
'name':"Robot Dreams",
'name':"Rustin",
'name':"Saw X",
'name':"Scream VI",
'name':"Shazam! Fury of the Gods",
'name':"Society of the Snow",
'name':"Sound of Freedom",
'name':"Spider-Man: Across the Spider-Verse",
'name':"Taylor Swift: The Eras Tour",
'name':"Teenage Mutant Ninja Turtles: Mutant Mayhem",
'name':"The ABCs of Book Banning",
'name':"The After",
'name':"The Barber of Little Rock",
'name':"The Boy and the Heron",
'name':"The Color Purple",
'name':"The Creator",
'name':"The Equalizer 3",
'name':"The Eternal Memory",
'name':"The Exorcist: Believer",
'name':"The Flash",
'name':"The Holdovers",
'name':"The Hunger Games: The Ballad of Songbirds & Snakes",
'name':"The Last Repair Shop",
'name':"The Little Mermaid",
'name':"The Marvels",
'name':"The Nun II",
'name':"The Super Mario Bros. Movie",
'name':"The Teachers' Lounge",
'name':"The Wonderful Story of Henry Sugar",
'name':"The Zone of Interest",
'name':"To Kill a Tiger",
'name':"Transformers: Rise of the Beasts",
'name':"Trolls Band Together",
'name':"Wish",
'name':"Wonka"
}


user_info={}

def signup():
    print("\nSignup to a new account")
    username=input("Enter new username: ")
    if username in user_info:
        print("this username already exists")
    else:
        password=str(input("Enter your password: "))
        if len(password) < 8 :
            print("Password must be at least 8 characters.")
        else:
            user_info[username]={'password':password}
            print("Signup successful!")
            main()

def login():
    print("\nLog-in")
    username=str(input("username: "))
    password=str(input("password: "))
    if username in user_info and user_info[username]['password']== password:
        print("log-in successful!")
        u_menu(username)
    else:
        print("invalid password/ account does not exist.")
        return
    
def u_menu():
    pass

def main():
    while True:
        print("Film Flask")
        print("Rate and review our curated collection of the best movies of 2023.")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice=int(input("Enter your choice: "))

        try:
            if choice==1:
                signup()
            elif choice==2:
                login()
            elif choice==3:
                print("\nExiting Program...")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-3.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
main()