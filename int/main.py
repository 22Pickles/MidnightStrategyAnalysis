from strategies import Strategies
import random
from typing import List


class Main:
    def score(self, pocket: List[int]) -> int:
        if (1 in pocket) and (4 in pocket):
            r: List[int] = [1, 4]
            o: List[int] = []
            for i in range(len(pocket)):
                if pocket[i] in r:
                    r.remove(pocket[i])
                else:
                    o.append(pocket[i])
            return sum(o)
        else:
            return 0

    def gameloop(self) -> int:
        game_running: bool = True
        dice: int = 6
        b: List[int] = []

        while game_running:
            a: List[int] = [random.randint(1,6) for _ in range(dice)]
            print(f"Roll: {a}\nPocket: {b}\nScore: {self.score(b)}")
            for i in [int(x) for x in [int(i) for i in input("Which do you want to take?\n>>>").split()]]:
                a.remove(i)
                b.append(i)
            dice = len(a)
            print("--------")
            if dice == 0:
                print(f"Game Over\nPocket: {b}\nScore: {self.score(b)}")
                game_running = False
                return self.score(b)
        return 1

    def main(self) -> None:
        self.gameloop()


if __name__ == "__main__":
    o = Main()
    o.main()


    