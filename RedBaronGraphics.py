# Graphics thingy
import time
      

def opening_graphic():
    print("  |\   __  \|\  ___ \ |\   ___ \        |\   __  \|\   __  \|\   __  \|\   __  \|\   ___  \ ")
    time.sleep(0.2)
    print("  \ \  \|\  \ \   __/|\ \  \_|\ \       \ \  \|\ /\ \  \|\  \ \  \|\  \ \  \|\  \ \  \\ \  \ ")
    time.sleep(0.2)
    print("   \ \   _  _\ \  \_|/_\ \  \ \\ \       \ \   __  \ \   __  \ \   _  _\ \  \\\  \ \  \\ \  \ ")
    time.sleep(0.2)
    print("    \ \  \\  \\ \  \_|\ \ \  \_\\ \       \ \  \|\  \ \  \ \  \ \  \\  \\ \  \\\  \ \  \\ \  \ ")
    time.sleep(0.2)
    print("     \ \__\\ _\\ \_______\ \_______\       \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\\ \__\ ")
    time.sleep(0.2)
    print("      \|__|\|__|\|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|\|_______|\|__| \|__| ")




import time

def animate_graphic():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 5:
            break
        # Clear the terminal
        print("\033c", end="")
        
        # Print the graphic with different colors
        if int(elapsed_time * 2) % 2 == 0:
            print("\033[31m", end="")
        else:
            print("\033[32m", end="")
        opening_graphic()
        
        # Wait for a short time
        time.sleep(0.5)


def opening_graphic2():
    print("")