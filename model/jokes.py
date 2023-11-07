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
    "Kylian Mbappe": {
        "position" : ST,
        "stats": [91, 97, 90, 80, 92, 36, 78]
    },

    "Sergi Roberto": {
        "position" : RB,
        "stats": [80, 74, 63, 79, 77, 75, 73]
    },

    "Ryota Morioka": {
        "Position" : CM,
        "stats": [72, 42, 69, 74, 69, 71, 68]
    },
    "Erling Haaland": {
        "position" : ST,
        "stats" : [91, 89, 93, 66, 80, 24, 88]
    },
    "Kevin DeBruyne": {
        "position": CM,
        "stats" : [91, 72, 88, 94, 87, 65, 78]
    },
    "Sandro Tonali": {
        "position": CM,
        "stats": [86, 84, 74, 81, 81, 82, 84]
    },
    "Qiu Zhongyi": {
        "position": CB,
        "stats": [48, 56, 25, 27, 34, 51, 52]
    },
    "Marcus Rashford": {
        "position": LW,
        "stats": [85, 90, 86, 78, 84, 42, 74]
    },
    "Vinicius Jr": {
        "position": LW,
        "stats": [89, 95, 82, 78, 90, 29, 68]
    },
    "Bruno Fernandes": {
        "position": CAM,
        "stats": [88, 71, 86, 90, 83, 69, 77]
    },
    "Kaoru Mitoma": {
        "position": LM,
        "stats": [80, 84, 73, 74, 85, 57, 65]
    },
    "Eberechi Eze": {
        "position": CAM,
        "stats": [79, 77, 76, 77, 82, 49, 68]
    },
    "Chris Donell": {
        "position": CM,
        "stats": [55, 63, 47, 52, 56, 48, 65]
    },
    "Son Seung Woo": {
        "position": RWB,
        "stats": [48, 62, 26, 34, 44, 47, 51]
    },
    "Jayden Harris": {
        "position": CDM,
        "stats": [58, 66, 48, 53, 54, 54, 69]    
    },
    "James Madisson": {
        "position": CAM,
        "stats": [84, 71, 81, 86, 86, 54, 63]
    },
    "Paulo Dybala": {
        "position": CF,
        "stats": [86, 80, 85, 85, 90, 40, 60]
    },
    "Hakan Calhanoglu": {
        "position": CM,
        "stats": [85, 67, 80, 86, 85, 70, 66]
    },
    "Iago Aspas": {
        "position": ST,
        "stats": [85, 81, 85, 79, 86, 35, 64]
    },
    "Antony": {
        "position": RM,
        "stats": [70, 83, 58, 63, 73, 38, 51]
    },
    "Noah Katterbach": {
        "position": LB,
        "stats": [69, 71, 40, 57, 72, 66, 58]
    }

}

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    #position = joke_list["Lionel Messi"]["position"]
    #position = joke_list[playerName]["position"]
    item_id = 0
    for player_name, player_info in joke_list.items():
        jokes_data.append({"name": player_name, "position": player_info["position"], "stats": player_info["stats"]})
        item_id += 1
    # prime some haha responses
    # for i in range(10):
       #  id = getRandomJoke()['id']
       #  addJokeHaHa(id)
    # prime some haha responses
    # for i in range(5):
       #  id = getRandomJoke()['id']
       #  addJokeBooHoo(id)
        
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
# def favoriteJoke():
    # best = 0
    # bestID = -1
    # for joke in getJokes():
       #  if joke['haha'] > best:
           #  best = joke['haha']
            # bestID = joke['id']
    # return jokes_data[bestID]
    
# Jeered joke
# def jeeredJoke():
  #   worst = 0
  #   worstID = -1
  #   for joke in getJokes():
  #       if joke['boohoo'] > worst:
  #           worst = joke['boohoo']
  #           worstID = joke['id']
   #  return jokes_data[worstID]

# Add to haha for requested id
# def addJokeHaHa(id):
   #  jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
   #  return jokes_data[id]['haha']

# Add to boohoo for requested id
# def addJokeBooHoo(id):
  #   jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
  #   return jokes_data[id]['boohoo']

# Pretty Print joke
# def printJoke(joke):
  #   print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
# def countJokes():
   #  return len(jokes_data)

# Test Joke Model
# if __name__ == "__main__": 
   #  initJokes()  # initialize jokes
    
    # Most likes and most jeered
# best = favoriteJoke()
   #  print("Most liked", best['haha'])
   #  printJoke(best)
   #  worst = jeeredJoke()
   #  print("Most jeered", worst['boohoo'])
  #   printJoke(worst)
    
    # Random joke
 #    print("Random joke")
  #   printJoke(getRandomJoke())
    
    # Count of Jokes
  #   print("Jokes Count: " + str(countJokes()))