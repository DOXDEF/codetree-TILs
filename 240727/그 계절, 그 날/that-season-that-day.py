def seasons(y, m, d):
    if y % 4 == 0 or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0):
        if m == 2:
            if d <= 29:
                return "Winter"
        if m == 1 or m == 12:
            if d <= 31:
                return "Winter"
        if m == 3 or m == 5:
            if d <= 31:
                return "Spring"
        if m == 4:
            if d <= 30:
                return "Spring"
        if m == 7 or m == 8:
            if d <= 31:
                return "Summer"
        if m == 6:
            if d <= 30:
                return "Summer"
        if m == 10:
            if d <= 31:
                return "Fall"
        if m == 9 or m == 11:
            if d <= 30:
                return "Fall"
    else:
        if m == 2:
            if d <= 28:
                return "Winter"
        if m == 1 or m == 12:
            if d <= 31:
                return "Winter"
        if m == 3 or m == 5:
            if d <= 31:
                return "Spring"
        if m == 4:
            if d <= 30:
                return "Spring"
        if m == 7 or m == 8:
            if d <= 31:
                return "Summer"
        if m == 6:
            if d <= 30:
                return "Summer"
        if m == 10:
            if d <= 31:
                return "Fall"
        if m == 9 or m == 11:
            if d <= 30:
                return "Fall"
    return -1

a, b, c = map(int, input().split())
print(seasons(a, b, c))