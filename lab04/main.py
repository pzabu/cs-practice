from stats import average_by_city, read_valid, warmest_city
import sys
lines = sys.stdin.read().splitlines()
res = read_valid(lines)
print(len(res))
print(len(lines)-len(res))
print(average_by_city(res)[warmest_city(res)])

