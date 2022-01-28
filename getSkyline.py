# y__________
# |         |
# |         |
# |         |---------
# |         |        |
# |         |        |
# _______________________________________________x

class Point:
    def __init__(self, x, y, start_point):
        self.x = x
        self.y = y
        self.s = start_point
    
    def print_point(self):
        print(f"[{self.x}, {self.y}, {self.s}]")


class AnswerPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print_point(self):
        print(f"[{self.x}, {self.y}]")


class Building:
    def __init__(self, xl, xr, h):
        self.xl = xl
        self.xr = xr
        self.h = h

    def print_building(self):
        print(f"[{self.xl}, {self.xr}, {self.h}]")

    def get_points(self):
        points = list()

        started_one = True if self.xl <= self.xr else False
        started_two = False if started_one == True else True

        points.append(Point(self.xl, self.h, started_one))
        points.append(Point(self.xr, self.h, started_two))

        return points


def print_buildings(buildings:list):
    for building in buildings:
        building.print_building()

def print_points(pnts:list):
    for point in pnts:
        point.print_point()


def get_all_points(buildings:list):
    points = list()
    for building in buildings:
        b_points = building.get_points()
        points.append(b_points[0])
        points.append(b_points[1])

    return points

def sort_points(pnts:list):
    for i in range(0, len(pnts)):
        for y in range(i+1, len(pnts)):
            if pnts[i].s == True and pnts[y].s == True:
                if pnts[i].x == pnts[y].x and pnts[i].y < pnts[y].y:
                    pnts[i], pnts[y] = pnts[y], pnts[i]
                    continue

            if pnts[i].s == True and pnts[y].s == False:
                if pnts[i].x == pnts[y].x and pnts[i].y > pnts[y].y:
                    pnts[i], pnts[y] = pnts[y], pnts[i]
                    continue

            if pnts[i].x == pnts[y].x and (pnts[i].s == False and pnts[y].s == True):
                pnts[i], pnts[y] = pnts[y], pnts[i]
                continue

            if pnts[i].x > pnts[y].x:
                pnts[i], pnts[y] = pnts[y], pnts[i]


    return pnts


def getSkyline(buildings:list):
    pnts = get_all_points(buildings)
    pnts = sort_points(pnts)
    
    queue = list()
    queue.append(0)
    old_max = 0

    answer_points = list()

    for point in pnts:
        old_max = max(queue)
        if point.s == True:
            queue.append(point.y)
        elif point.s == False:
            queue.remove(point.y)

        if old_max != max(queue):
            answer_points.append(AnswerPoint(point.x, max(queue)))
    
    return answer_points


def MyMain():
    i = int(input("Enter size: "))
    buildings = list()
    
    for index in range(0, i):
        xl, xr, h = [int(x) for x in input().split()]
        buildings.append(Building(xl, xr, h))

    answer_points = getSkyline(buildings)
    print_points(answer_points)


if __name__ == "__main__":
    MyMain()