### https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def twoArrays(k, A, B):
    # Write your code here
    for i in range(len(A)):
        B = sorted(B,reverse=True)
        A = sorted(A)
        if B[i]+A[i] < k:
            return "NO"
    return "YES"
