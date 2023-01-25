# https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
def lonelyinteger(a):
    # Write your code here
    n = list(filter(lambda x:a.count(x)==1,a))
    return n[0]
