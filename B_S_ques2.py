def find_target(Array, Target):
    left = 0
    right = len(Array) - 1
    while left <= right:
        mid = (left + right) // 2
        if Array[mid] == Target:
            return mid  # Return the index of the target if found
        elif Array[mid] < Target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if the target is not found

def count_occurrences(Array, Target):
    # Find any occurrence of the target using binary search
    mid = find_target(Array, Target)
    if mid == -1:
        return 0  # Target not found in the array
    
    count = 1  # Start with the occurrence at 'mid'
    left = mid - 1
    right = mid + 1

    # Count occurrences to the left
    while left >= 0 and Array[left] == Target:
        count += 1
        left -= 1

    # Count occurrences to the right
    while right < len(Array) and Array[right] == Target:
        count += 1
        right += 1

    return count

def main():
    Array = [2, 4, 4, 4, 6, 8]
    Target = 4
    print(f"Count of {Target}: {count_occurrences(Array, Target)}")

    Array2 = [1, 2, 3, 6, 8, 5]
    Target2 = 8
    print(f"Count of {Target2}: {count_occurrences(Array2, Target2)}")

main()
