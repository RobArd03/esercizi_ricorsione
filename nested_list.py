

def count_leaf_nodes(input_list):
    if len(input_list) == 0:
        return 0
    else:
        counter = 0
        for element in input_list:
            if type( element ) is list:
                counter += count_leaf_nodes(element)
            else:
                counter += 1
        return counter


if __name__ == "__main__":
    names = ["Adam", ["Lisa", "Bart",["Rob", "Jack"]], "Paul"]
    print( count_leaf_nodes(names) )





