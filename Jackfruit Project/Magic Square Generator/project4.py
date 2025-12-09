import tkinter as tk
from tkinter import messagebox

# ------------------ MAGIC SQUARE ALGORITHMS ------------------ #

def magic_square_odd(n):
    square = [[0]*n for _ in range(n)]
    i, j = 0, n//2

    for num in range(1, n*n + 1):
        square[i][j] = num
        ni, nj = (i - 1) % n, (j + 1) % n
        if square[ni][nj] != 0:
            i = (i + 1) % n
        else:
            i, j = ni, nj
    return square


def magic_square_doubly_even(n):
    square = [[(i*n) + j + 1 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                square[i][j] = (n*n + 1) - square[i][j]
    return square


def magic_square_singly_even(n):
    half = n // 2
    sub_square = magic_square_odd(half)

    square = [[0]*n for _ in range(n)]
    add = [0, 2*half*half, 3*half*half, half*half]

    # Place the 4 sub-squares
    for r in range(half):
        for c in range(half):
            square[r][c] = sub_square[r][c] + add[0]
            square[r][c + half] = sub_square[r][c] + add[1]
            square[r + half][c] = sub_square[r][c] + add[2]
            square[r + half][c + half] = sub_square[r][c] + add[3]

    # Swap columns
    k = half // 2
    for r in range(half):
        for c in range(k):
            square[r][c], square[r + half][c] = square[r + half][c], square[r][c]

    c = k
    for r in range(half):
        square[r][c], square[r + half][c] = square[r + half][c], square[r][c]

    return square


def generate_magic_square(n):
    if n % 2 == 1:
        return magic_square_odd(n)
    elif n % 4 == 0:
        return magic_square_doubly_even(n)
    else:
        return magic_square_singly_even(n)


# ------------------ GUI ------------------ #

def generate():
    try:
        n = int(entry.get().strip())
        if n < 3:
            messagebox.showerror("Error", "Enter n ≥ 3")
            return
    except:
        messagebox.showerror("Error", "Invalid number!")
        return

    square = generate_magic_square(n)

    # Clear previous grid
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Display new magic square
    for r in range(n):
        for c in range(n):
            tk.Label(
                output_frame, text=str(square[r][c]),
                width=4, height=2, relief="solid",
                borderwidth=1, font=("Arial", 12)
            ).grid(row=r, column=c)


# ------------------ TKINTER WINDOW ------------------ #

root = tk.Tk()
root.title("Magic Square Generator (Any n)")

tk.Label(root, text="Enter n (any integer ≥ 3):", font=("Arial", 12)).pack()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate Magic Square",
          command=generate, font=("Arial", 12)).pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

root.mainloop()


# ------------------ TEST FUNCTION CALLS ------------------ #

print("Odd Magic Square (n = 5):")
sq1 = magic_square_odd(5)
for row in sq1:
    print(row)

print("\nDoubly Even Magic Square (n = 8):")
sq2 = magic_square_doubly_even(8)
for row in sq2:
    print(row)

print("\nSingly Even Magic Square (n = 6):")
sq3 = magic_square_singly_even(6)
for row in sq3:
    print(row)

print("\nAuto Generate (Any n):  n = 15")
sq4 = generate_magic_square(15)
for row in sq4:
    print(row)
