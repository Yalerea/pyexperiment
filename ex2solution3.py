def get_count(sentence):
    count = 0
    for str in sentence:
        if str =='a' or str == 'e' or str == 'i' or str == 'o' or str == 'u':
            count+=1
    return count