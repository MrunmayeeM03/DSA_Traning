def insertionSort(arr):

    for i in range(1, len(arr)):

        current = arr[i]
        pos = i

        while pos > 0 and current < arr[pos - 1]:

            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = current

        print(arr)

    return arr


if __name__ == "__main__":

    arr = [5, 2, 17, 3, 4, 9, 15, 1]

    print("Before Sorting:", arr)

    insertionSort(arr)

    print("After Sorting:", arr)