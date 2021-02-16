from random import getrandbits


class Player:
    def __init__(self, name):
        self.name = name
        self.wallet = 300
        self.position = 0

    def receive_money(self, value):
        self.wallet += value

    def pay(self, value):
        self.wallet -= value

    def set_position(self, position):
        self.position = position

    def bankruptcy(self):
        self.wallet = 0

    def reset_player(self):
        self.wallet = 300
        self.position = 0


class ImpulsivePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def will_buy(self, value):
        if value <= self.wallet:
            self.wallet = self.wallet - value
            return True
        return False


class DemandingPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def will_buy(self, value):
        if self.wallet >= value > 50:
            self.wallet = self.wallet - value
            return True
        return False


class CautiousPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def will_buy(self, value):
        is_buying = (self.wallet - value) >= 80
        if is_buying:
            self.wallet = self.wallet - value
            return True
        return False


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def will_buy(self, value):
        is_buying = bool(getrandbits(1))
        if is_buying and value <= self.wallet:
            self.wallet = self.wallet - value
            return True
        return False


class Building:
    def __init__(self, rent):
        self.value = rent * 2
        self.rent = rent
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def remove_owner(self):
        self.owner = None


class GameStatistics:
    def __init__(self, winner, number_of_round):
        self.winner = winner
        self.number_of_round = number_of_round
