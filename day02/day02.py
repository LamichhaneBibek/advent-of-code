class cubeSet:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return str((self.r,self.g,self.b))
    def __repr__(self):
        return str((self.r,self.g,self.b))
    
    def max(self, other):
        self.r = max(self.r, other.r)
        self.g = max(self.g, other.g)
        self.b = max(self.b, other.b)
    
    def isSubset(self,other):
        return (self.r <= other.r and self.g <= other.g and self.b <= other.b)
    
    def power(self):
        return self.r * self.g * self.b
    
    def parse(reveal):
        colors = ["red","green","blue"]
        values = [0]*3
        for token in reveal.split(","):
            for i,color in enumerate(colors):
                if color in token:
                    values[i] = int(token.split()[0])
        return cubeSet(*values)
    

def day02(input):
    total = cubeSet(12,13,14)
    p1 = p2 = 0
    for game_num, line in enumerate(input.splitlines()):
        game_num += 1
        _, rhs = line.split(":")
        sets = []
        for reveal in rhs.split(";"):
            sets.append(cubeSet.parse(reveal))
        if all(s.isSubset(total) for s in sets):
            p1 += game_num

        maxCubes = cubeSet(0,0,0)
        for s in sets:
            maxCubes.max(s)
        p2 += maxCubes.power()
    return p1, p2

def main():
    input = open("input.txt").read()
    p1,p2 = day02(input)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")

if __name__ == "__main__":
    main()