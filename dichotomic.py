



def dichotomic(input_list, val):
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        index = len(input_list)//2
        return (dichotomic(input_list[:index], val) or
                dichotomic(input_list[index:], val))


if __name__ == '__main__':
    sequenza = [1,2,3,4,5,6,7,8,9,10]
    print(dichotomic(sequenza, 2))
    print(dichotomic(sequenza, 11))