bio_score = float(input("Enter your biology score: "))
chem_score = float(input("Enter your chemistry score: "))
physics_score = float(input("Enter your physics score: "))

if bio_score < 40:
    print("Fail")
elif chem_score < 40:
    print("Fail")
elif physics_score < 40:
    print("Fail")
else:

    score = (bio_score + chem_score + physics_score) / 3

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