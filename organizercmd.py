import os
import sys
import shutil
import organize

print "==============================================="
print "    Welcome to the ultimate folder organizer"
print "==============================================="

def menu():
	"This function displays the menu of the app from which user can choose"

	print "Press 1 to organize a whole folder \n" 
	print "Press 2 to organize a single folder\n"
	print "Press 3 to get help \n"
	print "Press 4 to quit the app \n"


	try:
		option = int(raw_input('>> '))

		if option == 1:
			organize.OrganizeWholeFolder()

		elif option == 2:
			organize.OrganizeSingleFolder()

		elif option == 3:
			showHelp()

		elif option == 4:
			sys.exit()

		else:
			print "Please select a valid choice from the ones above"
			menu()

	except ValueError:
		print "That is not a valid number" 
		menu()



def showHelp():
	print "This app helps you arrange and make sense of the files on your computer"
	menu()

menu()