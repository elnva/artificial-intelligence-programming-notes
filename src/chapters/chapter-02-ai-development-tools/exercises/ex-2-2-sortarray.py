def quicksort_improved(xl):
    if len(xl) <= 1:
        return xl

    pivot = xl[0]
    less = []
    greater = []

    # We only loop through the list ONE time now
    for x in xl[1:]:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort_improved(less) + [pivot] + quicksort_improved(greater)

def quicksort(xl):
    # BASE CASE: If the list has 0 or 1 element, it is already sorted.
    # This stops the recursion from running infinitely.
    if len(xl) <= 1:
        return xl
    else:
        # PIVOT SELECTION: Choose the first element in the list as the pivot point.
        pivot = xl[0]

        # PARTITIONING (Less Than): Iterate through the rest of the list (xl[1:])
        # and keep only the numbers that are strictly smaller than the pivot.
        less = [x for x in xl[1:] if x < pivot]

        # PARTITIONING (Greater Than / Equal To): Iterate through the rest of the list
        # and keep the numbers that are greater than or equal to the pivot.
        greater = [x for x in xl[1:] if x >= pivot]

        # RECURSION & COMBINATION: Recursively sort the 'less' and 'greater' lists.
        # Then, concatenate the sorted 'less' list, the pivot itself (as a list),
        # and the sorted 'greater' list together in that exact order.
        return quicksort(less) + [pivot] + quicksort(greater)


# Define an unsorted list of numbers to test the function
data = [12, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the quicksort function on the data and store the returned sorted list in 't'
t = quicksort(data)

# Output the final sorted list to the console
print(t)