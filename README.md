# SW_RPG_Diceroller

Dice roller for FFG Star Wars RPG game
Tested on linux Debian 9 with Python 3.5.3.

## How to run

```commandline
cd src
export PYTHONPATH=$PYTHONPATH:`pwd`
python3 ./src/Game.py
```

## TODO list

+ [ ] UDP client/server
+ [ ] users logic
+ [ ] Unit test
+ [ ] GUI

## Coding rules

[PEP-8](https://www.python.org/dev/peps/pep-0008/) compliant

## Code quality check

The code quality can be checked by using `pylint3` with a [script](./run_code_analysis.sh) to run.
The script generate a [report](code_analysis_report.txt) to monitor quality code through development.
The script should be run before pushing to Github, new warning or code flaws should'nt be add.
