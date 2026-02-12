import numpy as np

try:
    coords = input("Enter elements: ")
    if ',' in coords:
        coords = np.array([int(x.strip()) for x in coords.split(',')])
    else:
        coords = np.array([int(x) for x in coords.split()])

    mean = np.mean(coords)
    std = np.std(coords)
    threshold = mean + std
    mask = coords > threshold

    print(f"original array: {coords.tolist()}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std}")
    print(f"Threshold: {threshold}")
    print(f"Mask: {mask.tolist()}")

    coords[mask] = mean
    print("array after replacing outliers:", coords.tolist())

except ValueError:
    print("Invalid input. Please enter integers only.")
