# put your code here.
tst = open("test.txt")

def word_counter(tst):

    word_dict = {}

    for line in tst:
        line.rstrip()
        new_line = line.split()

        for word in new_line:
            word_dict[word] = word_dict.get(word,0) + 1

    
    for word in word_dict.items():
        lst = (f'{word[0]} {word[1]}')
        print(lst)
    
    return word_dict        
      




print(word_counter(tst))

# How to remove punctuation to avoid duplicate words ?