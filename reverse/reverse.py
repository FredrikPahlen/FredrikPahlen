def kör():
  list = []
  tal = (input("Hur många siffror ska listan innehålla?"))
  if tal == 2:
    a, b, = (input("skriv in dina två tal här, separerade av kommatecken").split())
    list.append(a)
    list.append(b)
    list.reverse()
    print (list)

  else if tal == 3:
   a, b, c = (input("skriv in dina tre tal här, separerade av kommatecken").split())
   list.append(a)
   list.append(b)
   list.append(c)
   list.reverse()
   print (list)

  else if tal == 4:
   a, b, c, d = (input("skriv in dina fyra tal här, separerade av kommatecken").split())
   list.append(a)
   list.append(b)
   list.append(c)
   list.append(d)
   list.reverse()
   print (list)

  else if tal == 5:
   a, b, c, d, e = (input("skriv in dina fem tal här, separerade av kommatecken").split())
   list.append(a)
   list.append(b)
   list.append(c)
   list.append(d)
   list.append(e)
   list.reverse()
   print (list)
