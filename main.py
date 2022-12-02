import time

from delivery import Delivery
from gui import GUI

SLEEP_TIME = 60

def main():
    while True:
        Delivery().run()
        GUI().update()
        print(f"Sleeping for {SLEEP_TIME} seconds.")
        print("———————————————————————————————————")
        print()
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
