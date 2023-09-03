import itertools
import collections


class Dice():
    sides: int
    outcomes: list[int]
        
    def __init__(self, sides: int) -> None:
        self.sides = sides
        self.outcomes = [i for i in range(1, sides+1)]
        return
        
    def __str__(self) -> str:
        return f'd{self.sides}'
    

    
class Roller():
    modifier: int
    number: int
    dice_type: Dice
        
    def __init__(self, number: int, dice_type: Dice, modifier: int) -> None:
        self.number = number
        self.modifier = modifier
        self.dice_type = dice_type
        return
    
    def get_totals(self) -> list[int]:
        print(f'Generating outcomes')
        outcomes = [self.dice_type.outcomes for i in range(0, self.number)]
        print(f'Getting totals')
        totals: list[int] = []
        for rolls in itertools.product(*outcomes):
            total = sum(rolls) + self.modifier
            totals.append(total)
        return totals
    
    def __str__(self) -> str:
        return f'{self.number}{self.dice_type}+{self.modifier}'
    
    
    
def print_probabilities(totals) -> None:
    print('Counting totals')
    count_dict = collections.Counter(totals)
    total_count = len(totals)
    print('Displaying odds')
    print('total', 'count', 'percentage')
    for item in count_dict:
        print(item, count_dict[item], count_dict[item]/total_count*100)

        
def roll(number, dice, modifier):
    roller = Roller(number, Dice(dice), modifier)
    print(f'Rolling {roller}:')
    print_probabilities(roller.get_totals())
    
    
# 3d6 + 4
roll(3,6,4)
