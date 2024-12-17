def parse_fraction(input_str):
    if '/' in input_str:
        numerator, denominator = input_str.split('/')
        return float(numerator) / float(denominator)
    else:
        return float(input_str)

def det(A):
    size = len(A)
    B = [row[:] for row in A]
    determinant = 1
    for i in range(size):
        if B[i][i] == 0:
            for j in range(i + 1, size):
                if B[j][i] != 0:
                    B[i], B[j] = B[j], B[i]
                    determinant *= -1 
                    break
            else:
                return 0  
        
        for j in range(i + 1, size):
            if B[j][i] != 0:
                factor = B[j][i] / B[i][i]
                for k in range(i, size):
                    B[j][k] -= factor * B[i][k]

    for i in range(size):
        determinant *= B[i][i]

    return determinant

def cramer(A, b):
    n = len(A)
    determinant = det(A)

    if determinant == 0:
        print("The system is inconsistent (no solution).")
        return

    det_values = []

    for var in range(n):
        modifiedA = [row[:] for row in A]
        for i in range(n):
            modifiedA[i][var] = b[i]

        detModified = det(modifiedA)
        det_values.append(detModified)

        print(f"x{var + 1} = {detModified / determinant:.6f}")

    if determinant != 0:
        print("The system is consistent with a unique solution.")
    else:
        print("The system is inconsistent (no solution).")

def main():
    mode = int(input("Select mode (1: Determinant, 2: Cramer's Rule): "))
    
    if mode not in [1, 2]:
        print("Invalid mode selected!")
        return

    m = int(input("Enter the size of the square matrix (m=n): "))

    A = []
    for row in range(m):
        A.append([parse_fraction(input(f"Enter matrix element [{row}][{col}]: ")) for col in range(m)])  # ใช้ parse_fraction ที่นี่

    if mode == 1:
        print("Matrix:")
        for row in A:
            print("\t".join(map(str, row)))
        
        determinant = det(A)
        print(f"Determinant = {determinant}")
    
    elif mode == 2:
        b = [parse_fraction(input(f"Enter constant element b[{i}]: ")) for i in range(m)]  # ใช้ parse_fraction ที่นี่
        cramer(A, b)

if __name__ == "__main__":
    main()
