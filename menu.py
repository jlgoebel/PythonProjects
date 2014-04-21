import csv

items = {"rice": 2.40, "cake": .80}
FILEPATH = "test.csv"

print "Welcome to the menu maker!"


def main_menu():
	print """
	Choose from these menu options:
	1. Add a new item to the menu.
	2. Print the menu.
	3. Enter order.
	4. Import menu.
	5. Save current menu.
	Q. Quit
	"""
	
	choice = raw_input(">> ")
	
	while True:
		if choice == "1":
			AddItem()
			main_menu()
		elif choice == "2":
			PrintItems()
			main_menu()
		elif choice == "3":
			EnterOrder()
			main_menu()
		elif choice == "4":
			ImportMenu()
			main_menu()
		elif choice == "5":
			SaveMenu()
			main_menu()
		elif choice.lower() == "q":# or choice =="q" need to find a way to auto-lowercase these
			exit()
		else:
			print "That isn't a valid option."
			main_menu()

def AddItem():
		item = raw_input("Enter the item name to add to the menu: ")
		price = raw_input("Enter the price of the item: ")
		
		try:
			intprice = float(price)
			items[item] = intprice
		except:
			print "That's not a valid price."
			AddItem()
		
def PrintItems():
	i = 1
	print "*" * 20
	print "Current list of items:"
	for food, price in items.items():
		print i, food, price
		i = i + 1
	print "*" * 20
	
def EnterOrder():
	PrintItems()
	
	#assign keys to different items in the dictionary so the user can enter numbers
	menukeys = []
	for food, price in items.items():
		menukeys.append(food)

	loop = "True"
	orderlisttwo = [] #trying with single line entry
	
	while loop == "True":
		print ("Enter the item you want to order from the list above. Enter DONE when complete")
		entry = raw_input(">> ")
		entry = entry.lower() #convert to lowercase
		if entry == "done":
			loop = "False"
		else:
			entrylist = list(entry)
			
			for x in entrylist:
				x = int(x) - 1 # make it into an integer and subtract 1
				orderlisttwo.append(menukeys[x])
				print "Adding", menukeys[x]

	#print/calculate the order
	i = 0
	NumberOfItems = len(orderlisttwo)
	TotalPrice = 0
	
	while i < len(orderlisttwo):
		ItemName = orderlisttwo[i]
		
		#get the price from the dictionary
		ItemPrice = items[ItemName]
		TotalPrice = TotalPrice + ItemPrice
		
		i = i + 1
	
	print "*" * 20
	print "The final order is:"
	for order in orderlisttwo:
		print order
	print "Total cost: ", TotalPrice
	print "*" * 20
		
def ImportMenu():
	#uses csv functions to import the file; divides the row using the comma
	#delimiter and makes a list. Then, adds the items of the list as item/price
	#to the items menu
	print "We're going to use the %r file. Okay?" % FILEPATH
	choice = raw_input(">> ")
	if choice == "yes":
		with open(FILEPATH, 'rb') as csvfile:
			importmenu = csv.reader(csvfile, delimiter=',')
			for row in importmenu:
				menuitem = ' '.join(row)
				menuitem = menuitem.split()
				items[menuitem[0]] = menuitem[1]
	

def SaveMenu():
	print "Are you sure?"
	choice = raw_input(">> ")
	if choice == "yes":
		print "Clearing file..."
		open("test", "w").close() #clears the file so we start from scratch
		
		with open(FILEPATH, 'wb') as csvfile:
			savedmenu = csv.writer(csvfile, delimiter=',')
			
			#the csv function adds the delimiter in between food & price
			for food, price in items.items():
				savedmenu.writerow([food] + [price])
		
		
#get it started!
main_menu()

