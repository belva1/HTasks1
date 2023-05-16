# example principe of work h = 4
# print(" " * 3 + "# "*1 + " " * 2)
# print(" " * 2 + "# "*2 + " " *1)
# print(" " * 1 + "# "*3 + " " *0)
# print(" " * 0 + "# "*4 + " " *(-1))

def draw_triangle(h):
    s = input("Please enter a symbol: ")
    if h < 0:
        print("The number must be positive.")
    elif not h % 2:
        print("The number must be even.")
    else:
        for i in range(h - 1):
            print(" " * (h - 1 - i) + f"{s} " * (i + 1) + " " * (h - 2 - i))
        for i in list(range(h))[::-1]:
            print(" " * (h - 1 - i) + f"{s} " * (i + 1) + " " * (h - 2 - i))

draw_triangle(5)