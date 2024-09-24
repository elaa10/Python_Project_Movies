def quickSort(list, key=None, reverse=False):
    """
    Ordoneaza lista folosind metoda quick sort (folosim list comprehension)
    :return: lista ordonata
    :rtype: list
    """
    if len(list) <= 1:
        return list
    pivot = list.pop()
    lesser = [x for x in list if (key(x) if key else x) <= (key(pivot) if key else pivot)]
    greater = [x for x in list if (key(x) if key else x) > (key(pivot) if key else pivot)]

    # lesser = [x for x in list if key(x) <= key(pivot) if key else x <= pivot)] dar mie imi apare eroare la aceasta scriere


    if reverse:
        return quickSort(greater, key=key, reverse=True) + [pivot] + quickSort(lesser, key=key, reverse=True)
    else:
        return quickSort(lesser, key=key) + [pivot] + quickSort(greater, key=key)


#print(quickSort([3, 4, 6, -1, 5, 1, -9], key=lambda item: item ))


def gnome_sort(list, key=None, reverse=False):

    index = 0
    while index < len(list):
        if key:
            #Comparam elemntele folosind key
            if index == 0 or key(list[index]) >= key(list[index-1]):
                index += 1
            else:
                list[index], list[index-1] = list[index-1], list[index]
                index -=1
        else:
            #Comparam elementele simplu, daca nu avem key
            if index == 0 or  list[index] >= list[index-1]:
                index +=1
            else:
                list[index], list[index-1] = list[index-1], list[index]
                index -=1

    if reverse:
        return list[::-1]
    return list

print(gnome_sort([3, 4, 6, -1, 5, 1, -9], key=lambda item: item, reverse=True))
