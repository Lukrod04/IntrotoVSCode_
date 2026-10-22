orders = ["Coffee", "Tea", "Coffee", "Smoothie", "Tea", "Coffee", "Water", "Coffee"
          ]

counts = {}

for drinks in orders:
  counts[drinks] = counts.get(drinks, 0) + 1

print(counts)