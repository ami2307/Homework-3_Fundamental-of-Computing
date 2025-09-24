def triangle(n):
    if n <= 0:
        return []
    rows = triangle(n-1)
    row_str = ' ' * (n-1) + '* ' * n
    return rows + [row_str.rstrip()]

def show_triangle(n):
    for line in triangle(n):
        print(line)
