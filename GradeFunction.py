score = int(input("Enter your score: "))

def grade():
    if score >= 70:
        print("1st")
    elif score >= 60:
        print("2.1")
    elif score >= 50:
        print("2.2")
    elif score >= 40:
        print("Pass")
    else:
        print("Fail")

    return score

grade()



