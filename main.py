import json

# loading the data
tracks = {}
artists = {}
totalSongsPlayed = 0
totalTimePlayed = 0
for file in ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json"]:
    dataSet = json.load(open(file))
    for song in dataSet:
        # checking the date of the song being played
        if song["endTime"][:4] == "2023":
            # updating information based on the song
            totalSongsPlayed += 1
            if song["artistName"] in artists: artists[song["artistName"]] += 1
            else: artists[song["artistName"]] = 1
            if song["trackName"] in tracks: tracks[song["trackName"]] += 1
            else: tracks[song["trackName"]] = 1
            totalTimePlayed += song["msPlayed"]


# converting the seconds
totalTimePlayed /= 1000

# printing the information
print(f"Mins Played: {totalTimePlayed / 60}")
print(f"Number Of Songs Played: {totalSongsPlayed}")
print(f"Artists Listened To: {len([key for key in artists])}")
print(f"Songs Listened To: {len([key for key in tracks])}")
best = sorted([key for key in artists], key=lambda v: artists[v])[-25:][::-1]
print(f"Top 5 Artists: \n    " + "\n    ".join(f"#{i}: {key} - {artists[key]} listens" for i, key in enumerate(best, 1)))
best = sorted([key for key in tracks], key=lambda v: tracks[v])[-25:][::-1]
print(f"Top 5 Songs: \n    " + "\n    ".join(f"#{i}: {key} - {tracks[key]} listens" for i, key in enumerate(best, 1)))

