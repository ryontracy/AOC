with open('input.txt') as f:
    lines = f.readlines()

games = []

class Game:
    def __init__(self, line):
        self.sets = []
        self.number = None
        self.parse()

    def parse(self):
        stripline = line.strip()
        splitstring = stripline.split(': ')
        self.number = int(splitstring[0].split(' ')[1])
        setstrings = splitstring[1].split('; ')
        for s in setstrings:
            set = {}
            ballsets = s.split(', ')
            for bs in ballsets:
                set[bs.split(' ')[1]] = int(bs.split(' ')[0])
            self.sets.append(set)
                    
        # print(self.number, ': ', self.sets)
    
    def _colors(self, color):
        colors = []
        for set in self.sets:
            try:
                colors.append(set[color])
            except KeyError:
                colors.append(0)
        return colors

    @property
    def reds(self):
        return self._colors('red')
    
    @property
    def blues(self):
        return self._colors('blue')
    
    @property
    def greens(self):
        return self._colors('green')

    def is_possible(self, red, blue, green):
        if max(self.reds) > red:
            return False
        elif max(self.blues) > blue:
            return False
        elif max(self.greens) > green:
            return False
        else:
            return True
        

for line in lines:
    game = Game(line)
    games.append(game)

possible_games = [game.number for game in games if game.is_possible(red=12, green=13, blue=14)]
print(possible_games)
print(sum(possible_games))

