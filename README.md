# SW_RPG_Diceroller
Dice roller for FF Star Wars RPG game

Tested on linux Debian 9 with Python 3.5.3.

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