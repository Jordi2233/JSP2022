import os, itertools

def main():
    os.system('clear')
    arr = [[2,4,3],[1,5,6],[9],[7,9,0]]
    arr = list(itertools.chain(arr[0], arr[1], arr[2]))
    print(arr)

if __name__ == "__main__":
    main()
