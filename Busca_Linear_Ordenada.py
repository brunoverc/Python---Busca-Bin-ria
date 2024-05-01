def ordered_sequential_search(list, searchedValue):
    index = 0
    while index < len(list):
        if(list[index] == searchedValue):
            return f"{searchedValue} encontrado na posição {index}"
        else:
            if(list[index] > searchedValue):
               return f"{searchedValue} Não presente na lista"
            else:
                index = index + 1