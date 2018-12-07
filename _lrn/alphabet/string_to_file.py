
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
fle_path = r"D:\myGit\rep-one\_lrn\alphabet\Files\array_alphabet.txt"
alph_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# with open("Output.txt", "w") as text_file:
#     print("Purchase Amount: {}".format(test), file=text_file)

f = "'" + alphabet.replace(" ", "', '") + "'"
print(f)
s = open(fle_path, 'w')
s.write(f)
s.close()
