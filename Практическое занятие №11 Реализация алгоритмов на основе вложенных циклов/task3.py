powers = [i**5 for i in range(151)]

find = False

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = powers[a] + powers[b] + powers[c] + powers[d]
                for e in range(d, 151):
                    if powers[e] == sum:
                        print(a, b, c, d, e)
                        print(a + b + c + d + e)
                        find = True
                        break
                    if powers[e] > sum:
                        break
                if find:
                    break
            if find:
                break
        if find:
            break
    if find:
        break