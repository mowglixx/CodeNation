def maths_quiz():
    q1 = input("Multiply 9 by 4. ")

    if q1 == "36":
        q2 = input(
            "Divide 150 by 6. ")
        if q2 == "25":
            q3 = input(
                "Divide 57 by 3. ")
            if q3 == "19":
                q4 = input(
                    "So, the secret code is 362519. Punch it in to the keypad! ")
                if q4 == "362519":
                    return True
    print("You suck.")
    return False
