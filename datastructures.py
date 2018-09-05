#Data structures
L = [1, 'X', [7, 8], (2, 3), False] #Creating list
T = (1,'X',(4,5),[8,9]) #Creating tuple
print(type(L))
print("List is {}".format(L))
print("Tuple is {}".format(T))

#for in for loop should start with small letter but not capital letter, otherwise syntax error
# and statement after for statement should have tab/space indentation
#Print statement with dynamic values printing
for i in range(0, len(L)) :
    print("The List element with index {} is - {} with type {}".format(i, L[i], type(L[i])))
for j in range(0,len(T)) :
    print("The tuple element with index {} is - {} with type {} ".format(j,L[j],type(L[j])))
print("Refering List element {}".format(L[0])) #Referring List element
print(L[-1])
print("Refering Tuple element {}".format(T[0])) #Refering Tuple element

print("Sliced list {}".format(L[1:3])) #Slicing List (need to use colon)
print(L[-1:-3])
L[0] = 8 #Reassigning List element
print(L)
del L[0], L[-1] #Deleting list elements
print(L)

T[3][0] = 2 # Tuple element reassignment (possible with only mutable element(list) inside tuple,
# not possible with any other immutable(tuple) element inside tuple
#Tuple reassignment/deletion is not possible with single elememt
print(T)

