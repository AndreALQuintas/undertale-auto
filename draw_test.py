import win32gui
import win32con
import win32api

# Get the screen dimensions
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# Define a window class
wc = win32gui.WNDCLASS()
wc.lpszClassName = "Overlay"  # Window class name
wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
wc.hInstance = win32gui.GetModuleHandle(None)
wc.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
wc.lpfnWndProc = win32gui.DefWindowProc

# Register the window class
win32gui.RegisterClass(wc)

print("rawr")

# Create a top-level transparent window
hwnd = win32gui.CreateWindowEx(
    win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT,
    "Overlay",
    "Overlay",
    win32con.WS_POPUP,
    0,
    0,
    screen_width,
    screen_height,
    None,
    None,
    wc.hInstance,
    None
)

print("rawrwarr")

# Make the window transparent and click-through
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TRANSPARENT)

# Create a device context (DC)
dc = win32gui.GetDC(hwnd)
print("rawrwarr")
# Draw a red rectangle on the screen
left, top, right, bottom = 100, 100, 300, 300  # Rectangle coordinates
red = win32api.RGB(255, 0, 0)
win32gui.FillRect(dc, (left, top, right, bottom), red)

# Update the window to show the drawing
win32gui.UpdateWindow(hwnd)
print("rawrwarr")
# Message loop to keep the window open
win32gui.PumpMessages()
