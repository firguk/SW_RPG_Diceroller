from src.Dices.Generic.Numeric import Numeric
from src.DicePool import DicePool
from src.Dices.StarWarsRPG.Ability import Ability
from src.Dices.StarWarsRPG.Boost import Boost
from src.Dices.StarWarsRPG.Difficulty import Difficulty
from src.Dices.StarWarsRPG.Force import Force
from src.Dices.StarWarsRPG.Setback import Setback

if __name__ == "__main__":
    d6 = Numeric(6)
    d20 = Numeric(20)
    ab = Ability()
    th = Difficulty()
    bo = Boost()
    sb = Setback()
    fo = Force()

    pool = DicePool()
    pool.add(d6)
    pool.add(d20)
    pool.add(ab)
    pool.add(th)
    pool.add(bo)
    pool.add(sb)
    pool.add(fo)

    pool.throw()
    print(pool)
