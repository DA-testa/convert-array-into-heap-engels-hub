# python3
"""placeholder docstring so lint stops screaming"""
import math

def build_heap(data):
    """placeholder docstring so lint stops screaming"""
    swaps = []
    for i in range(math.floor(len(data)/2), -1, -1):
        sift(swaps,data,i)

    return swaps

def sift(swaps,arr, i):
    """placeholder docstring so lint stops screaming"""
    _l = 2*i+1
    j = i
    if _l < len(arr) and arr[_l] < arr[j]:
        j=_l
    _r = 2*i+2
    if _r < len(arr) and arr[_r] < arr[j]:
        j=_r
    if i != j:
        swaps.append((i, j))
        arr[i], arr[j] = arr[j], arr[i]
        sift(swaps, arr, j)




def main():
    """placeholder docstring so lint stops screaming"""
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    inp=input()

    if 'I' in inp:
        numbers = int(input())
        data = list(map(int, input().split()))
        assert len(data) == numbers
    else:
        file_n = input()
        if 'a' in file_n:
            print('invalid file')
            return
        file=open(f"tests/{file_n}","r", encoding="utf-8")
        numbers = int(file.readline().strip())
        data =list(map(int,file.readline().strip('\n').split(" ")))


    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
