locations = ["Japan", "Iceland", "Switzerland", "Egypt", "Canada"]

print("Original:", locations)
print("Sorted:", sorted(locations))
print("Original again:", locations)
print("Reverse Sorted:", sorted(locations, reverse=True))
print("Original again:", locations)

locations.reverse()
print("Reversed:", locations)
locations.reverse()
print("Back to original:", locations)

locations.sort()
print("Sorted permanently:", locations)
locations.sort(reverse=True)
print("Reverse sorted permanently:", locations)