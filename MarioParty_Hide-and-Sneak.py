import random as rand

def choose_hiding_spot(list):
    return rand.choice(list)

if __name__ == "__main__":

# the game runs for three rounds
    game_count = 10000
    seeker_wins = 0
    round_1_wins = 0
    round_2_wins = 0
    round_3_wins = 0
    for count in range(0, game_count):
        list_rock = []
        list_stump = []
        list_bush = []
        list_house = []

        list_hiding_spots = [
            list_rock,
            list_stump,
            list_bush,
            list_house
        ]

        list_hiders = [
            "Mario",
            "Luigi",
            "Peach"
        ]
        
        for round in range(0,3):
            
            # the 3 hiders pick a spot
            for hider in list_hiders:
                choose_hiding_spot(list_hiding_spots).append(hider)
            
            # the seeker picks a spot
            spot = choose_hiding_spot(list_hiding_spots)
            if spot != []:
                for hider in spot:
                    list_hiders.remove(hider)
            list_hiding_spots.remove(spot)
            
            for spot in list_hiding_spots:
                spot.clear()
            if list_hiders == []:
                seeker_wins += 1
                if round == 0:
                    round_1_wins += 1
                if round == 1:
                    round_2_wins += 1
                if round == 2:
                    round_3_wins += 1

    print(f"Win Chance: {seeker_wins/game_count}, Lose Chance: {(game_count - seeker_wins)/game_count}")

    print(f"Round 1 wins per game: {round_1_wins/game_count}")

    print(f"Round 2 wins per game: {round_2_wins/game_count}")

    print(f"Round 3 wins per game: {round_3_wins/game_count}")
