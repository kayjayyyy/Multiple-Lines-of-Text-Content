# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 3 - Multiple Lines of Text Content

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(78))

# Open mylife.txt (read)
with open("mylife.txt", "w") as input_txt_file:
    while True:
        # Ask for the users inpot
        text = input("\nEnter the line you want to extract in txt file: ")
        input_txt_file.write(text + "\n")
        # Loop the program until the users say no to end it
        while True:
            yes_or_no = input("\nAre there more lines y/n? ")
            # If yes "y", ask again for the users input
            if yes_or_no.lower() == "y":
                break
            else:
                break
        # If no "n", stop the program
        if yes_or_no.lower() == "n":
            break
        
# Close the program/txt file
input_txt_file.close()    

# Outro and border line
print("\n")
print("\033[33mPlease check for the mylife.txt file\033[0m".center(80))
print("\n")
print("\033[3mThank you! Have a great day!".center(70))
print("")
print("\033[35m※ \033[0m" * 35)
print("")