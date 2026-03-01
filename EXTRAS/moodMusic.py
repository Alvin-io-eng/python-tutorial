playlist = [
    "we dont talk about bruno",
    "last heartbreak song",
    "can't stop the feeling",
    "starlight",
    "shut up & dance with me",
    "dusk till dawn",
    "beautiful people",
    "begging you",
    "miles on it",
    "line by line",
    "thank god",
    "romantic call",
    "insecure",
    "say you won't let go",
    "fire on fire"
        ]

categories = ["SAD","LOVE","HAPPY","NEUTRAL"]

print("""
Below is your playlist and categories available
assign each song into a category
""")
print("------------PLAYLIST-----------")
for _ in playlist:
    print(_)

print("-----------CATEGORIES-----------")
for _ in categories:
    print(_)

songlist = []

for eachSong in playlist:
    assignedCategory = input(f"Assign Category for this song \"{eachSong}\" ")
    if assignedCategory.upper() not in categories:
            print("Category not found")
            # repeat()
    else:
        category = assignedCategory.upper()
        song = {category:eachSong}
        songlist.append(song)

print(songlist)
selectCategory = input("Select Category youl'd like to listen to today: ").upper()

    

    




