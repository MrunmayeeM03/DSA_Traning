def SelectionSort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':

    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    print("Before Sorting:", arr)

    SelectionSort(arr)

    print("After Sorting:", arr)



