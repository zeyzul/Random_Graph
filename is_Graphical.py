# Input: a degree sequence d
# Output: True if the sequence is graphical and False otherwise

# Uses Havel Hakimi Theorem

def is_Graphical(degrees):

    while -1 not in degrees:
        degrees.sort(reverse=True)  # re-sort the list at each iteration

        i = degrees.pop(0)  # remove the first element
        count = 0
        for j in range(i):  # subtract 1 from first i elements of the degree
            try:
                degrees[count] -= 1
            except:
                return False
            count += 1

        if len(degrees) == 0:
            # if we never reach a negative value then it means we popped each value in the list and subtracted 1 from
            # remaining elements successfully. Hence we should have an empty list with all degrees removed
            return True

    # If the return value in the while loop is not reached then it means we got a negative value in the degree while
    # iterating, hence the sequence is not graphical
    return False
