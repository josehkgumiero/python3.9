from class_point import Point
from class_line import Line
import copy


def main():
    print(__file__.split("/")[-1].split(".")[0])
    print("""\n""")

if __name__ == '__main__':
    main()

    p1 = Point(0, 0)
    
    p2 = Point(10, 10)

    line1 = Line(p1, p2)

    line2 = copy.deepcopy(line1)

    line3 = copy.copy(line1)

    print('line1', line1, line1.p1, id(line1.p1), line1.p2, id(line1.p2))

    print('line2', line2, line2.p1, id(line2.p1), line2.p2, id(line2.p2))

    print('line3', line3, line3.p1, id(line3.p1), line3.p2, id(line3.p2))
