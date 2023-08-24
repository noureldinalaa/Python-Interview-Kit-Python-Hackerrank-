# Link to the problem:
#https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def countingSort(arr):
    # Write your code here
    counting_array = [0]*100
    for i in arr:
        counting_array[i] = counting_array[i] +1

    return counting_array
