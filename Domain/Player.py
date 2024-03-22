from Domain.Enums import Pillar


class Player:
    def __init__(self, name):
        self.name: str = name

        self.stone: int = 0
        self.food: int = 0
        self.ideas: int = 0
        self.money: int = 0
        self.population: int = 5
        self.stone_production: int = 0
        self.food_production: int = 0
        self.idea_production: int = 0
        self.tax_production: int = 0
        self.tariff_production: int = 0
        self.unrest: int = 0

        self.technology_cards: [TechnologyCard] = []
        self.build_cards: [BuildCard] = []
        self.wonders: [WonderTile] = []
        self.golden_ages: [GoldenAgeTile] = []
        self.civ_achievements: [CivAchievementTile] = []
        self.trade_goods: [TradeGood] = []
        self.leader: Leader


class Board:
    pass


class Game:
    def __init__(self, players: [Player]):
        self.players: [Player] = players
        self.starting_player: Player
        self.board: Board = Board()


class TechnologyCard:
    def __init__(self, name: str, starting: bool):
        self.name: str = name
        self.starting: bool = starting
        self.pillars: [Pillar] = []
        self.requirements: [Pillar] = []
        self.effect = None
        self.face_up: bool = False
        self.player: Player
        self.game: Game
        

    def flip(self):
        if self.face_up:
            raise AttributeError('Card is already face up.')
        self.face_up = True
        self.effect()


class TradeGood:
    pass


class Leader:
    pass


class BuildCard:
    pass


class WonderTile:
    pass


class GoldenAgeTile:
    def __init__(self, name: str, pillar: Pillar):
        self.name: str = name
        self.pillar: Pillar = pillar


class CivAchievementTile:
    pass

