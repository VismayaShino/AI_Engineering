"""names = ("Meredith", "Emily", "Meredith")
print(type(names))
print(names.index('Meredith'))
print(names.count('Meredith'))"""

"""movies = []
mov1 = input("Enter first movie name:")
mov2 = input("Enter second movie name:")
mov3 = input("Enter third movie name:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)"""

palindrome = [1,2,3,2,1]
copy_pal = palindrome.copy()
copy_pal.reverse()

if (copy_pal == palindrome):
    print("given list is a palindrome")
else:
    print("given list is not a palindrome")


"""c d a a b b a"""
grades = []
grades.append("C")
grades.append("D")
grades.append("A")
grades.append("A")
grades.append("B")
grades.append("B")
grades.append("A")

grades.sort()
print(grades)
