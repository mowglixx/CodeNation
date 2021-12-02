def missing_word_puzzle():
    q1 = input("Okay, first of all... Last Christmas, I gave you my... ")

    if q1.lower() == "heart":
        q2 = input(
            "Very good! How about... But tonight, thank God it's them instead of... ")
        if q2.lower() == "you":
            q3 = input(
                "Nicely done. One more... Snow is falling all around me, children playing, having... ")
            if q3.lower() == "fun":
                return True
    print("You suck.")
    return False
