def antal_poäng():
 poäng = 0
 antal_slag = input("Skriv in antal slag på de två hålen")
 AS1 = int(antal_slag[0])
 if AS1 == 1:
  poäng += 3
 elif AS1 == 2:
  poäng += 2
 elif AS1 == 3:
  poäng += 1
 else:
  poäng += 0

 AS2 = int(antal_slag[2])
 if AS2 == 1:
  poäng += 4
 elif AS2 == 2:
  poäng += 3
 elif AS2 == 3:
  poäng += 2
 elif AS2 == 4:
  poäng += 1
 else:
  poäng += 0


 print ("Du fick " + str(poäng) + " poäng på minigolfrundan")
