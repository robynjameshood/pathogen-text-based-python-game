#Pathogen
import random, pickle, time, story, storyEnd #Imports random, pickle, time and the story module for the responses.
totalKills = 0
pathogen = {1 : {'E. Coli ' : 45}, #Selectable virus catalogue.
            2 : {'Sepsis ' :  70},
            3 : {'Influenza ' : 140},
            4 : {'Pneumonia' : 125},
            5 : {'Tuberculosis' : 150}}
mutations = {1: {'Small Pox' : 320}, #Possible permutations of mutations.
             2 : {'Bubonic Plague' : 335},
             3 : {'Ebola ' : 375},
             4 : {'SARS' : 210},
             5 : {'Mono-virus' : 30},
             6 : {'Rabis' : 10},
             7 : {'Polio' : 15},
             8 : {'Hepatitis C' : 25},
             9 : {'Lassa Fever' : 20},
             10 : {'Malaria' : 20}}
countryPopulous = {1 : {'Germany' : 8500}, #Country selection catalogue.
                   2 : {'Australia' : 7500},
                   3 : {'United States of America' : 9500},
                   4 : {'North Korea' : 8700},
                   5 : {'Russia' : 15000}}
countryChoice = {} #Empty dictionary which will be populated by the player's choice of country.
playerVirus = {} #Empty dictionary to store the player's virus.
player = {} #Empty dictionary to be utilized later (name, score of each session).
points = 0 #Assigns points to zero.
choice = "" #Assigns empty string.


def welcomeScreen():
    name = str(input("\nEnter your initials: "))
    for i in range(0, 100):
        print("")
    print("\nWelcome", name,", you're about to embark on a mission to devour your selected populus. "
          "\nYou'll have the ability to select from a given catalogue of bacterium, viruses and plagues to select. "
          "\nYou'll be provided with the ability to mutate your chosen virus at the end of each weeks for three weeks, be warned, this can be for the better, or the worse.")
    return name
def saveGame(name, points):
    player[name] = points #Assigns the dictionary of name with the value of points.
    data_out = open("highscores", 'wb') #Variable to load the information into.
    pickle.dump(player, data_out) #Dumps the contents of player into data_out and saves to "savegame" file.
    data_out.close()
def highscores():
    data_in = open("highscores", 'rb') #Variable to open the file.
    player = pickle.load(data_in) #Variable to store the file.
    for i in range(0, 100):
                print("")
    print("\nHIGHSCORES: ")
    print("\nHighest score: ", max(player)) #Prints the highest score in the dictionary/dat file.
    for key, value in player.items(): #Cycles through the keys and values of the dictionary and prints the name and score of each successful play through.
        print("\nName: ", key, "\nScore : ", value)
def loadingBar():
    print("\nLOADING VIRUS...")
    print("\nPlease wait...")
    time.sleep(3)
    for i in range(0, 100): #reference - https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        print("")
def pointsCalculator(number):
    points = number * 5
    return points
def loadingEnvironment():
    print("\nLOADING ENVIRONMENT...")
    print("\nPlease wait...")
    time.sleep(3)
    for i in range(0, 100):
        print("")

def virusOptions():
    while True:
        try:
            choice = int(input("\nPlease select a virus from our pathogen catalogue: "
                       "\n1). E. Coli."
                       "\n2). Sepsis."
                       "\n3). Influenza."
                       "\n4). Pneumonia."
                       "\n5). Tuberculosis."
                       "\nYour choice: "))
            while choice == 0 or choice > 5:
                choice = int(input("\nPlease select a virus from our pathogen catalogue: "
                       "\n1). E. Coli."
                       "\n2). Sepsis."
                       "\n3). Influenza."
                       "\n4). Pneumonia."
                       "\n5). Tuberculosis."
                       "\nYour choice: "))
            break
        except ValueError:
            print("\nOption doesn't exit, try again.")
    for i in range(0, 100):
        print("")
    return playerVirus.update(pathogen[choice]) #Updates the player's virus dictionary with the pathogen of their choice.

def countries(countryChoice):
    for virus in playerVirus:
        print("\nYour virus strand: ", virus, "\t\t Daily mortality rate: ", playerVirus[virus])
        while True:
            try:
                country = int(input("\nPlease select a point of attack: "
                        "\n1). Germany."
                        "\n2). Australia."
                        "\n3). United States of America."
                        "\n4). North Korea. "
                        "\n5). Russia."
                        "\nYour choice: "))
                while country == 0 or country > 5:
                    country = int(input("\nPlease select a point of attack: "
                        "\n1). Germany."
                        "\n2). Australia."
                        "\n3). United States of America."
                        "\n4). North Korea. "
                        "\n5). Russia."
                        "\nYour choice: "))
                break
            except ValueError:
                print("\nOption doesn't exit, try again.")
    for i in range(0, 100):
        print("")
    return countryChoice.update(countryPopulous[country]) #Updates the users country choice with the name and populous of the user's choice.
def mutate():
    mutation = random.randint(1, len(mutations)) #Selects a random mutation using a random number starting from the beginning key up to the length of the mutation dictionary.
    playerVirus.clear() #Clears the previous player's virus details from the dictionary.
    playerVirus.update(mutations[mutation]) #Updates the players dictionary with the new virus details (strand, mortality rate).
def weekday(points, day):
    global totalKills
    for virus in playerVirus:
        for people in countryChoice:
            countryChoice[people] -= playerVirus[virus] #Reduces the chosen population based on the mortality rate of the user's selected or mutated virus.
    totalKills += playerVirus[virus] #adds to the daily kill count.
    points = pointsCalculator(totalKills) #Calculates points based on the daily kill rate (additive).
    print(day, "\nDeaths: ", totalKills,  "\nCountry: ", people, "\nPopulous: ", round(countryChoice[people]), "\nStrand: ", virus, "\nMortality Rate Per Day: ", playerVirus[virus], "\nAccrued Points: ", round(points))
    if totalKills < 1000:
        message = story.low() #Calls the low function in the story module.
    if totalKills >= 1000 and totalKills < 2000:
        message = story.medium() #Calls the module Story and the function of medium within.
    if totalKills >= 2000 and totalKills < 3500:
        message = story.uppermedium()
    if totalKills >= 3500:
        message = story.high()
    time.sleep(5) #reference - https://www.tutorialspoint.com/python/time_sleep.htm
    return points

def week(dayNumber, points):
    points = weekday(points,"\n\n\nMonday\n---------------------------------------------------------------") #Returns points, cycles through each day, sending the points variable and the day of the week.
    points = weekday(points,"\n\n\nTuesday\n---------------------------------------------------------------")
    points = weekday(points,"\n\n\nWednesday\n---------------------------------------------------------------")
    points = weekday(points,"\n\n\nThursday\n---------------------------------------------------------------")
    points = weekday(points,"\n\n\nFriday\n---------------------------------------------------------------")
    points = weekday(points,"\n\n\nSatuday\n---------------------------------------------------------------")
    points = weekday(points,"\n\n\nSunday\n---------------------------------------------------------------")
    return points
def main(points):
    name = welcomeScreen() #Assigned name with the returning function.
    counter = 0 #Loop counter for the three weeks.
    virusOptions() #Calls the virus catalogue dictionary and presents options to the screen for the user to select.
    loadingBar() #Prints loading text to screen.
    countries(countryChoice) #Calls the countries function and passed the countryChoice dictionary to be populated by the user's selection.
    loadingEnvironment()
    while counter < 3: #Loops up to three, then breaks out of the loop on the third week; this is so it doens't ask the user if they wish to mutate at the end of the fourth week.
        points = week(points, "")
        counter+=1 #adds one to the counter.
        for i in range(0, 100):
                print("")
        choice = str(input("\nI'm now going to offer you the ability to mutate your virus, be warned, the mutation maybe for the better or the worse. "
                           "\nDo you wish to mutate (yes/no): "))
        if choice == "yes":
            mutate()
            print("\nParty time!")
            time.sleep(3)
            for i in range(0, 100):
                print("")
        else:
            for i in range(0, 100): #Prints white space to replicate a clear screen function.
                print("")
            print("\nGood luck...")
            time.sleep(3) #Standard sleep timer.
            for i in range(0, 100):
                print("")
            pass
    #final week
    points = week(points, "")
    storyEnd.finale(name, points) #Calls the story function within the StoryEnd module.
    #Sends name and points to savegame function and assigns the value points to name. Then saving to file.
    saveGame(name, points)
def menu():
    while True: #reference - https://docs.python.org/3/tutorial/errors.html
        try: #This tries the input to ensure that the user enters valid input. It also accommodates for the user leaving it blank and pressing enter.
            selection = int(input("\n1). Play game" #Menu options.
                          "\n2). Highscores"
                          "\nSelect: "))
            break
        except ValueError:
            print("\nDoes that look like a number to you?")
    while selection > 2:
        print("\nOption doesn't exit, try again.")
        menu()
    while selection == 0: #loop to prevent the user from selecting an option outside of the menus instructions.
        print("\nOption doesn't exit, try again.")
        menu()
    if selection == 1:
        main(points)
        menu()
    if selection == 2:
        highscores() #Loads and unpickles file and prints highest scores.
        menu() #Cycles back to the menu.

menu()
