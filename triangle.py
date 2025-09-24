def triangle(n):
    if n <= 0:
        return []
    rows = triangle(n - 1)
    stars = ' '.join(['*'] * n)  
    row_str = ' ' * (n - 1) + stars
    return rows + [row_str]

def show_triangle(n):
    for line in triangle(n):
        print(line)
