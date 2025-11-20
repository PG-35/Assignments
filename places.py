places = ["Germany","France","Spain","Argentina","Russia"]
print(places)


print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nStill in original order:")
print(places)

places.reverse()
print("\nAfter reverse():")
print(places)


places.reverse()
print("\nAfter reverse() again (back to original):")
print(places)

places.sort()
print("\nAfter sort() alphabetical:")
print(places)

places.sort(reverse=True)
print("\nAfter sort() reverse Operation (Not Aphabetical)")
print(places)
