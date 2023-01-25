#https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
def diagonalDifference(arr):
    # Write your code here
    last_flag = len(arr)-1
    start_flag = 0
    LRD = 0 # Left to right diagonal
    RLD = 0 # Right to left diagonal

    for element in arr:
        LRD = LRD + element[start_flag]
        RLD = RLD + element[last_flag]
        start_flag +=1
        last_flag -=1
    return abs(LRD-RLD)
