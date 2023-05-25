# Commands for the "Coord" input function, "Restock" : restocks the vending machine, "Stats" shows the stats detailing the selected vending machine

# Main classes


class stock():
  """Object to be sold in vending machines, obj.name, price, max stock per index"""

  def __init__(self, name, price, maxStockIndex):
    self.name = name
    self.price = price
    self.maxStockIndex = maxStockIndex

class vending_machine():
  """vending machine object, obj.name, location, stock"""

  def __init__(self, name, location, stock):
    self.name = name
    self.location = location
    self.stock = stock

    j = []
    for l in range(0, len(stock)):
      j.append(stock.get(l).maxStockIndex)

    self.StockPerIndex = j

    # StockPerIndex = [obj.msi, obj.msi, obj.msi, ...], can be changed individually

    self.sales = 0
    self.total = 0

  #

  def displayStats(self):
    print(f"\n{self.sales} total sales \n£{self.total} total money earned")

  def displayStock(self):
    o = 0

    print("")
    for l in range(0, len(self.stock)):
      if self.stock.get(l).name == "Empty":
        continue
      print(
        f"{o+1}. {self.stock.get(l).name} - {self.StockPerIndex[o]} - £{self.stock.get(o).price}"
      )
      o += 1

    print("")

  #

  def vend(self, coord):
    """Returns a sodas name and drink by index, increments the object's "stock" attribute by -1"""
    cStock = self.StockPerIndex[coord]
    cObj = self.stock.get(coord)
    print(f"{cObj.name} selected. £{cObj.price}")

    if cStock == 0:
      return f"{cObj.name} is Out Of Stock" if cObj != stockL[
        0] else "Out Of Stock"

    money = intInput("How much money to enter? (pence): ") / 100

    if money < cObj.price:
      inc = intInput(
        f"Please add more money \n{money} entered of {cObj.price}: ") / 100
      money += inc

    change = str(money - cObj.price)

    dispTrue = input(f"Dispense {cObj.name}? Y/N ")
    dispTrue = True if dispTrue[0].upper() == "Y" else False

    if dispTrue == False:
      return "Vend cancelled"

    self.StockPerIndex[coord] = self.StockPerIndex[coord] - 1
    self.sales += 1
    self.total += cObj.price

    return f"\n{cObj.name} dispensed \n£{cObj.price} charged \n£{change[0:4]} as change\n\nThank you for buying\n"

  #

  def restock(self):
    j = []
    for l in range(0, len(self.stock)):
      j.append(self.stock.get(l).maxStockIndex)

    self.StockPerIndex = j


# Functions


def intInput(string):
  """takes user input until the input recieved is an integer"""
  a = ""
  while not a.isdigit():
    a = input(string)
  return int(a)


def addStock(name, price, stockP):
  """Appends a stock object to the stockL list"""
  stockL.append(stock(name, price, stockP))


#


def formDict(array):
  """Forms a dictionary of length 10, Array = [1, 7, 5, 8, 9, 21]
        {index : stock} 
    """
  while len(array) < 10:
    array.append(0)
  out = {}
  for i, v in enumerate(array):
    out[i] = stockL[v]
  return out


#


def formVendingMachine(name, location, dict):
  """Adds a vending machine object to a list"""
  vendingMachines.append(vending_machine(name, location, dict))


# Interface Procedure


def displayVendingMachine():
  for i, v in enumerate(vendingMachines):
    print(f"{i+1}. {v.name} - {v.location}")


# Main script

stockL = []
vendingMachines = []

addStock("Empty", 0, 0)  # Default / placeholder for the vending machines # 0
addStock("Coke", 1.75, 7) # 1
addStock("Crisps", 2.5, 4) # 2
addStock("Pepsi", 1.5, 2) # 3
addStock("Fanta", 1.99, 3) # 4 
addStock("Doritoes", 1.60, 8) # 5
addStock("Cream Soda", 1.65, 6) # 6
addStock("A Raw Egg", .50, 12)# 7

# These can be used to create infinite amounts of vending machines

basic = formDict([1, 2, 3, 4, 5, 6, 7])
pepsi = formDict([3,3,3,3,3])
cola = formDict([1, 1, 1, 1, 1])
beverages = formDict([1, 3, 4, 6])
eggs = formDict([7, 7, 7, 7, 7, 7])

formVendingMachine("Main", "Cafeteria", basic)
formVendingMachine("Food", "Library", basic)
formVendingMachine("Pepsi", "Break Room", pepsi)
formVendingMachine("Coke", "The Mall", cola)
formVendingMachine("Larry", "Canteen", beverages)
formVendingMachine("Eggs", "The Farm", eggs)
formVendingMachine("Break Room", "Teachers 'Lounge'", formDict([1,2,5,4,7]))

cMachine = vendingMachines[0]

iterateT = True  # Controls loop iteration, set to False when a vending machine has been selected, set back during coord selection

while True:
  while iterateT:
    if iterateT:

      print('\x1B[4m' + ("\nSelect a vending machine: ") + '\x1B[0m')
      displayVendingMachine()

      vendC = len(vendingMachines) + 2
      while vendC > len(vendingMachines):
        vendC = intInput("\nChoose Machine:") - 1

      try:
        cMachine = vendingMachines[vendC]
      except IndexError:
        print("Not valid \nMachine 1 selected as default")
        iterateT = True

      cMachine.displayStock()
      iterateT = False

  vendCoord = input("Coord: ")

  if vendCoord.isdigit():
    vendCoord = int(vendCoord)

  else:
    iterateT = True
    if vendCoord[0].lower() == "r":
      cMachine.restock()
    elif vendCoord[0].lower() == "s":
      cMachine.displayStats()
    else:
      print("Not an accepted input")

  if iterateT == False:
    iterateT = True
    print(f"{cMachine.vend(vendCoord-1)}")
