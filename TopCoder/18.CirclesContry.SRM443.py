import mathExt as M

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.inside = set()
        self.outside = set()

    def put_inside(self, circle):
        self.inside.add(circle)

    def put_outside(self, circle):
        self.outside.add(circle)

    def get_point(self):
        return (self.x, self.y)

    def is_inside(self, point):
        dist = M.distance(self.get_point(), point)
        return True if self.r > dist else False

    def __str__(self):
        str = '{},{},{}'.format(self.x, self.y, self.r)

        insides = []
        for c in self.inside:
            insides.append('({},{},{})'.format(c.x, c.y, c.r))

        outsides = []
        for c in self.outside:
            outsides.append('({},{},{})'.format(c.x, c.y, c.r))

        str += '[{}],[{}]'.format(",".join(insides), ",".join(outsides))
        return str

def check_two_circle(C1, C2):
    if C1 is C2:
        return

    dist = M.distance(C1.get_point(), C2.get_point())
    if dist < C1.r:
        if C1.r > C2.r:
            C1.put_inside(C2)
            C2.put_outside(C1)
    elif dist <  C2.r:
        if C2.r > C1.r:
            C2.put_inside(C1)
            C1.put_outside(C2)

def find_point_in(contries, point):
    for c in contries:
        if c.is_inside(point):
            check_insides = find_point_in(c.inside, point) if len(c.inside) > 0 else None
            return check_insides if check_insides is not None else c

    return None

def least_borders(X, Y, R, x1, y1, x2, y2):
    contries = []
    for x, y, r in zip(X, Y, R):
        contries.append(Circle(x, y, r))

    for c1 in contries:
        for c2 in contries:
            check_two_circle(c1, c2)

    start = (x1, y1)
    end = (x2, y2)

    start_country = find_point_in(contries, start)
    end_country = find_point_in(contries, end)

    if start_country is None:
        if end_country is None:
            return 0
        else:
            return len(end_country.outside) + 1

    if end_country is None:
        return len(start_country.outside) + 1

    if end_country in start_country.outside:
        borders = 1
        for c in start_country.outside:
            if end_country in c.outside:
                borders += 1
        return borders

    if start_country in end_country.outside:
        borders = 1
        for c in end_country.outside:
            if start_country in c.outside:
                borders += 1
        return borders

    return len(end_country.outside) + len(start_country.outside) + 2


print(least_borders([0],[0],[2],-5,1,5,1))
print(least_borders([0,-6,6],[0,1,2],[2,2,2],-5,1,5,1))
print(least_borders([1,-3,2,5,-4,12,12],[1,-1,2,5,5,1,1],[8,1,2,1,1,1,2],-5,1,12,1))
print(least_borders([-3,2,2,0,-4,12,12,12],[-1,2,3,1,5,1,1,1],[1,3,1,7,1,1,2,3],2,3,13,2))
print(least_borders([-107,-38,140,148,-198,172,-179,148,176,153,-56,-187],
                    [175,-115,23,-2,-49,-151,-52,42,0,68,109,-174],
                    [135,42,70,39,89,39,43,150,10,120,16,8],
                    102,16,19,-108))

