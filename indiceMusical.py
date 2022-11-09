def menu():
  print('Option 1 Add')
  print('Option 2 Search')
  print('Option 3 Modify')
  print('Option 4 Print list')
  print('Option 5 Print letter')
  print('Option 0 Exit')
  eleccion = input()
  return eleccion

def addNewElement():
      name = input('Enter name\n')
      surname = input('Enter surname\n')
      element = {'name': name, 'surname': surname}
      addElement(listGlobal, element)
      print('Element added')

def addElement(list, element):
  list.append(element)

def getElement(list, element):
  return element in list

def printPretty(list):
 for i in range(len(list)):
   print('spot', i)
   print('Name: ' + list[i]['name'] + '\nSurname: ' + list[i]['surname']+ '\n')

def searchSingerByName():
  searchingName = input("Enter the artist name: ")
  for i in range(len(listGlobal)):
    if listGlobal[i]['name'] == searchingName:
      print('Is ' + listGlobal[i]['surname'] + ' in position ', i)
 
  
listGlobal = [
  {'name': 'Nora ', 'surname ': 'Jones '},
  {'name': 'Ludovico ', 'surname': 'Enaudi '},
]

letterNora = ["I waited till I saw the sun I don't know why \n I didn't come  I left you by the house of fun  I don't know why \n I didn't come  I don't know why I didn't come \n  When I saw the break of day  I wished that I could fly away"],["Instead of kneeling in the sand  Catching teardrops in my hand\n My heart is drenched in wine \n But your be on my mind  Forever"],
["I waited till I saw the sun I don't know why \n I didn't come  I left you by the house of fun  \n I don't know why I didn't come  I don't know why \n I didn't come  When I saw the break of day \n I wished that I could fly away"],["Instead of kneeling in the sand  Catching teardrops in my hand\n   My heart is drenched in wine \n But your be on my mind  Forever"],
letters = [letterNora]
#crear una única lista
#for i in range(len(listGlobal)):
#  letters.append({listGlobal[i], letterNora})

elecUser = 1
while elecUser != 0 :
  elecUser = menu()

  if elecUser == '1': 
        addNewElement()
  elif elecUser == '2':  
        searchSingerByName()
  elif elecUser == '3': 
        print('modify')
  elif elecUser == '4':
        printPretty(listGlobal)
  elif elecUser == '5':
        print(letters)      
  elif elecUser == '0': 
        print('Good bye')
        break