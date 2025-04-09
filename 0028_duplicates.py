def return_dups(an_iterable):
    dups = []
    a_set = set()
    for item in an_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    print(f"This is our set with out duplicates {a_set}")
    print(f"This is our list with duplicates {dups}")


a_list = ["Susan Adams",
          "Kwame Goodall",
          "Jill Hampton",
          "Susan Adams", "Vladimir Putin", "Karl Marks", "Vladimir Putin"]

return_dups(a_list)
