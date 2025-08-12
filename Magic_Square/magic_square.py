def generate_odd(n):
    mat = [[0] * n for _ in range(n)]
    i = n // 2
    j = n - 1

    for num in range(1, n * n + 1):
        mat[i][j] = num
        if num % n == 0:
            j -= 1
        else:
            i -= 1
            j += 1
        i = (i + n) % n
        j = (j + n) % n

    return mat

def generate_doubly_even(n):
    mat = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            mat[i][j] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4) + (j % 4) == 3):
                mat[i][j] = n * n + 1 - mat[i][j]

    return mat

def generate_singly_even(n):
    halfN = n // 2
    subSquareSize = halfN * halfN
    subSquare = generate_odd(halfN)
    mat = [[0] * n for _ in range(n)]

    for i in range(halfN):
        for j in range(halfN):
            val = subSquare[i][j]
            mat[i][j] = val
            mat[i + halfN][j + halfN] = val + subSquareSize
            mat[i][j + halfN] = val + 2 * subSquareSize
            mat[i + halfN][j] = val + 3 * subSquareSize

    k = (n - 2) // 4
    for i in range(halfN):
        for j in range(k):
            mat[i][j], mat[i + halfN][j] = mat[i + halfN][j], mat[i][j]
        for j in range(n - k + 1, n):
            mat[i][j], mat[i + halfN][j] = mat[i + halfN][j], mat[i][j]

    # Swap specific elements
    mat[k][0], mat[k + halfN][0] = mat[k + halfN][0], mat[k][0]
    mat[k][k], mat[k + halfN][k] = mat[k + halfN][k], mat[k][k]

    return mat

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd(n)
    if n % 4 == 0:
        return generate_doubly_even(n)
    return generate_singly_even(n)

def print_square(mat):
    for row in mat:
        print(" ".join(map(str, row)))

def main():
    # Optional: starting state label (not required for logic)
    state_label = input("Enter starting state (optional): ").strip()

    # Core input: order
    while True:
        try:
            n = int(input("Enter order of magic square: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the order.")

    if n < 3:
        print("Magic square not possible for n < 3")
        return

    magic_square = generate_magic_square(n)

    print("Starting state:")
    if state_label:
        print(f"State label: {state_label}")
    print_square(magic_square)

if __name__ == "__main__":
    main()
