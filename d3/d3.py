from collections import deque

q = deque()
e = deque()


def handle_operation(q):
    digit1 = ""
    digit2 = ""
    encountered_comma = False
    for elem in q:
        if elem.isdigit() and not encountered_comma:
            digit1 += elem
        elif elem.isdigit() and encountered_comma:
            digit2 += elem
        elif elem == ",":
            encountered_comma = True
        else:
            pass
    m_res = int(digit1) * int(digit2)
    print(f"handled op: {digit1} x {digit2} = {m_res}")
    return m_res


def handle_enabled(q):
    enabled = ""
    for elem in q:
        enabled += elem
    if enabled == "do()":
        return True
    elif enabled == "don't()":
        return False
    else:
        raise ValueError("Weird stuff going on...")


with open("d3/input.txt", "r") as file:
    acc = 0
    num_digits = 0
    comma_is_set = False
    num_commas = 0
    enabled = True
    for line in file:
        for char in line:
            print(f"Got {char}")
            if char == "m":
                if len(q) == 0:
                    q.append("m")
                    print("appended m")
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char == "u":
                if len(q) > 0 and q[-1] == "m":
                    q.append(char)
                    print("appended u")
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char == "l":
                if len(q) > 0 and q[-1] == "u":
                    q.append(char)
                    print("appended l")
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char == "(":
                if len(q) > 0 and q[-1] == "l":
                    q.append(char)
                    print("appended (")
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char == ")":
                if len(q) > 0 and q[-1].isdigit() and comma_is_set:
                    q.append(char)
                    print("appended )")
                    if enabled:
                        acc += handle_operation(q)
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char == ",":
                if len(q) > 0 and q[-1].isdigit() and num_commas < 1:
                    q.append(char)
                    print(f"appended {char}")
                    num_digits = 0
                    # handle mul(a) for case ")"
                    comma_is_set = True
                    # handle mul(10,2,4)
                    num_commas += 1
                else:
                    q.clear()
                    num_commas, num_digits, comma_is_set = 0, 0, False
            elif char.isdigit():
                if len(q) > 0 and q[-1] == "(":
                    q.append(char)
                    print(f"appended {char}")
                    num_digits = 1
                elif len(q) > 0 and q[-1] == ",":
                    q.append(char)
                    print(f"appended {char}")
                    num_digits = 1
                elif len(q) > 0 and q[-1].isdigit():
                    if num_digits < 4:
                        q.append(char)
                        print(f"appended {char}")
                        num_digits += 1
                    else:
                        q.clear()
                        num_commas, num_digits, comma_is_set = 0, 0, False
            else:
                q.clear()
                num_commas, num_digits, comma_is_set = 0, 0, False

            if char == "d":
                if len(e) == 0:
                    e.append("d")
                    print("appended d")
                else:
                    e.clear()
            elif char == "o":
                if len(e) > 0 and e[-1] == "d":
                    e.append(char)
                    print("appended o")
                else:
                    e.clear()
            elif char == ")":
                if len(e) > 0 and e[-1] == "(":
                    e.append(char)
                    print("appended )")
                    enabled = handle_enabled(e)
                    e.clear()
                else:
                    e.clear()
            elif char == "(":
                if len(e) > 0 and (e[-1] == "o" or e[-1] == "t"):
                    e.append(char)
                    print("appended (")
                else:
                    e.clear()
            elif char == "n":
                if len(e) > 0 and e[-1] == "o":
                    e.append(char)
                    print("appended n")
                else:
                    e.clear()
            elif char == "'":
                if len(e) > 0 and e[-1] == "n":
                    e.append(char)
                    print("appended '")
                else:
                    e.clear()
            elif char == "t":
                if len(e) > 0 and e[-1] == "'":
                    e.append(char)
                    print("appended t")
                else:
                    e.clear()
            else:
                e.clear()


print(acc)
