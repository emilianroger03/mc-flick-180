import ctypes
import ctypes.wintypes
import os
import time

OPTIONS_PATH = os.path.join(
    os.environ["APPDATA"],
    "ModrinthApp",
    "profiles",
    "minecraft pvp AND SB SOMETIMES",
    "options.txt",
)

PEEK_TIME = 0.2
VK_XBUTTON1 = 0x05

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long), ("top", ctypes.c_long),
        ("right", ctypes.c_long), ("bottom", ctypes.c_long),
    ]

def is_pressed(vk):
    return ctypes.windll.user32.GetAsyncKeyState(vk) & 0x8000

def get_window_center():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    rect = RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
    pt = POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(pt))
    return pt.x + rect.right // 2, pt.y + rect.bottom // 2

def flick(total_dx):
    steps = 10
    step_dx = total_dx // steps
    cx, cy = get_window_center()
    for i in range(steps):
        ctypes.windll.user32.SetCursorPos(cx + step_dx, cy)
        time.sleep(0.025)

def read_sensitivity():
    with open(OPTIONS_PATH) as f:
        for line in f:
            if line.startswith("mouseSensitivity:"):
                return float(line.split(":")[1].strip())
    print("Could not find mouseSensitivity in options.txt, using default 0.5")
    return 0.5

def calc_pixels_for_180(sensitivity):
    f = sensitivity * 0.6 + 0.2
    g = f * f * f * 8.0
    degrees_per_pixel = g * 0.15
    return round(180.0 / degrees_per_pixel)

sensitivity = read_sensitivity()
pixels = calc_pixels_for_180(sensitivity)

print("MC Flick 180 - Quick Peek")
print(f"  Sensitivity: {sensitivity:.4f}")
print(f"  Pixels for 180: {pixels}")
print(f"  Button: Side button 1 (back / Button 4)")
print(f"  Peek time: {int(PEEK_TIME * 1000)}ms")
print(f"  Close this window to quit")
print()
print("Ready! Press side button.")

last_flick = 0

while True:
    now = time.time()
    if is_pressed(VK_XBUTTON1) and now - last_flick > 1.0:
        last_flick = now
        print(">> Peek!")
        flick(pixels)
        time.sleep(PEEK_TIME)
        flick(-pixels)
    time.sleep(0.001)
