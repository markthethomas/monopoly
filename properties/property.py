"""
Property class
"""


class Property(object):
    """
    a monopoly property that items on the
    board can inherit from
    """

    def __init__(self, name, price, baseRent, rentWithHouses, mortgageValue, owner=None, houseCost, hotelCost):
        self.name = name
        self.owner = owner
        self.price = price
        self.baseRent = baseRent
        self.rentWithHouses = rentWithHouses
        self.mortgageValue = mortgageValue

        self.houseCost = houseCost
        self.hotelCost = hotelCost

        self.houses = 0
        self.hotels = 0

    @property
    def rent(self):
        return

    def purchase(self, player, cost):
        player.balance -= cost

    def purchaseProperty(self, player):
        self.owner = player
        purchase(player, self.cost)

    def buyHotel(self, player):
        self.hotels += 1
        player.balance -= self.hotelCost

    def buyHouse(self, player):
        self.houses += 1
        player.balance -= self.houseCost
