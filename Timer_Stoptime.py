import time

def countdown_timer():
    seconds = int(input("Enter the countdown time in seconds: "))
    while seconds > 0:
        print(f"Time left: {seconds} seconds", end="\r")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("\nTime's up!")

def stopwatch():
    print("Press Enter to start the stopwatch. Press Enter again to stop it.")
    input()  # Wait for user to press Enter
    start_time = time.time()
    input()  # Wait for user to press Enter again
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def main():
    print("Choose an option:")
    print("1. Timer")
    print("2. Stopwatch")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        countdown_timer()
    elif choice == "2":
        stopwatch()
    else:
        print("Invalid choice. Exiting.")

main()