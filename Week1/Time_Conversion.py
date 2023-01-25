# https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
def timeConversion(s):
    # Write your code here
    t = datetime.strptime(s, '%I:%M:%S%p')
    # Format nto a 24-hour time string
    t_24 = t.strftime('%H:%M:%S')
    return t_24
