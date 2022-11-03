import os, math
os.system('clear')

given_list = input("Enter RGB color like '255 255 255': ").split()
given_list = [int(num) for num in given_list]

def RGB2HSV(arr):

# Check and add or remove items to always have 3 elements

    if len(arr) == 1:
        arr.extend((0, 0))
    elif len(arr) == 2:
        arr.append(0)
    else:
        del arr[3:]



    R = arr[0]/255.0
    G = arr[1]/255.0
    B = arr[2]/255.0

    Cmax = max(R, G, B)
    Cmin = min(R, G, B)
    D = Cmax-Cmin

    if Cmax == Cmin:
        H = 0
    elif Cmax == R:
        H = (60 * ((G - B) / D) + 360) % 360
    elif Cmax == G:
        H = (60 * ((B - R) / D) + 120) % 360
    elif Cmax == B:
        H = (60 * ((R - G) / D) + 240) % 360

    if Cmax == 0:
        S = 0
    else:
        S = (D / Cmax) * 100

    V = Cmax * 100

    return (H, S, V)

print(RGB2HSV(given_list))
