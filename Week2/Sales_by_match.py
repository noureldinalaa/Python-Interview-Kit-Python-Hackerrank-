# https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

from collections import Counter
def sockMerchant(n, ar):


    socks_count = Counter(ar)
    pairs = sum(val // 2 for val in socks_count.values())

    return pairs
