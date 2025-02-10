import pandas as pd

def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x2 - x1 == 0:
        return float('inf')  # Vertical line with undefined slope
    return round((y2 - y1) / (x2 - x1), 3)

def all_possible_slopes(points):
    slopes = []
    serial = 1
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            slope = calculate_slope(points[i], points[j])
            slopes.append((serial, points[i], points[j], slope))
            serial += 1
    return slopes

# Example usage:
a=5.06
b=3.1
c=3.01
d=2.99
e=2.78
points = [(6.38,a),(5.33,b),(5.13,c),(4.84,d),(4.62,e)]
result = all_possible_slopes(points)

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Serial', 'Point 1', 'Point 2', 'Slope'])

# Save the DataFrame to an Excel file
output_file = 'slopes_output.xlsx'
df.to_excel(output_file, index=False)

print(f"Data has been saved to '{output_file}'.")
