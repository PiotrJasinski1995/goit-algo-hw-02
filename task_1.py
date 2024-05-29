import random, keyboard
from classes.request_queue import Request_Queue
import time
import msvcrt

def main():
    queue = Request_Queue(maxsize=10)
    start_program = False
    print('Hello! Press "s" to start and "q" to exit:\n')

    while True:
        if start_program:
            create_amount = random.randint(0, queue.maxsize)
            for i in range(create_amount):
                if not queue.full():
                    time.sleep(0.3)
                    queue.generate_request()
            
            delete_amount = random.randint(0, queue.qsize())
            for i in range(delete_amount):
                if not queue.empty():
                    time.sleep(0.3)
                    queue.process_request()
        
        # Check for a key press to break the loop
        if msvcrt.kbhit():
            key = msvcrt.getch().decode()

            if key == 's' and not start_program:
                print("Program started.")
                start_program = True
            elif key == 'q':
                print("Loop terminated by user.")
                break
    
    print('Goodbye!')

if __name__ == '__main__':
    main()
