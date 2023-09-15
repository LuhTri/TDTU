# Luu Huu Tri - 52200167

import numpy as np
A = np.random.randint(101, size=(10, 10))
B = np.random.randint(21, size=(2, 10))
C = np.random.randint(21, size=(10, 2))


print("A = \n", A)
print("\nB = \n", B)
print("\nC = \n", C)
print("\n--- --- --- --- --- --- --- --- --- ---\n")

# a.
sum_1a = A + A.T + C@B + (B.T)@(C.T)
print("\na). A + A.T + C@B + (B.T)@(C.T) = \n", sum_1a)


# b.
sum_A = 0
for i in range(1, 11):
    temp = np.copy(A/(9 + i))
    for j in range(1, i):
        temp = temp @ A/(9 + i)
    sum_A += temp
print("\nb). A/10 + (A/11)**2 + (A/12)**3 + ... + (A/18)**9 + (A/19)**10 =\n", sum_A)


# c.
odd_rows = A[0::2]
print("\nc). The odd rows matrix of the matrix A: \n", odd_rows)


# d.
odd_int = A[A % 2 != 0]
print("\nd). The odd integer numbers vector: \n", odd_int)

# e.
# Ham kiem tra mot so nguyen co phai so nguyen to hay khong
def isPrimeNumber(n):
    if n < 2:
        return False

    for i in range(2, int(n/2) + 1):
        if (n % i == 0):
            return False
    return True


prime_nums = []
for K in A:
    for i in K:
        if isPrimeNumber(i):
            prime_nums.append(i)
prime_nums = np.array(prime_nums)
print("\ne). The prime numbers vector: \n", prime_nums)


# f.
D = C@B
print("\nf). Matrix D = C * B: \n", D)

for i in range(0, len(D)):
    if (i % 2 == 0):
        D[i] = np.flip(D[i])
print("\nReverse element in the odd rows of the matrix D = C@B: \n", D)


# g.
count_prime = []  # Luu so luong so nguyen to cua tung hang
max_count = 0  # Luu gia tri lon nhat trong count_prime

for K in A:
    count = 0  # Dung de dem cac so nguyen to trong hang
    for i in K:
        if isPrimeNumber(i):
            count += 1
    if max_count < count:
        max_count = count
    count_prime.append(count)

# In cac dong co count so nguyen to lon nhat
if max_count > 0:
    print("\ng). Rows have maximum count of prime numbers: ")
    for i in range(0, len(A[0])):
        if count_prime[i] == max_count:
            print(A[i])
else:
    print("\ng). The matrix A has no prime number")


# h.
# Ham tra ve do dai cua chuoi le lien tuc trong tung hang
def odd_sequence_len(A):
    length = 0
    max_length = 0

    for i in A:
        if (i % 2 != 0):
            length += 1
            if max_length < length:
                max_length = length
        else:
            length = 0

    return max_length


max_odd_len = 0  # Luu do dai lon nhat cua chuoi le

for K in A:
    if max_odd_len < odd_sequence_len(K):
        max_odd_len = odd_sequence_len(K)

# In cac dong co chuoi le lien tuc dai nhat
if max_odd_len != 0:
    print("\nh). Rows have longest contiguous odd numbers sequence: ")
    for K in A:
        if odd_sequence_len(K) == max_odd_len:
            print(K)
else:
    print("\nh). The matrix A has no odd numbers")