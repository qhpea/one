import dataclasses
import enum

class TarotSuit(enum.StrEnum):
    MAJOR = "Major"
    WANDS = "Wands"
    CUPS = "Cups"
    SWORDS = "Swords"
    PENTACLES = "Pentacles"

@dataclasses.dataclass
class TarotCard:
    name: str
    number: int
    suit: TarotSuit

CARDS = [
    TarotCard(name='The Fool', number=0, suit=TarotSuit.MAJOR),
    TarotCard(name='The Magician', number=1, suit=TarotSuit.MAJOR),
    TarotCard(name='The High Priestess', number=2, suit=TarotSuit.MAJOR),
    TarotCard(name='The Empress', number=3, suit=TarotSuit.MAJOR),
    TarotCard(name='The Emperor', number=4, suit=TarotSuit.MAJOR),
    TarotCard(name='The Hierophant', number=5, suit=TarotSuit.MAJOR),
    TarotCard(name='The Lovers', number=6, suit=TarotSuit.MAJOR),
    TarotCard(name='The Chariot', number=7, suit=TarotSuit.MAJOR),
    TarotCard(name='Strength', number=8, suit=TarotSuit.MAJOR),
    TarotCard(name='The Hermit', number=9, suit=TarotSuit.MAJOR),
    TarotCard(name='Wheel of Fortune', number=10, suit=TarotSuit.MAJOR),
    TarotCard(name='Justice', number=11, suit=TarotSuit.MAJOR),
    TarotCard(name='The Hanged Man', number=12, suit=TarotSuit.MAJOR),
    TarotCard(name='Death', number=13, suit=TarotSuit.MAJOR),
    TarotCard(name='Temperance', number=14, suit=TarotSuit.MAJOR),
    TarotCard(name='The Devil', number=15, suit=TarotSuit.MAJOR),
    TarotCard(name='The Tower', number=16, suit=TarotSuit.MAJOR),
    TarotCard(name='The Star', number=17, suit=TarotSuit.MAJOR),
    TarotCard(name='The Moon', number=18, suit=TarotSuit.MAJOR),
    TarotCard(name='The Sun', number=19, suit=TarotSuit.MAJOR),
    TarotCard(name='Judgement', number=20, suit=TarotSuit.MAJOR),
    TarotCard(name='The World', number=21, suit=TarotSuit.MAJOR),
    TarotCard(name='Ace of Cups', number=1, suit=TarotSuit.CUPS),
    TarotCard(name='Two of Cups', number=2, suit=TarotSuit.CUPS),
    TarotCard(name='Three of Cups', number=3, suit=TarotSuit.CUPS),
    TarotCard(name='Four of Cups', number=4, suit=TarotSuit.CUPS),
    TarotCard(name='Five of Cups', number=5, suit=TarotSuit.CUPS),
    TarotCard(name='Six of Cups', number=6, suit=TarotSuit.CUPS),
    TarotCard(name='Seven of Cups', number=7, suit=TarotSuit.CUPS),
    TarotCard(name='Eight of Cups', number=8, suit=TarotSuit.CUPS),
    TarotCard(name='Nine of Cups', number=9, suit=TarotSuit.CUPS),
    TarotCard(name='Ten of Cups', number=10, suit=TarotSuit.CUPS),
    TarotCard(name='Page of Cups', number=11, suit=TarotSuit.CUPS),
    TarotCard(name='Knight of Cups', number=12, suit=TarotSuit.CUPS),
    TarotCard(name='Queen of Cups', number=13, suit=TarotSuit.CUPS),
    TarotCard(name='King of Cups', number=14, suit=TarotSuit.CUPS),
    TarotCard(name='Ace of Swords', number=1, suit=TarotSuit.SWORDS),
    TarotCard(name='Two of Swords', number=2, suit=TarotSuit.SWORDS),
    TarotCard(name='Three of Swords', number=3, suit=TarotSuit.SWORDS),
    TarotCard(name='Four of Swords', number=4, suit=TarotSuit.SWORDS),
    TarotCard(name='Five of Swords', number=5, suit=TarotSuit.SWORDS),
    TarotCard(name='Six of Swords', number=6, suit=TarotSuit.SWORDS),
    TarotCard(name='Seven of Swords', number=7, suit=TarotSuit.SWORDS),
    TarotCard(name='Eight of Swords', number=8, suit=TarotSuit.SWORDS),
    TarotCard(name='Nine of Swords', number=9, suit=TarotSuit.SWORDS),
    TarotCard(name='Ten of Swords', number=10, suit=TarotSuit.SWORDS),
    TarotCard(name='Page of Swords', number=11, suit=TarotSuit.SWORDS),
    TarotCard(name='Knight of Swords', number=12, suit=TarotSuit.SWORDS),
    TarotCard(name='Queen of Swords', number=13, suit=TarotSuit.SWORDS),
    TarotCard(name='King of Swords', number=14, suit=TarotSuit.SWORDS),
    TarotCard(name='Ace of Wands', number=1, suit=TarotSuit.WANDS),
    TarotCard(name='Two of Wands', number=2, suit=TarotSuit.WANDS),
    TarotCard(name='Three of Wands', number=3, suit=TarotSuit.WANDS),
    TarotCard(name='Four of Wands', number=4, suit=TarotSuit.WANDS),
    TarotCard(name='Five of Wands', number=5, suit=TarotSuit.WANDS),
    TarotCard(name='Six of Wands', number=6, suit=TarotSuit.WANDS),
    TarotCard(name='Seven of Wands', number=7, suit=TarotSuit.WANDS),
    TarotCard(name='Eight of Wands', number=8, suit=TarotSuit.WANDS),
    TarotCard(name='Nine of Wands', number=9, suit=TarotSuit.WANDS),
    TarotCard(name='Ten of Wands', number=10, suit=TarotSuit.WANDS),
    TarotCard(name='Page of Wands', number=11, suit=TarotSuit.WANDS),
    TarotCard(name='Knight of Wands', number=12, suit=TarotSuit.WANDS),
    TarotCard(name='Queen of Wands', number=13, suit=TarotSuit.WANDS),
    TarotCard(name='King of Wands', number=14, suit=TarotSuit.WANDS),
    TarotCard(name='Ace of Pentacles', number=1, suit=TarotSuit.PENTACLES),
    TarotCard(name='Two of Pentacles', number=2, suit=TarotSuit.PENTACLES),
    TarotCard(name='Three of Pentacles', number=3, suit=TarotSuit.PENTACLES),
    TarotCard(name='Four of Pentacles', number=4, suit=TarotSuit.PENTACLES),
    TarotCard(name='Five of Pentacles', number=5, suit=TarotSuit.PENTACLES),
    TarotCard(name='Six of Pentacles', number=6, suit=TarotSuit.PENTACLES),
    TarotCard(name='Seven of Pentacles', number=7, suit=TarotSuit.PENTACLES),
    TarotCard(name='Eight of Pentacles', number=8, suit=TarotSuit.PENTACLES),
    TarotCard(name='Nine of Pentacles', number=9, suit=TarotSuit.PENTACLES),
    TarotCard(name='Ten of Pentacles', number=10, suit=TarotSuit.PENTACLES),
    TarotCard(name='Page of Pentacles', number=11, suit=TarotSuit.PENTACLES),
    TarotCard(name='Knight of Pentacles', number=12, suit=TarotSuit.PENTACLES),
    TarotCard(name='Queen of Pentacles', number=13, suit=TarotSuit.PENTACLES),
    TarotCard(name='King of Pentacles', number=14, suit=TarotSuit.PENTACLES)
]


class TarotReading:
    "a tarot reading of three cards"
    def __init__(self):
        import random
        self.cards = random.choices(CARDS, k=3)
    
    def __str__(self):
        return ", ".join(f"{card.name}" for card in self.cards)
    
def do_tarot_reading():
    return TarotReading()

