from time import sleep

def countdown(n):
    while n >= 0:
        print(n)
        sleep(0.5)
        n -= 1

def countdown_rev(n):
    if n <= 0:
        print("Stop")
    else:
        print(n)
        sleep(0.5)
        counter = n-1
        countdown_rev(counter)

if __name__ == "__main__":
    # countdown(10)
    countdown_rev(10)


