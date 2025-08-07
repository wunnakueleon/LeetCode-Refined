input_list = [0, 1, 2, 2, 3, 3, 90, 28, 19]
target_sum = 5


def two_sums(list_input, target):

    dict_num = {}
    index = 0
    two_sum_list = []

    for each_num in list_input:
        second_sum_num = target - each_num
        dict_num[each_num] = index
        if second_sum_num in dict_num:
            two_sum_list.append(second_sum_num)
            two_sum_list.append(each_num)
            return two_sum_list

        index += 1
    return "No value is found"




print(two_sums(target=target_sum, list_input=input_list))
