import random


CF = "Center Forward"
ST = "Striker"
RB = "Right Back"
LB = "Left Back"
CM = "Central Midfield"
LW = "Left Wing"
CDM = "Central Defensive Midfield"
CB = "Center Back"
RM = "Right Midfield"
LM = "Left Midfield"
LD = "Left Back"
CAM = "Central Attacking Midfield"
RW = "Right Wing"
LWB = "Left Wing Back"
RWB = "Right Wing Back"
jokes_data = []
joke_list = {

    "Lionel Messi": {
        "position" : CF,
        "stats": [90, 80, 87, 90, 94, 33, 64]
    },
    "Cristiano Ronaldo" : {
        "position" : ST,
        "stats": [86, 85, 90, 75, 92, 45, 78]
    },
    "Erling Haaland": {
        "position" : ST,
        "stats" : [91, 89, 93, 66, 80, 24, 88],
    },
    "Kevin DeBruyne": {
        "position": CM,
        "stats" : [91, 72, 88, 94, 87, 65, 78],
    },
    ""

}

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    #position = joke_list["Lionel Messi"]["position"]
    #position = joke_list[playerName]["position"]
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
    return jokes_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
    return jokes_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))