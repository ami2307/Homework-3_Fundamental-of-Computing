def triangle(n, total=None):
    if total is None:
        total = n
    if n <= 0:
        return []
    rows = triangle(n - 1, total)
    stars = ' '.join(['*'] * n)
    spaces = ' ' * (total - n)
    row_str = spaces + stars
    return rows + [row_str]

def show_triangle(n):
    lines = triangle(n)
    if lines:
        for line in lines:
            print(line)
    else:
        print()  

