candidates: list[str] = []
possiblities = [str(x) for x in range(9, 0, -1)]


def construct_candidates(curr: list[str] = []):
    for p in possiblities:
        if p in curr:
            continue
        curr.append(p)
        if len(curr) == 9:
            candidates.append("".join(curr))
            curr.remove(p)
            return
        construct_candidates(curr)
        curr.remove(p)


def solve_for_number(s: str):
    subset = ""
    for c in s:
        subset += c
        res = []
        num = int(subset)
        length = 0
        for p in set_of_numbers:
            r = str(num * p)
            length += len(r)
            res.append(r)
            if length == 9:
                if s != "".join(res):
                    break
                elif p != 1:
                    return True
            if length > 9:
                break
    return False


construct_candidates()
set_of_numbers = [x for x in range(1, 10)]

for c in candidates:
    if solve_for_number(c):
        print(c)
        exit()
