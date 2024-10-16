import json
import importlib.resources as pkg_resources
import dataclasses
import enum

class TarotSuit(enum.StrEnum):
    MAJOR_ARCANA = "Major"
    WANDS = "Wands"
    CUPS = "Cups"
    SWORDS = "Swords"
    PENTACLES = "Pentacles"

@dataclasses.dataclass
class TarotCard:
    name: str
    number: int
    suit: TarotSuit


CARDS = [TarotCard(**card) for card in  json.loads(pkg_resources.read_text(__name__, "cards.json"))]
import random

class TarotReading:
    "a tarot reading of three cards"
    def __init__(self):
        self.cards = random.choices(CARDS, k=3)
    
    def __str__(self):
        return ", ".join(f"{card.name}" for card in self.cards)
    
def do_tarot_reading():
    return TarotReading()

