import time
from pynput.mouse import Button, Controller, Listener

mouse = Controller()
INTERVAL = 10  

print("Auto-clicker démarré. F8 pour quitter.")

running = True
last_click = 0.0

def on_press(key):
    global running
    if key == key.f8:
        running = False
        return False

with Listener(on_press=on_press) as listener:
    while running:
        now = time.time()
        if now - last_click >= INTERVAL:
            pos = mouse.position
            print(f"Clic à {pos} - {time.strftime('%H:%M:%S')}")
            mouse.click(Button.left)
            last_click = now
        time.sleep(0.1)
