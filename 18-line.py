# Significados= row: filas. range: 11 filas hacia abajo. line: Linea. clos: Columnas.

for row in range(10):
    line = ""
    for col in range(10):
        if(row == 0 or row == 9):
            line += "*"
        else:
            line  += " "
    print(line)