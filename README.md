# SW_RPG_Diceroller

Dice roller for FFG Star Wars RPG game
Tested on linux Debian 9 with Python 3.5.3.

## TODO

### Dices

#### Generic

+ [ ] Numeric (d6, d10, d20...)

#### SW

+ [X] Ability / Difficulty
+ [ ] Challenge / Proficiency
+ [X] Boost / Setback
+ [X] Force
+ [ ] Dices results

### Network

+ [ ] UDP client
+ [ ] UDP server
+ [ ] Lobby

### Misc

+ [ ] Users
+ [ ] Lobby
+ [ ] Unit test (sider ?)
+ [ ] GUI

## Coding rules

[PEP-8](https://www.python.org/dev/peps/pep-0008/) compliant

## Quick specs

```
                                     +------+
                                     | Game +<------+
      +---------------+              +-+-+--+       |
      | Communication |                | ^          |
      +---------------+   +-------+    | |          |
                 +------> | Lobby | <--+ |          |
                          +-------+      |          |
                                         |          |
                                         |          |
                                         |    +-----+----+
          +---------+                    |    | DicePool |
          | Player  |                    |    +----------+
          ++--------+--------------------+         ^---+
           ^    ^----+                                 |
+----------+-+       |                                 +-------+
| GameMaster |       |                                 ++ Dice |
+------------+  +----+-------+                          +------+
                | Adventurer |
                +------------+
```

> Very subject to change
>> Lobby and game might be merged
