# part 1

def process_report(report):
    return all([(pair2>pair1 and pair2-pair1<4) for pair1,pair2 in zip(report, report[1:])]) or all((pair2<pair1 and pair1-pair2<4) for pair1,pair2 in zip(report, report[1:]))

unsafe_reports = []
with open('d2/input.txt', 'r') as file:
    safe = 0
    for line in file:
        report = [int(elem) for elem in line.split()]
        increasing = all([(pair2>pair1 and pair2-pair1<4) for pair1,pair2 in zip(report, report[1:])])
        decreasing = all((pair2<pair1 and pair1-pair2<4) for pair1,pair2 in zip(report, report[1:]))
        if increasing or decreasing:
            safe += 1
        else:
            unsafe_reports.append(report)
print(safe)

new_safe = 0
for report in unsafe_reports:
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if process_report(new_report):
            new_safe += 1
            break
print(new_safe)
print(new_safe+safe)




