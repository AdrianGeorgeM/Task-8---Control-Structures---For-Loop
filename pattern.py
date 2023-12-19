# Total number of lines in the pattern
total_lines = 9

# Loop through each line
for i in range(1, total_lines + 1):
    # Determine if we are in the increasing or decreasing part of the pattern
    if i <= (total_lines // 2) + 1:
        # For the first half, print increasing number of stars
        print('*' * i)
    else:
        # For the second half, print decreasing number of stars
        print('*' * (total_lines - i + 1))
