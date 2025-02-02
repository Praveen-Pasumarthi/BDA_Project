import sys
from collections import defaultdict

product_counts = defaultdict(int)
for line in sys.stdin:
    product, count = line.strip().split("\t")
    product_counts[product] += int(count)

for product, count in product_counts.items():
    print(f"{product}\t{count}")  # Output: ProductID → Total Views
