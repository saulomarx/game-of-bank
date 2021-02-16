from random import getrandbits


class Player:
    def __init__(self):
        self.wallet = 300
        self.position = 0

    def receive_money(self, value):
        self.wallet += value

    def pay(self, value):
        self.wallet -= value


class ImpulsivePlayer(Player):
    def __init__(self):
        super().__init__()

    def will_buy(self, value):
        if value <= self.wallet:
            self.wallet = self.wallet - value
            return True
        return False


class DemandingPlayer(Player):
    def __init__(self):
        super().__init__()

    def will_buy(self, value):
        if self.wallet >= value > 50:
            self.wallet = self.wallet - value
            return True
        return False


class CautiousPlayer(Player):
    def __init__(self):
        super().__init__()

    def will_buy(self, value):
        is_buying = (self.wallet - value) >= 80
        if is_buying:
            self.wallet = self.wallet - value
            return True
        return False


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def will_buy(self, value):
        is_buying = bool(getrandbits(1))
        if is_buying and value <= self.wallet:
            self.wallet = self.wallet - value
            return True
        return False


class Building:
    def __init__(self, value):
        self.value = value
        self.owner = None
