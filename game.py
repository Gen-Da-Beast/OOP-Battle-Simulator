from goblin import Goblin
from hero import Hero
import random

ARENA_NAME = "genevieves fire ring"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblin2 = Goblin("Henry")
    
    print(f"{goblin2.name} enters the arena with {goblin.health} health.")
    
    print("But no hero has answered the call... yet.")

    hero= Hero("Stephan")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    print(f"{hero.name} attacks {goblin.name}...")
    goblin.take_damage(hero.attack())

    if goblin.is_alive:
        hero.take_damage(goblin.attack())


    



if __name__ == "__main__":
    main()
