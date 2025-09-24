def triangle(n, total=None):
    if total is None:
        total = n
    if n == 0:
        return [""]
    rows = triangle(n - 1, total)
    stars = ' '.join(['*'] * n)
    spaces = ' ' * (total - n)
    return rows + [spaces + stars]

def show_triangle(n):
    lines = triangle(n)
    if not lines:        
        print("")
    else:
        for line in lines:
            print(line)

