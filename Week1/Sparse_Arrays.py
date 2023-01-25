# https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
def matchingStrings(strings, queries):
  # Write your code here
  numbers=[]
  for quary in queries:
      quary = [quary]
      number = len(list(filter(lambda x: x in quary,strings)))
      numbers.append(number)
  return numbers
