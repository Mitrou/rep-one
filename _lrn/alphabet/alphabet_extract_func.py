# alphabet importing
from variables import *


def alpha_query(test_str):
    # some variables
    tst_arr = []
    tst_arr_w = []
    w_str = ''
    counter = 0

    # building the alphabet indexes list from the test string given
    for i in test_str:
        test_index = alph_array.index(i)
        tst_arr.append(test_index)

    # generating strings of serial data and store them into tst_arr_w
    for i in tst_arr:
        if counter == len(tst_arr)-1 and len(w_str) != 0:       # handling last element in list
            w_str += str(alph_array[i])                         # ^
            tst_arr_w.append(w_str)                             # ^
        elif counter == len(tst_arr)-1 and len(w_str) == 0:     # ^
            tst_arr_w.append(str(alph_array[i]))                # ^
        elif i+1 == tst_arr[counter+1]:                         # if the next character is good
            w_str += str(alph_array[i])                         # just extending the string by alphabet character
        elif i+1 != tst_arr[counter + 1]:                       # if the next character is bad
            w_str += str(alph_array[i])                         # extending the string by alphabet character
            tst_arr_w.append(w_str)                             # extending the strings storage list
            w_str = ''                                          # NULLing the string
        else:
            print('Error!')
        counter += 1
    return max(tst_arr_w, key=len)                             # returning the final result


print(alpha_query('dddabcgggbcdefgaab'))
