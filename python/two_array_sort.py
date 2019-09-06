number = [5,2,3,4,1]
alphabet = ["a","b","c","d","e"]

set = zip(number,alphabet)

sorted_set = sorted(set)

for num, alph in sorted_set:
    print(num, alph)
