# count all of the numbers that are greater than the previous numbers
# in the depth.dat file

# prime the loop with a number that could never be less than the first number
previous = 999999
count = 0
# open the file as read only
# 'with' closes the file automatically when done
with(open('depth.dat', 'r')) as f:
    # this loop will execute run until we call break
    while True:
        line = f.readline()
        # if there isn't another line the exit the loop
        if not line:
            break
        else:
            current = int(line)            
            if (current > previous):
                count += 1
            # prepare the next comparion
            previous = current

print(f'{count} larger than previous')