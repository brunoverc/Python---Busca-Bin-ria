def binary_search_iteration(list, searchedValue):
    fistIndex = 0
    size = len(list)
    lastIndex = size - 1
    middleElementIndex = (fistIndex + lastIndex) // 2
    midlleElement = list[middleElementIndex]
    
    searched = True
    while searched:
        if fistIndex == lastIndex:
            if midlleElement != searchedValue:
                searched = False
                return f"{searchedValue} Não presente na lista"
        elif midlleElement == searchedValue:
            return f"{midlleElement} encontrado na posição {middleElementIndex}"
        elif midlleElement > searchedValue:
            newPosition = middleElementIndex - 1
            lastIndex = newPosition
            middleElementIndex = (fistIndex + lastIndex) // 2
            midlleElement = list[middleElementIndex]
            if midlleElement == searchedValue:
                return f"{midlleElement} encontrado na posição {middleElementIndex}"
        elif midlleElement < searchedValue:
            newPosition = middleElementIndex + 1
            fistIndex = newPosition
            lastIndex = size - 1
            middleElementIndex = (fistIndex + lastIndex) // 2
            midlleElement = list[middleElementIndex]
            if midlleElement == searchedValue:
                return f"{midlleElement} encontrado na posição {middleElementIndex}"
