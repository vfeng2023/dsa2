# read points
from math import sqrt
def computeDist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
def findMinDist(points):
    points.sort(key = lambda a: a[0])

    def combine(left, mid, right, delta):
        stripmall = []
        i = mid
        while i >= left:
            if abs(points[mid][0] - points[i][0]) < delta:
                stripmall.append(points[i])
            i-= 1

        j = mid + 1
        while j <= right:
            if abs(points[mid][0] - points[j][0]) < delta:
                stripmall.append(points[j])
            j += 1
        stripmall.sort(key = lambda a:a[1])
        mindist = float('inf')
        for p in range(len(stripmall)):
            for k in range(p+1,min(p+8, len(stripmall))):
                mindist = min(mindist, computeDist(stripmall[p], stripmall[k]))
        return mindist

    def recur(left, right):
        if right - left + 1 <= 3:
            minDist = float('inf')
            for i in range(left, right+1):
                for j in range(i+1, right+1):
                    minDist = min(minDist, computeDist(points[i], points[j]))
            return minDist
        else:
            mid = (left+right)//2
            leftmin = recur(left, mid)
            rightmin = recur(mid+1, right)
            stripdist = combine(left, mid, right, min(leftmin, rightmin))

            return min(leftmin, rightmin, stripdist)
    return sqrt(recur(0, len(points) - 1))

def main():
    # read points, call compute dist
    testcases = []
    linecount = 0
    filename = "100000.txt"# "input.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        n = int(lines[linecount])
        linecount += 1
        while n!=0:
            pointslist = []
            for i in range(n):
                pointslist.append(list(map(float, lines[linecount].split())))
                linecount += 1
            n = int(lines[linecount])
            linecount += 1
            testcases.append(pointslist)
    # print(pointslist)
    print("read file")
    for p in testcases:
        result = findMinDist(p)
        if result < 10000:
            print(result)
        else:
            print("infinity")


if __name__ == "__main__":
    main()