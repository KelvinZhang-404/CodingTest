import heapq


def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    salesDict = {}

    for sale in sales:
        if sale not in salesDict:
            salesDict[sale] = 1
        else:
            salesDict[sale] += 1

    salesList = salesDict.values()
    print(salesDict)
    print(salesList)

    # nthMin = (sorted(salesList))[n-1]  # O(n.logn)
    nthMin = heapq.nsmallest(n, salesDict)[-1]  # O(n)

    return [key for key, value in salesDict.items() if value == nthMin][0]


if __name__ == "__main__":
    print(nth_lowest_selling([4, 3, 1, 5, 3, 2, 5, 4, 5, 4, 5, 1, 3, 3, 3], 2))
