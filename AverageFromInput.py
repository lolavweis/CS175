total = 0
count = 0

# Open the file for reading
with open("numbers.txt", "r") as file:
    for line in file:
        try:
            number = int(line)
            count += 1
            total += number
            print(f'I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}')
        except ValueError:
            print(f"Skipped a non-integer value: {line.strip()}")

# Calculate the average
if count > 0:
    average = total / count
    print(f"Average: {average:6.1f}")
else:
    print("No valid numbers found in the file.")
