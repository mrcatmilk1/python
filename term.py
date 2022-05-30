from string import ascii_letters
password = "a341uH%/wi29sussybakafr22tr22@@jeok050709bluecat22"
ice = input("Icebreaker: ")
lock = list(ascii_letters) + ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '.', ',', '<', '>', '/', '|', ']', '[', '{', '}', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
pw = list(password)
i = 0
j = 0
icebreaker = ""
vis = ""
if ice == 'y':
    while icebreaker != password:
        while lock[i] != pw[j]:
            vis += icebreaker + lock[i] + """
            """
            print(vis)
            i += 1
        icebreaker += lock[i]
        i = 0
        j += 1
    print(f'Password: {icebreaker}')
if icebreaker == password:
    print("Success.")
if ice != 'y' and ice != 'n':
    print("Invalid input, try again (y/n) ")
    ice = input("Icebreaker: ")
    if ice == 'y':
        while icebreaker != password:
            while lock[i] != pw[j]:
                i += 1
            icebreaker += lock[i]
            i = 0
            j += 1
        print(f'Password: {icebreaker}')
    if icebreaker == password:
        print("Success.")
if ice == 'n':
    guess = input("Password: ")
    if guess == password:
            print("Success.")
    else:
        print(f'Incorrect password; 2 tries left.')
        guess = input("Password: ")
        if guess != password:
            print(f'Incorrect password; 1 try left')
            guess = input("Password: ")
        if guess != password:
            print("Locked out.")
            quit()
        if guess == password or icebreaker == password:
            print("Success.")
name = input("Name: ").upper()
id = input("ID: ")
while name != "DISCORD" and id != "261827216":
    while name != "DISCORD" or id != "261827216":
        print("Invalid name or ID, please try again.")
        name = input("Name: ").upper()
        id = input("ID: ")
if name == "DISCORD" and id == "261827216":
    print("Logged in.")
    op = input("Enter file name: ").upper()
    if op != "OPERATION GRAVEDIGGER":
        print("Invalid file.")
        op = input("Enter file name: ").upper()
        while op != "OPERATION GRAVEDIGGER":
            print("Invalid file.")
            op = input("Enter file name: ").upper()
    if op == "OPERATION GRAVEDIGGER":
        print("""
        MARAS OFFICIAL C-LOGS
        
        PRITAS

        HAMMERHEAD, ATSAL-6 - TL7 PRI
        REINDEER - TL5

        SECTAS

        SNOWMAN, OMID-2 DESTINY MARAS MAJ
        ATSAL-2 GC

        CARROT TEAM

        OMID-1 DISCORD MARAS LTCOL
        OMID-4 DAYBREAK MARAS MGYSGT (POSOOP)
        OMID-5 DEATHBRINGER MARAS SSGT
        """)
while True:
    back = input("Go back: ").lower()
    if back != 'y' and back != 'n':
        print("Invalid input, try again (y/n) ")
    if back == "y":
        op = input("Enter file name: ").upper()
        if op != "OPERATION GRAVEDIGGER":
            print("Invalid file.")
            op = input("Enter file name: ").upper()
            while op != "OPERATION GRAVEDIGGER":
                print("Invalid file.")
                op = input("Enter file name: ").upper()
        if op == "OPERATION GRAVEDIGGER":
            proceed = input("Accessing file... proceed? (y/n) ")
            if proceed == 'y':
                print("""
                MARAS OFFICIAL C-LOGS

                PRITAS

                HAMMERHEAD, ATSAL-6 - TL7 PRI
                REINDEER - TL5

                SECTAS

                SNOWMAN, OMID-2 DESTINY MARAS MAJ
                ATSAL-2 GC

                CARROT TEAM

                OMID-1 DISCORD MARAS LTCOL
                OMID-4 DAYBREAK MARAS MGYSGT (POSOOP)
                OMID-5 DEATHBRINGER MARAS SSGT
                """)
            else:
                print("Quitting...")
                quit()
    if back == "n":
        quit()