# part 1

with open('d2/input.txt', 'r') as file:
    safe = 0
    for line in file:
        report = [int(elem) for elem in line.split()]
        increasing = all([(pair2>pair1 and pair2-pair1<4) for pair1,pair2 in zip(report, report[1:])])
        decreasing = all((pair2<pair1 and pair1-pair2<4) for pair1,pair2 in zip(report, report[1:]))
        if increasing or decreasing:
            safe += 1
print(safe)

# part 2
with open('d2/input.txt', 'r') as file:
    safe = 0
    for line in file:
        report = [int(elem) for elem in line.split()]
        lenm1 = len(report)-1
        increasing = sum([(pair2>pair1 and pair2-pair1<4) for pair1,pair2 in zip(report, report[1:])])
        decreasing = sum((pair2<pair1 and pair1-pair2<4) for pair1,pair2 in zip(report, report[1:]))
        if ((lenm1-increasing)<2 and decreasing == 0) or ((lenm1-decreasing)<2 and increasing == 0):
            print(lenm1, increasing, decreasing)
            safe += 1
    
print(safe)


