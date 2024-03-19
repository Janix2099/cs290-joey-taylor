# type python -m uvicorn server:app --reload to host!

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Card Data, will do one of each series, plus the entirety of Series 1 to show that the filters work!
Card_Data = [
    
    {
        "name": "Abomination",
        "effects": ["no-ability"],
        "power": 9,
        "energy": 5,
        "img": "./assets/abomination.webp",
        "series": 1,
        "desc": '"Foolish rabble! You are beneath me!"',
        "id": 1,
        
    },

    {
        "name": "America Chavez",
        "effects": ["on-reveal"],
        "power": 2,
        "energy": 1,
        "img": "./assets/america-chavez.webp",
        "series": 1,
        "desc": "On Reveal: Give the top card of your deck +2 Power.",
        "id": 2,
        
    },

    {
        "name": "Angel",
        "effects": ["destroy"],
        "power": 2,
        "energy": 1,
        "img": "./assets/angel.webp",
        "series": 1,
        "desc": "When one of your cards is destroyed, this flies out of your hand or deck to replace it.",
        "id": 3,
        
    },

    {
        "name": "Angela",
        "effects": [],
        "power": 2,
        "energy": 2,
        "img": "./assets/angela.webp",
        "series": 1,
        "desc": "After you play a card here, +1 Power.",
        "id": 4,
        
    },

    {
        "name": "Ant-Man",
        "effects": ["on-going"],
        "power": 1,
        "energy": 1,
        "img": "./assets/ant-man.webp",
        "series": 1,
        "desc": "Ongoing: If your side of this location is full, +4 Power.",
        "id": 5,
        
    },

    {
        "name": "Apocalypse",
        "effects": ["discard"],
        "power": 6,
        "energy": 8,
        "img": "./assets/apocalypse.webp",
        "series": 1,
        "desc": "When you discard this, put it back with +4 Power.",
        "id": 6,
        
    },

    {
        "name": "Armor",
        "effects": ["on-going", "destroy"],
        "power": 3,
        "energy": 2,
        "img": "./assets/armor.webp",
        "series": 1,
        "desc": "Ongoing: Cards here can’t be destroyed.",
        "id": 7,
        
    },
    {
        "name": "Bishop",
        "effects": [],
        "power": 1,
        "energy": 3,
        "img": "./assets/bishop.webp",
        "series": 1,
        "desc": "After you play a card, this gains +1 Power.",
        "id": 8,
        
    },
    {
        "name": "Blade",
        "effects": ["on-reveal", "discard"],
        "power": 3,
        "energy": 1,
        "img": "./assets/blade.webp",
        "series": 1,
        "desc": "On Reveal: Discard the rightmost card from your hand.",
        "id": 9,
        
    },
    {
        "name": "Blue Marvel",
        "effects": ["on-going"],
        "power": 3,
        "energy": 5,
        "img": "./assets/blue-marvel.webp",
        "series": 1,
        "desc": "Ongoing: Your other cards have +1 Power.",
        "id": 10,
        
    },
    {
        "name": "Cable",
        "effects": ["on-reveal"],
        "power": 3,
        "energy": 2,
        "img": "./assets/cable.webp",
        "series": 1,
        "desc": "On Reveal: Draw a card from your opponent’s deck.",
        "id": 11,
        
    },
    {
        "name": "Captain America",
        "effects": ["on-going"],
        "power": 3,
        "energy": 3,
        "img": "./assets/captain-america.webp",
        "series": 1,
        "desc": "Ongoing: Your other cards here have +1 Power.",
        "id": 12,
        
    },
    {
        "name": "Carnage",
        "effects": ["on-reveal", "destroy"],
        "power": 2,
        "energy": 2,
        "img": "./assets/carnage.webp",
        "series": 1,
        "desc": "On Reveal: Destroy your other cards here. +2 Power for each destroyed.",
        "id": 13,
        
    },
    {
        "name": "Colossus",
        "effects": ["on-going", "destroy"],
        "power": 3,
        "energy": 2,
        "img": "./assets/colossus.webp",
        "series": 1,
        "desc": "Ongoing: Can’t be destroyed, moved, or have its Power reduced.",
        "id": 14,
        
    },
    {
        "name": "Cosmo",
        "effects": ["on-reveal", "on-going"],
        "power": 3,
        "energy": 3,
        "img": "./assets/cosmo.webp",
        "series": 1,
        "desc": "Ongoing: On Reveal abilities won’t happen here.",
        "id": 15,
        
    },
    {
        "name": "Cyclop",
        "effects": ["no-ability"],
        "power": 4,
        "energy": 3,
        "img": "./assets/cyclops.webp",
        "series": 1,
        "desc": '"Let’s move, X-Men."',
        "id": 16,
        
    },
    {
        "name": "Deathlok",
        "effects": ["on-reveal", "destroy"],
        "power": 5,
        "energy": 3,
        "img": "./assets/deathlok.webp",
        "series": 1,
        "desc": "On Reveal: Destroy your other cards here.",
        "id": 17,
        
    },
    {
        "name": "Devil Dinosaur",
        "effects": ["on-going"],
        "power": 5,
        "energy": 5,
        "img": "./assets/devil-dinosaur.webp",
        "series": 1,
        "desc": "Ongoing: +2 Power for each card in your hand.",
        "id": 18,
        
    },
    {
        "name": "Doctor Strange",
        "effects": ["on-reveal", "move"],
        "power": 3,
        "energy": 3,
        "img": "./assets/doctor-strange.webp",
        "series": 1,
        "desc": "On Reveal: Move your highest-Power card(s) to this location.",
        "id": 19,
        
    },
    {
        "name": "Domino",
        "effects": [],
        "power": 3,
        "energy": 2,
        "img": "./assets/domino.webp",
        "series": 1,
        "desc": "You always draw this card on turn 2, and not before.",
        "id": 20,
        
    },
    {
        "name": "Elektra",
        "effects": ["on-reveal", "destroy"],
        "power": 2,
        "energy": 1,
        "img": "./assets/elektra.webp",
        "series": 1,
        "desc": "On Reveal: Destroy an enemy 1-Cost card here.",
        "id": 21,
        
    },
    {
        "name": "Enchantress",
        "effects": ["on-reveal", "on-going"],
        "power": 5,
        "energy": 4,
        "img": "./assets/enchantress.webp",
        "series": 1,
        "desc": "On Reveal: Remove the abilities from all Ongoing cards here.",
        "id": 22,
        
    },
    {
        "name": "Forge",
        "effects": ["on-reveal"],
        "power": 2,
        "energy": 2,
        "img": "./assets/forge.webp",
        "series": 1,
        "desc": "On Reveal: Give the next card you play +2 Power.",
        "id": 23,
        
    },
    {
        "name": "Gamora",
        "effects": ["on-reveal"],
        "power": 7,
        "energy": 5,
        "img": "./assets/gamora.webp",
        "series": 1,
        "desc": "On Reveal: If your opponent played a card here this turn, +5 Power.",
        "id": 24,
        
    },
    {
        "name": "Groot",
        "effects": ["on-reveal"],
        "power": 4,
        "energy": 3,
        "img": "./assets/groot.webp",
        "series": 1,
        "desc": "On Reveal: If your opponent played a card here this turn, +2 Power.",
        "id": 25,
        
    },
    {
        "name": "Morbius",
        "effects": ["on-going", "discard"],
        "power": 0,
        "energy": 2,
        "img": "./assets/morbius.webp",
        "series": 4,
        "desc": "Ongoing: +2 Power for each time you discarded a card this game.",
        "id": 26,
        
    },
    {
        "name": "Spider-Man",
        "effects": ["on-reveal", "move"],
        "power": 5,
        "energy": 3,
        "img": "./assets/spider-man.webp",
        "series": 3,
        "desc": "On Reveal: Move to another location and pull an enemy card from here to there.",
        "id": 27,
    },

    {
        "name": "The Phoenix Force",
        "effects": ["on-reveal", "destroy", "move"],
        "power": 5,
        "energy": 4,
        "img": "./assets/the-phoenix-force.webp",
        "series": 4,
        "desc": "On Reveal: Revive one of your destroyed cards and merge with it. That card can move each turn.",
        "id": 28,
        
    },
    {
        "name": "Werewolf by Wolf",
        "effects": ["on-reveal"],
        "power": 4,
        "energy": 4,
        "img": "./assets/werewolf-by-night.webp",
        "series": 5,
        "desc": "After you play a card, move there to gain +2 Power if it has an On Reveal.",
        "id": 29,
        
    },
        {
        "name": "X-23",
        "effects": ["destroy", "discard"],
        "power": 2,
        "energy": 1,
        "img": "./assets/x-23.webp",
        "series": 5,
        "desc": "When this is discarded or destroyed, regenerate it at a random location and you get +1 Energy next turn.",
        "id": 30,
        
    },
]

# no security, boo-womp, couldn't get CORS to work
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=JSONResponse)
async def read_cards():
    return Card_Data

@app.get("/collection", )
async def custom_collect(collection: str):
    string_collection_list = collection.split(',')
    int_collection_list = []
    for string in string_collection_list:
        num = int(string)
        int_collection_list.append(num)
    retval = []
    for card in Card_Data:
        if card["id"] in int_collection_list:
            retval.append(card)
    return retval



