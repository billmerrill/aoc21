from dataclasses import dataclass, field
import pprint

@dataclass
class CaveNode:
    name: str
    links: list = field(default_factory=list)

    def __hash__(self):
        return self.name

@dataclass
class Caves:
    start: CaveNode
    end: CaveNode
    caves: dict = field(default_factory=dict)
    fname: str = None

    def __post_init__(self):
        self.caves['start'] = self.start
        self.caves['end'] = self.end
    
        if self.fname:
            self.load(self.fname)

    def load(self, fname):
        lines = []
        with open(self.fname, 'r') as fh:
            lines = fh.readlines()
        
        for line in lines:
            hay, bee = line.strip().split('-')
            if hay not in self.caves.keys():
                self.caves[hay] = CaveNode(hay)
            self.caves[hay].links.append(bee)
            if bee not in self.caves.keys():
                self.caves[bee] = CaveNode(bee,)
            self.caves[bee].links.append(hay)

    def pretty(self):
        for c in self.caves.values():
            print(f'{c.name}: {c.links}')

def walk(caves):
    pathes = []

    def step(curr_name, path, double_cave):
        path.append(curr_name)
        for next_cave in caves.caves[curr_name].links:
            if next_cave == 'start':
                continue
            if next_cave == 'end':
                final_path = path.copy()
                final_path.append('end')
                pathes.append(final_path)
                continue
            if next_cave.islower():
                if next_cave == double_cave:
                    if path.count(next_cave) > 1:
                        continue
                elif next_cave in path:
                    continue
            step(next_cave, path.copy(), double_cave)
            

    for small_cave in [c for c in caves.caves.keys() if c.islower() and c not in ['start', 'end']]:
        step('start', [], small_cave)
    str_set = set([','.join(x) for x in pathes])
    print(len(str_set))


fname = '/Users/bill/fun/aoc21/12/ex1.txt'
# fname = '/Users/bill/fun/aoc21/12/ex2.txt'
fname = '/Users/bill/fun/aoc21/12/input.txt'
caves = Caves(start=CaveNode('start'), end=CaveNode('end'), fname=fname)
caves.pretty()
walk(caves)