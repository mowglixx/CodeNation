from .textutils import typewriter

def maths_puzzle():
    typewriter("Multiply 9 by 4.\n ")
    if input('\n') == "36":
        # q2
        typewriter("\nDivide 150 by 6.")
        if input('\n') == "25":
            typewriter("\nWhat is 57 Divided by 3?")
            # q3
            if input('\n') == "19":
                typewriter("\nSo, the secret code is 362519. Punch it in to the keypad!")
                if input('\n') == "362519":
                    return True
    typewriter("\nYou suck.")
    return False
