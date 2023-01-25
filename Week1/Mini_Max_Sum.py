# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

    def miniMaxSum(arr):
            # Write your code here
            for i in range (len(arr)):
                 sum_array.append(sum(arr)-arr[i]) 
            print(str(min(sum_array)) + " " + str(max(sum_array)))
