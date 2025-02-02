import sys
for line in sys.stdin:
    fields = line.strip().split(",")
    if len(fields) > 4 and fields[2] == "Product View":
        print(f"{fields[4]}\t1") 
