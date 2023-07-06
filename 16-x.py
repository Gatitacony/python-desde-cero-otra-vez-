# Dibujar una x de tamaño 10 utilizando el *




equis = { 1:["'   ,--,  ,--,'"], 2:["'   |'. \/ .`|'" ],3: [f"'   '  \/  / ;'" ],4:["'    \  \.' /'" ],4:["'     \  ;  ;'"], 5:["'    / \  \  \ ' " ], 6:["'  ./__;   ;  \ ' "], 7:["'  |   :/\  \ ;'" ], 8:["'  `---'  `--`'"]}

       
       
# Dibujar una x de tamaño 12 utilizando el *
# *               *
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# *               *


for y in range(1,12):
  line = ""
  for x in range(1,12):
    if (x == y) or (x + y == 12):
      line += "*"
    else:
      line += " "
  print(line)

        


