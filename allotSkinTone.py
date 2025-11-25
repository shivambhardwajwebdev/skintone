def allotSkin(colorsList):
    # These are the 5 reference colors from the original skin.png
    colors = [
        [59, 34, 25],      # Index 0
        [161, 110, 75],    # Index 1
        [212, 170, 120],   # Index 2
        [230, 188, 152],   # Index 3
        [255, 231, 209]    # Index 4
    ]

    # We assign a descriptive name to each color above
    # You can change these text strings to whatever you want your website to say
    skin_labels = [
        "Dark Ebony (Cool)",      # Index 0
        "Medium Dark (Warm)",     # Index 1
        "Medium (Warm)",          # Index 2 (This matches your [212, 170, 120])
        "Fair (Cool)",            # Index 3
        "Light / Pale (Warm)"     # Index 4
    ]

    diffList = []
    for i in range(5):
        diff = diffColor(colorsList, colors[i])
        diffList.append(diff)
    
    # Find the index of the smallest difference
    indexOfMinDist = diffList.index(min(diffList))
    
    # Return the Text Label instead of the numbers
    return skin_labels[indexOfMinDist]

def diffColor(colorsList, colorX):
    x1 = abs(colorsList[0] - colorX[0])
    x2 = abs(colorsList[1] - colorX[1])
    x3 = abs(colorsList[2] - colorX[2])
    # Use basic Euclidean distance logic
    x = int(x1 + x2 + x3)
    return x