import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1, y1 = map(float, input("Enter coordinates of Point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of Point 2 (x2 y2): ").split())

distance = calculate_distance(x1, y1, x2, y2)
print(f"Distance between the two points: {distance:.2f} units")

