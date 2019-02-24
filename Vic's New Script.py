for i in range(10):
 print(i)

 l = [4, 5, 6]
 for i in l:
     print(i)

     i = 8
     while i > 0:
         print(i)
         i = i - 1

         i = 8
         while True:
             if i <= 0:
                 break
             i = i - 1

             i = 8
             if i > 0:
                 print("i is greater than zero")
             else:
                 print("i is less than or equal to zero")

                 i = 8
                 if i > 0:
                     print("i is greater than zero")
                 elif i < 4:
                     print("i is between 0 and 4")
                 else:
                     print("i is greater than or equal to four")

i = 8
if i > 0:
    print("i is greater than zero")
elif i < 4\
        :
    print("i is between 0 and 4")
else:
    print("i is greater than or equal to four")


    def my_function():
        i = 8
        if i > 0:
            print("i is greater than zero")
        elif i < 4:
            print("i is between 0 and 4")
        else:
            print("i is greater than or equal to four")

            def add(a, b):
                return a + b
print(add(3, 9))
