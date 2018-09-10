# put your code here.
tst = open("test.txt")

def word_counter(tst):

    word_dict = {}

    for line in tst:
        line.rstrip()
        new_line = line.split()
        
        for word in new_line:

            word_dict[word] = word_dict.get(word,0) + 1
        
    return word_dict


    #print(each_word)

print(word_counter(tst))
