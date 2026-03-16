from strategies import Strategies
import random
from typing import List


class Main:
    
    def main(self) -> None:
        pass

    def gameloop(self) -> None:
        game_running:bool = True
        dice: int = 6
        b: List[int] = []

        while game_running:
            a: List[int] = [random.randint(1,6) for _ in range(dice)]
            



    