"""Modifying Global variable"""

ENEMIES = 1

def increase_enemies():
    global ENEMIES 
    ENEMIES += 1
    print(f"Enemies inside the function: {ENEMIES}")

increase_enemies()
print(f"Enemies outside the function: {ENEMIES}")
