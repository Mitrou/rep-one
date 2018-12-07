# pre built alphabet characters array
alph_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# string to be tested
test_str = 'dddabcgggbcdefgaab'

# some variables
tst_arr = []
tst_arr_w = []
test_index = 0
w_str = ''
counter = 0

# building the alphabet indexes list from the test string given
for i in test_str:
    test_index = alph_array.index(i)
    tst_arr.append(test_index)

# middle list of alphabet indexes
# print(tst_arr)                                              # [3, 3, 3, 0, 1, 2, 6, 6, 6, 1, 2, 3, 4, 5, 6, 0, 0, 0]

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
#    print(tst_arr_w)                                        # middle list for each cycle iteration
    counter += 1

# printing the final result
print(max(tst_arr_w, key=len))
