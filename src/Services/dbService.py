import csv

database_path = "./Database/"

movieDbName = f"{database_path}movie.csv"
movieDbColumns = ["id", "title", "description", "duration_mins", "language", "release_date", "country", "genre"]

movieMediaDbName = f"{database_path}movieMedia.csv"
movieMediaDbColumns = ["id", "movieid", "cardsrcaddress", "detailbanneraddress"]

screeningDbName = f"{database_path}screening.csv"
screeningDbNameColumns = ["id", "movieid", "date", "starttime", "endtime", "hallid"]

# Function to create the initial CSV file
def create_csv_file(databaseName, columnNameList):
    with open(databaseName, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columnNameList)

# Function to get the next available ID
def get_next_id(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            existing_ids = [int(row['id']) for row in reader]

            if not existing_ids:  # Check if the list of existing IDs is empty
                return 1  # Start with 1 as the first ID
            else:
                return max(existing_ids) + 1
    except FileNotFoundError:
        return 1  # If the file doesn't exist, start with 1 as the first ID

# Function to add a new record to the CSV
def add_record(filename, record):
    next_id = get_next_id(filename)
    record['id'] = next_id

    with open(filename, 'a', newline='') as file:
        fieldnames = movieDbColumns  # Use your column names
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:  # If the file is empty, write the header row
            writer.writeheader()

        writer.writerow(record)
    
    # Close the file explicitly
    file.close()

# Function to read all records from the CSV
def read_all_records(csv_file):
    records = []
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records

# Function to search for a record by ID
def search_record_by_id(search_id, csv_file):
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == search_id:
                return row
    return None

# Function to update a record by ID
def update_record_by_id(update_id, new_data, columnNameList, csv_file):
    records = read_all_records()
    for record in records:
        if record["ID"] == update_id:
            record.update(new_data)
            break

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnNameList)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

def db_initial_setup_movie():
    create_csv_file(movieDbName, movieDbColumns)
    db_initial_insert_movie()

    create_csv_file(movieMediaDbName, movieMediaDbColumns)
    db_initial_insert_movie_meida()

def db_initial_insert_movie():
    # Define a list of movie records
    movie_records = [
        {
            'title': "The Nun II",
            'description': "1956 - France. A priest is murdered. An evil is spreading. The sequel to the worldwide smash hit follows Sister Irene as she once again comes face-to-face with Valak, the demon nun.",
            'duration_mins': 110,
            'language': "English",
            'release_date': "07/09/2023",
            'country': "United States",
            'genre': "Thriller"
        },
        {
            'title': "Five Nights at Freddy's",
            'description': "Can you survive five nights? The terrifying horror game phenomenon becomes a blood-chilling cinematic event, as Blumhouse— the producer of M3GAN, The Black Phone and The Invisible Man— brings Five Nights at Freddy's to the big screen. The film follows a troubled security guard as he begins working at Freddy Fazbear's Pizza. While spending his first night on the job, he realizes the night shift at Freddy's won't be so easy to make it through.",
            'duration_mins': 109,
            'language': "English",
            'release_date': "26/10/2023",
            'country': "United States",
            'genre': "Horror"
        },
        {
            'title': "Killers of the Flower Moon",
            'description': "Additional language: Sioux Based on David Grann's broadly lauded best-selling book, Killers of the Flower Moon is set in 1920s Oklahoma and depicts the serial murder of members of the oil-wealthy Osage Nation, a string of brutal crimes that came to be known as the Reign of Terror.",
            'duration_mins': 206,
            'language': "English",
            'release_date': "19/10/2023",
            'country': "Australia",
            'genre': "Crime"
        },
        {
            'title': "Uproar",
            'description': "UPROAR is a moving and heartwarming comedy about connection and finding your place in the world. 17-year-old Josh Waaka (Julian Dennison) is growing up in New Zealand in 1981. The rugby-obsessed country is divided over the arrival of the South African Springboks team, sparking nationwide protests. Josh, who has never felt like he fits in anywhere, is inspired by the protests and by a newfound passion for performing to find his own voice. After embracing his community and his Māori heritage, Josh and his family set out on a journey towards healing.",
            'duration_mins': 110,
            'language': "English",
            'release_date': "05/10/2023",
            'country': "United Kingdom",
            'genre': "Comedy"
        },
        {
            'title': "Taylor Swift | The Eras Tour",
            'description': "The cultural phenomenon continues on the big screen! Immerse yourself in this once-in-a-lifetime concert film experience with a breathtaking, cinematic view of the history-making tour. Taylor Swift Eras attire and friendship bracelets are strongly encouraged!",
            'duration_mins': 168,
            'language': "English",
            'release_date': "13/10/2023",
            'country': "New Zealand",
            'genre': "Concert"
        },
        {
            'title': "Oppenheimer",
            'description': "Written and directed by Christopher Nolan, Oppenheimer is an IMAX®-shot epic thriller that thrusts audiences into the pulse-pounding paradox of the enigmatic man who must risk destroying the world in order to save it. The film stars Cillian Murphy as J. Robert Oppenheimer and Emily Blunt as his wife, biologist and botanist Katherine Kitty Oppenheimer. Oscar® winner Matt Damon portrays General Leslie Groves Jr., director of the Manhattan Project, and Robert Downey, Jr. plays Lewis Strauss, a founding commissioner of the U.S. Atomic Energy Commission. Academy Award® nominee Florence Pugh plays psychiatrist Jean Tatlock, Benny Safdie plays theoretical physicist Edward Teller, Michael Angarano plays Robert Serber and Josh Hartnett plays pioneering American nuclear scientist Ernest Lawrence. Oppenheimer also stars Oscar® winner Rami Malek and reunites Nolan with eight-time Oscar® nominated actor, writer and filmmaker Kenneth Branagh.",
            'duration_mins': 180,
            'language': "English",
            'release_date': "20/07/2023",
            'country': "New Zealand",
            'genre': "Biography"
        },
        {
            'title': "Saw X",
            'description': "John Kramer (Tobin Bell) is back. The most disturbing installment of the Saw franchise yet explores the untold chapter of Jigsaw's most personal game. Set between the events of Saw I and II, a sick and desperate John travels to Mexico for a risky and experimental medical procedure in hopes of a miracle cure for his cancer - only to discover the entire operation is a scam to defraud the most vulnerable. Armed with a newfound purpose, the infamous serial killer returns to his work, turning the tables on the con artists in his signature visceral way through devious, deranged, and ingenious traps.",
            'duration_mins': 118,
            'language': "English",
            'release_date': "28/09/2023",
            'country': "United States",
            'genre': "Horror"
        },
        {
            'title': "The Creator",
            'description': "From director/co-writer Gareth Edwards (Rogue One, Godzilla) comes an epic sci-fi action thriller set amidst a future war between the human race and the forces of artificial intelligence. Joshua (John David Washington), a hardened ex-special forces agent grieving the disappearance of his wife (Gemma Chan), is recruited to hunt down and kill the Creator, the elusive architect of advanced AI who has developed a mysterious weapon with the power to end the war…and mankind itself. Joshua and his team of elite operatives journey across enemy lines, into the dark heart of AI-occupied territory, only to discover the world-ending weapon he's been instructed to destroy is an AI in the form of a young child (Madeleine Yuma Voyles).",
            'duration_mins': 133,
            'language': "English",
            'release_date': "28/09/2023",
            'country': "United States",
            'genre': "Action"
        }
    ]

    # Add each record to the CSV
    for record in movie_records:
        add_record(movieDbName, record)

def db_initial_insert_movie_meida():
    movie_media_records = [
        {
            'movieid': "1",
            'cardsrcaddress': "../../static/Cards/TheNunII.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/TheNunII.jpg"
        },
        {
            'movieid': "2",
            'cardsrcaddress': "../../static/Cards/FiveNightsatFreddy.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/FiveNightsatFreddy.jpg"
        },
        {
            'movieid': "3",
            'cardsrcaddress': "../../static/Cards/KillersoftheFlowerMoon.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/KillersoftheFlowerMoon.jpg"
        },
        {
            'movieid': "4",
            'cardsrcaddress': "../../static/Cards/Uproar.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/Uproar.jpg"
        },
        {
            'movieid': "5",
            'cardsrcaddress': "../../static/Cards/TaylorSwift.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/TaylorSwift.jpg"
        },
        {
            'movieid': "6",
            'cardsrcaddress': "../../static/Cards/Oppenheimer.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/Oppenheimer.jpg"
        },
        {
            'movieid': "7",
            'cardsrcaddress': "../../static/Cards/SawX.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/SawX.jpg"
        },
        {
            'movieid': "8",
            'cardsrcaddress': "../../static/Cards/TheCreator.jpg",
            'detailbanneraddress': "../static/MovieDetailBanner/TheCreator.jpg"
        }
    ]

    for record in movie_media_records:
        add_record(movieMediaDbName, record)
