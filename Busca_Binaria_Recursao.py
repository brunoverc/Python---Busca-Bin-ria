def binary_search_recursion(list, firstIndex, lastIndex, searchedValue):
    if(lastIndex >= firstIndex):
        middleElementIndex = (firstIndex + lastIndex) // 2
        middleElement = list[middleElementIndex]

        if(middleElement == searchedValue):
            return f"'{middleElement}' encontrado na posição {middleElementIndex}"
        elif (middleElement > searchedValue):
            newPosition = middleElementIndex - 1
            #novo último índice é a nova posição
            return binary_search_recursion(list, firstIndex, newPosition, searchedValue)
        elif (middleElement < searchedValue):
            newPosition = middleElementIndex + 1
            #novo primeiro índice é a nova posição
            return binary_search_recursion(list, newPosition, lastIndex, searchedValue)
    else:
        return f"'{searchedValue}' Não presente na lista"

