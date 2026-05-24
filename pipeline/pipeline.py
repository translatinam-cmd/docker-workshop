import sys

sys.argv = [sys.argv[0], "1"]  # For testing purposes, set month to 1

print("arguments", sys.argv)

month = int(sys.argv[1])

print(f"hello pipeline, month={month}")