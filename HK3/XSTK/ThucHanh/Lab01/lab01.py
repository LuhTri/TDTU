# 52200167_LuuHuuTri
import itertools

# Cau1
def num_3_digits():
    print("Cau 1:")
    A = {1, 2, 3, 4, 5}
    k = 3
    n = len(A)

    num_3_digits = list(itertools.permutations(A, k))
    num_length = len(num_3_digits)

    print("%i permutations of %s:" % (k, A))
    for i in num_3_digits:
        print(i)

    print("Num_length is: %i!/(%i - %i)! = " % (n, n, k), num_length)


def cross(A, B):
    return {a + b for a in A for b in B}


# Cau 2
def randomly_draw():
    print("Cau 2:")
    urn = cross("W", "12345678") | cross(
        "B", "123456") | cross("R", "123456789")

    # a
    print("a/. ")
    U3 = list(itertools.combinations(urn, 3))
    len_U3 = len(U3)

    print("%i combinations of %s:" % (3, urn))
    for i in U3:
        print(i)
    print("Len of U3 combinations:", len_U3)

    # b
    print("b/.")
    for i in U3:
        if i[0][0] != i[1][0] and i[0][0] != i[2][0] and i[1][0] != i[2][0]:
            print(i)

    # c
    print("c/.")
    for i in U3:
        if i[0][0] == "W" and i[1][0] == "R":
            print(i)



def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


# Cau 3
def book_arrangement():
    print("Cau 3:")
    U_math = cross("M", "1234")
    U_phy = cross("P", "123")
    U_chem = cross("C", "12")
    U_lang = {"L1"}

    math_arrange = list(itertools.permutations(U_math))
    phy_arrange = list(itertools.permutations(U_phy))
    chem_arrange = list(itertools.permutations(U_chem))

    count = 0
    for a in math_arrange:
        for b in phy_arrange:
            for c in chem_arrange:
                B = a, b, c, tuple(U_lang)
                urn = list(itertools.permutations(B, 4))
                for i in urn:
                    print(i)
                    count += 1
    print("Numbers of book arrangement: ", count)


# Cau 4
def select_a_group():
    print("Cau 4:")
    U_men = cross("M", "12346")
    U_women = cross("W", "123456789")

    men_per = list(itertools.permutations(U_men, 3))
    women_per = list(itertools.permutations(U_women, 2))

    count = 0
    for m in men_per:
        for w in women_per:
            per = m, w
            urn = list(itertools.permutations(per, 2))
            for i in urn:
                print(i)
                count += 1
    print("Numbers of selection:", count)


# Cau 5
def poker_hand():
    print("Cau 5:")

    deck = cross("12345678910JQK", "SCDH")

    print("a/.")
    poker_5 = list(itertools.combinations(deck, 5))
    len_poker_5 = len(poker_5)
    print("Numbers of possible 5 cards poker is:", len_poker_5)

    # b
    print("b/.")

    def check_three_of_a_kind(poker):
        denomination = [i[0] for i in poker]
        for i in denomination:
            if (denomination.count(i) == 3):
                return True
        return False

    three_of_a_kind = []
    for poker_hand in poker_5:
        if (check_three_of_a_kind(poker_hand)):
            three_of_a_kind.append(poker_hand)

    len_three_of_a_kind = len(three_of_a_kind)
    print("Numbers of 'three of a kind' is:", len_three_of_a_kind)


# Cau 1
num_3_digits()

# Cau 2
randomly_draw()

# Cau 3
book_arrangement()

# Cau 4
select_a_group()

# Cau
poker_hand()
