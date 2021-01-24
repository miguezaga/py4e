def count (word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return(count)

a_in_banana = count("banana", "a")
print(a_in_banana)
