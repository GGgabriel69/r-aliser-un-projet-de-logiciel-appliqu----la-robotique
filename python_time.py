import threading
import time
print("Début")

def my_callback():
    print("fin")
    
def start_timer(seconds, callback):
    def my_sleep():
        for i in range(1, 6):
            print(i,"bateau bateau")
            time.sleep(seconds)
            
        callback()
    
    thread = threading.Thread(target=my_sleep)
    thread.start()

# Start a 5-second timer with a callback
start_timer(1, my_callback)



