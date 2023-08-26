def remove_duplicates(sequence):
    none_duplicates = []
    [none_duplicates.append(i) for i in sequence if i not in none_duplicates]
    print(none_duplicates)        
    return none_duplicates

remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5])        