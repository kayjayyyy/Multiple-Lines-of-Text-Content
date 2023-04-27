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