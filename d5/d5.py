from collections import defaultdict


def process_rules(line):
    line = list(map(int, line.strip("\n").split("|")))
    rules[line[1]].append(line[0])
    return rules


def process_updates(line):
    line = list(map(int, line.strip("\n").split(",")))
    updates.append(line)


def reorder(update):
    ordered_update = []
    len_update = len(update)
    for i in range(len_update - 1):
        current_page = update[i]
        for other_page in update[i + 1 :]:
            if other_page in rules[current_page]:
                if other_page not in ordered_update:
                    ordered_update.append(other_page)
        if current_page not in ordered_update:
            ordered_update.append(current_page)
        
    return ordered_update


with open("d5/test.txt") as f:
    rules = defaultdict(list)
    updates = []

    process = process_rules
    for line in f:
        if line == "\n":
            process = process_updates
            continue
        process(line)

# sort each update rule -- faster searching inside each list by using a bisect
for k in rules:
    rules[k].sort()

print(rules)
# print(updates)
# print(len(updates))

mid_val = 0

invalid_updates = []
for update in updates:

    len_update = len(update)
    # print(len_update)

    valid = True

    for i in range(len_update - 1):

        current_page = update[i]

        if rules.get(current_page):
            # I have an entry for the current page

            for other_page in update[i + 1 :]:
                if other_page in rules[current_page]:
                    valid = False
                    print(
                        f"INVALID: {update}.\nBroken rule is {other_page}\nNot in {current_page}={rules[current_page]}\n"
                    )
                    invalid_updates.append(reorder(update))

                    break
        else:
            continue

        if valid is False:
            break

    if valid is False:
        continue

    print(f"VALID: {update}\n")
    mid_val += update[(len_update - 1) // 2]

print("p1: ", mid_val)

mid_val = 0
for update in invalid_updates:

    mid_val += update[(len(update) - 1) // 2]

print(invalid_updates)
print("p2: ", mid_val)
