def draw_pyramid_for(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))


def draw_pyramid_while(size):
    i = 1
    while i <= size:
        print(" " * (size - i) + "*" * (2 * i - 1))
        i += 1

def draw_cross(n):
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Exemples d'utilisation
draw_pyramid_for(5)
draw_pyramid_while(5)
draw_cross(7)