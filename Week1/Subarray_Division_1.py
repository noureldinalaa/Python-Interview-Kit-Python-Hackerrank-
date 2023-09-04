https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one


def birthday(s, d, m):
    # Use a sliding window to create all contiguous subarrays of size m
    segments = []
    for i in range(len(s) - m + 1):
        slide_window = s[i:i+m]
        segments.append(slide_window)
    # Filter the segments whose sum is equal to d
    valid_segments = list(filter(lambda segment: sum(segment) == d, segments))
    
    # Return the number of valid segments
    return len(valid_segments)
