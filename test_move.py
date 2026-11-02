import ctypes
import ctypes.wintypes
import time

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

print("DON'T TOUCH YOUR MOUSE!")
print("Moving in 3 seconds...")
time.sleep(3)

# Get current position
pt = POINT()
ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
print(f"Cursor start: {pt.x}, {pt.y}")

# Method 1: mouse_event
print("Test 1: mouse_event (relative move)...")
for i in range(20):
    ctypes.windll.user32.mouse_event(0x0001, 50, 0, 0, 0)
    time.sleep(0.02)

time.sleep(0.5)
ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
print(f"Cursor after test 1: {pt.x}, {pt.y}")

# Method 2: SetCursorPos
print("Test 2: SetCursorPos (absolute move)...")
ctypes.windll.user32.SetCursorPos(pt.x + 300, pt.y)

time.sleep(0.5)
ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
print(f"Cursor after test 2: {pt.x}, {pt.y}")

print("Done! Which test moved your cursor?")
