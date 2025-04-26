#Alan Hernández Badillo
import numpy as np

#Solucionador de Sistemas de Ecuaciones Lineales para Matrices Cuadradas
def nosol(matriz):
    for fila in matriz:
        if all(elemento == 0 for elemento in fila[:-1]) and fila[-1] != 0:
            return True
    return False

def inf(matriz):
    for fila in matriz:
        if all(elemento == 0 for elemento in fila):
            return True
    return False

print("Welcome to the linear equation solver of the form Ax=b where A is a square matrix (nxn) and b a vector with constant values")

ans=True

while ans:

    print("""
    1.Begin
    2.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans=="1":
      n =int(input("Write the value for n: "))

      A = np.zeros((n,n))

      for i in range(n):
          for j in range(n):
                  A[i, j] = float(input(f"Write the value for row {i + 1} column {j + 1}: "))

      d= all(all(elemento < 1 for elemento in fila) for fila in A)
      
      if d:
          for fila in range(len(A)):
              for columna in range(len(A[0])):
                  A[fila][columna] *= 10
          print(A)        
      else:
          print(A)

      b = np.zeros((n,1))

      for i in range(n):
          b[i, 0] = float(input(f"Write matrix with independent terms {i + 1}: "))

      print(b)

      detA = np.linalg.det(A)
      print("\nThe determinant is: \n")
      print(detA)

      if detA!=0:
        C = np.concatenate((A, b), axis=1)
        print("\nThe extended matrix is:")
        print(C)
        for j in range(len(C)):
        
            print(f'\nModifying the elements of the COLUMN {j+1}:\n')
            if C[j, j] != 1 and C[j, j] != 0:
                print(f"Operation performed: Row{j+1}/{C[j, j]}")
                C[j, :] = C[j, :] / C[j, j]
                print(C)
            else:
                print(f"\nRow {j+1} wasn't modified.\n")

            for i in range(len(C)):
                if i != j:
                    print(f"Modifying the elements of the ROW {i+1}...")
                    print(f"Operación realizada: Row {i+1} - ({C[i, j]}) * row {j+1}")
                    C[i, :] = C[i, :] - C[i, j] * C[j, :]
                    print(C)
                    
            if inf(C):
                if nosol(C):
                    print("The system has no solution")
                else:
                    print("The system has infinitely many solutions")
            else:
                if nosol(C):
                    print("The system has no solution")
                else:
                    print("The system has one solution")
                    x = np.linalg.solve(A,b)
                    print(x)

                        

      else:
        print("The system either has no solution or has infinitely many solutions")
        C = np.concatenate((A, b), axis=1)
        print("\nThe extended matrix is:")
        print(C)
        for j in range(len(C)):
            print(f'\nModifying the elements of the COLUMN {j+1}:\n')
            if C[j, j] != 1:
                print(f"Operation performed: Row{j+1}/{C[j, j]}")
                if C[j, j] == 0:
                    print(C)
                else:  
                    C[j, :] = C[j, :] / C[j, j]
                    print(C)
            else:
                print(f"\nRow {j+1} wasn't modified.\n")

            for i in range(len(C)):
                if i != j:
                    print(f"Modifying the elements of the ROW {i+1}...")
                    print(f"Operación realizada: Row {i+1} - ({C[i, j]}) * row {j+1}")
                    C[i, :] = C[i, :] - C[i, j] * C[j, :]
                    print(C)
                    
            if inf(C):
                if nosol(C):
                    print("The system has no solution")
                else:
                    print("The system has infinitely many solutions")
            else:
                if nosol(C):
                    print("The system has no solution")

                    
    elif ans=="2":
      print("\nDe nada, vuelva prontooo")
      ans = None
    else:
      print("\n Not Valid Choice Try again")