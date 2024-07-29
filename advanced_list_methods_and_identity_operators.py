submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted her assignment and attended class.")
else:
    print("Alice either forgot to submit her assignment or missed class.")