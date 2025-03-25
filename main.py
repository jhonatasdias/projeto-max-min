def max_min_dc(arr, low, high):
    """
    Recursively finds the minimum and maximum elements in a subarray using the divide and conquer approach.

    :param arr: List of numbers to search.
    :type arr: list
    :param low: Starting index of the subarray.
    :type low: int
    :param high: Ending index of the subarray.
    :type high: int

    :return: A tuple (min, max) with the smallest and largest elements in the subarray.
    :rtype: tuple

    :notes:
        - Base case: If the subarray has only one element, returns it as both min and max.
        - Base case: If the subarray has two elements, returns them in sorted order.
        - Divide: If the subarray has more than two elements, it is split into two halves.
        - Conquer: The function is recursively called on both halves.
        - Combine: The final min and max are obtained by comparing results from both halves.
    """
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2
    min_esq, max_esq = max_min_dc(arr, low, mid)
    min_dir, max_dir = max_min_dc(arr, mid + 1, high)

    min_final = min(min_esq, min_dir)
    max_final = max(max_esq, max_dir)
    return min_final, max_final


def max_min_select(arr):
    """
    Finds the minimum and maximum elements in a list using the divide and conquer algorithm.

    :param arr: List of numbers to process. Must not be empty.
    :type arr: list

    :return: A tuple (min, max) with the smallest and largest elements in the list.
    :rtype: tuple

    :raises ValueError: If the input list is empty.
    """

    if not arr:
        raise ValueError("A lista não pode estar vazia.")
    return max_min_dc(arr, 0, len(arr) - 1)

# Exemplo de uso:
if __name__ == '__main__':
    sequencia = [7, 2, 9, 0, 4, 6, 3, 8, 1, 5]
    minimo, maximo = max_min_select(sequencia)
    print("Sequência:", sequencia)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)