#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adnaan
#
# Created:     15/02/2024
# Copyright:   (c) Adnaan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # Starting position
        self.money = 1500  # Initial money
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.jail_cards = 0
        self.doubles_count = 0
        self.get_out_of_jail_free_cards = 0

    def move(self, board):
        if self.in_jail:
            self.jail_turns += 1
            if self.jail_cards > 0:
                self.use_jail_card()
            else:
                self.pay_bail()
                return
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 == roll2:
            self.doubles_count += 1
            if self.doubles_count == 3:
                print(f"{self.name} rolled doubles 3 times in a row! Go to jail.")
                self.go_to_jail()
                return
        else:
            self.doubles_count = 0
        new_position = (self.position + roll1 + roll2) % len(board)
        print(f"{self.name} rolled {roll1}, {roll2}. Moved to {board[new_position]['name']}")
        self.position = new_position
        self.execute_square_action(board[new_position])

    def execute_square_action(self, square):
        if square['type'] == 'property':
            self.land_on_property(square)
        elif square['type'] == 'chance':
            self.draw_chance_card(square)
        elif square['type'] == 'community_chest':
            self.draw_community_chest_card(square)
        elif square['type'] == 'jail':
            print(f"{self.name} is just visiting jail.")
        elif square['type'] == 'go_to_jail':
            print(f"{self.name} goes to jail.")
            self.go_to_jail()
        elif square['type'] == 'free_parking':
            print(f"{self.name} lands on Free Parking. Nothing happens.")
        elif square['type'] == 'go':
            print(f"{self.name} passes GO and collects $200.")
            self.money += 200

    def land_on_property(self, square):
        if not square.get('owner'):
            self.buy_property(square)
        elif square['owner'] != self:
            self.pay_rent(square)

    def buy_property(self, square):
        if self.money >= square['price']:
            self.money -= square['price']
            self.properties.append(square)
            square['owner'] = self
            print(f"{self.name} bought {square['name']} for ${square['price']}")
        else:
            print(f"{self.name} doesn't have enough money to buy {square['name']}")

    def pay_rent(self, square):
        rent = square['rent']
        self.money -= rent
        square['owner'].money += rent
        print(f"{self.name} paid ${rent} rent to {square['owner'].name}")

    def draw_chance_card(self, square):
        print(f"{self.name} draws a Chance card.")
        # Add Chance card actions

    def draw_community_chest_card(self, square):
        print(f"{self.name} draws a Community Chest card.")
        # Add Community Chest card actions

    def go_to_jail(self):
        self.in_jail = True
        self.position = 10  # Jail position

    def use_jail_card(self):
        self.jail_cards -= 1
        self.in_jail = False

    def pay_bail(self):
        self.money -= 50
        self.in_jail = False
        print(f"{self.name} paid $50 bail to get out of jail")

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

def print_board(board):
    for square in board:
        print(square['name'])

# Create the game board
board = [
    {'name': 'Go', 'type': 'go'},
    {'name': 'Mediterranean Avenue', 'type': 'property', 'price': 60, 'rent': 2, 'owner': None},  # Initialize 'owner' key
    # Add more properties
    {'name': 'Chance', 'type': 'chance'},
    {'name': 'Community Chest', 'type': 'community_chest'},
    {'name': 'Jail', 'type': 'jail'},
    # Add more squares
]

# Initialize players
players = [Player("Player 1"), Player("Player 2")]

# Main game loop
while True:
    for player in players:
        print(f"\n{player.name}'s turn:")
        print_board(board)  # Print board before each player's turn
        input("Press Enter to roll the dice...")
        player.move(board)

        print(f"{player.name}'s balance: ${player.money}")

        # Check for bankrupt players
        bankrupt_players = [p for p in players if p.money <= 0]
        for bankrupt_player in bankrupt_players:
            print(f"{bankrupt_player.name} is bankrupt! Eliminating from the game.")
            players.remove(bankrupt_player)

        # Check for game end



    def draw_community_chest_card(self, square):
        print(f"{self.name} draws a Community Chest card.")
        # Add Community Chest card actions

    def go_to_jail(self):
        self.in_jail = True
        self.position = 10  # Jail position

    def use_jail_card(self):
        self.jail_cards -= 1
        self.in_jail = False

    def pay_bail(self):
        self.money -= 50
        self.in_jail = False
        print(f"{self.name} paid $50 bail to get out of jail")

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def calculate_rent(self):
        # Implement rent calculation with houses and hotels
        pass

# Create the game board
board = [
    {'name': 'Go', 'type': 'go'},
    {'name': 'Mediterranean Avenue', 'type': 'property', 'price': 60, 'rent': 2},
    # Add more properties
    {'name': 'Chance', 'type': 'chance'},
    {'name': 'Community Chest', 'type': 'community_chest'},
    {'name': 'Jail', 'type': 'jail'},
    # Add more squares
]

# Initialize players
players = [Player("Player 1"), Player("Player 2")]

# Main game loop
while True:
    for player in players:
        print(f"\n{player.name}'s turn:")
        input("Press Enter to roll the dice...")
        player.move(board)

        print(f"{player.name}'s balance: ${player.money}")

        # Check for bankrupt players
        bankrupt_players = [p for p in players if p.money <= 0]
        for bankrupt_player in bankrupt_players:
            print(f"{bankrupt_player.name} is bankrupt! Eliminating from the game.")
            players.remove(bankrupt_player)

        # Check for game end
        if len(players) == 1:
            print(f"{players[0].name} wins the game!")
            quit()
