https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def pangrams(s):
    # Write your code here
    alpha = list(map(chr, range(ord('a'), ord('z')+1)))
    x = list(filter(lambda  x:x not in s.lower(),alpha))
    if len(x) == 0:

        return  "pangram"
    else:

        return "not pangram"
