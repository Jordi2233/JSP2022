import os, math
os.system('clear')

mod = input("What do you want to do? (RGB2HSV or HSV2RGB: ")
mod = mod.upper()


def RGB2HSV(arr):

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

    H = round(H, 2)
    S = round(S, 2)
    V = round(V, 2)

    return (H, S, V)

def HSV2RGB(arr):

    H = arr[0]
    S = arr[1]
    V = arr[2]

    if 0 <= H < 360 and 0 <= S <= 1 and 0 <= V <= 1:
        C = S * V
        X = C * (1 - ((H / 60) % 2 - 1))
        m = V - C

    if 0 <= H < 60:
        R = C
        G = X
        B = 0
    elif 60 <= H < 120:
        R = X
        G = C
        B = 0
    elif 120 <= H < 180:
        R = 0
        G = C
        B = X
    elif 180 <= H < 240:
        R = 0
        G = X
        B = C
    elif 240 <= H < 300:
        R = X
        G = 0
        B = C
    elif 300 <= H < 360:
        R = C
        G = 0
        B = X

    R = (R + m) * 255
    G = (G + m) * 255
    B = (B + m) * 255
    if R > 255:
        R = 0
    if G > 255:
        G = 0
    if B > 255:
        B = 0
    return (R, G, B)


given_list = input("Enter color like '255 255 255': ").split()
given_list = [int(num) for num in given_list]

if len(given_list) == 1:
    given_list.extend((0, 0))
elif len(given_list) == 2:
    given_list.append(0)
else:
    del given_list[3:]

if mod == "RGB2HSV":
    res = RGB2HSV(given_list)
elif mod == "HSV2RGB":
    res = HSV2RGB(given_list)

print(res)

