import copy
import random


class Hat:
    def __init__(self, **args):
        self.args = args
        self.contents = []
        self.get_contents()
        print(self.contents)

    def draw(self, number):
        removed_items = []
        
        if number > len(self.contents):
            return self.contents

        while number > 0:
            item = random.randint(0, len(self.contents)-1)
            removed_items.append(self.contents[item])
            self.contents.pop(item)
            number -= 1

        return removed_items

    def get_contents(self):
        for ball in self.args.items():
            val = ball[1]
            while val > 0:
                self.contents.append(ball[0])
                val -= 1


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    balls_returned = 0
    cont_experiments = num_experiments

    while cont_experiments > 0:
        contents = copy.copy(hat.contents)
        draw = num_balls_drawn
        draws = []
        expected = 0
        
        while draw > 0:
            if num_balls_drawn > len(contents):
                draws = copy.copy(contents)
                break
            else:    
                index = random.randint(0, len(contents)-1)
                draws.append(contents[index])
                contents.pop(index)
                draw -= 1

        cont_experiments -= 1
        
        for n in expected_balls.items():
            if draws.count(n[0]) >= n[1]:
                expected += 1

        if expected == len(expected_balls):
            balls_returned += 1

    return balls_returned / num_experiments
