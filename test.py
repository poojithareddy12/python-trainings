print("hello")
print("hi")

i = 0
for i in range(10) :
    print(i)
list1 = [1, 2, 3, 4]
print(list1)
list2 = [5, 6, 7, 8]
print(list2)

c = list1 + list2
print(c)

a = "string"
print(a)
b= 'string'
print(b)
c= """string"""
print (c)

list3 = [1, 'hi', 'false', (2, 3)]
x = type(list3[-2])
print (x)


def sayhi():
    """
    This function prints Hi
    """
    print("Hi")

sayhi()
