def SEE1(word, phrase):
    x = phrase.split()

    num = x.count(word)

    return num

print(SEE1("hi", "Hi hi"))