# Demo of some relaxations of Python syntax achieved via preprocessing
# 1) forever loop now supported (=== while True)
# 2) until loop now supported (=== while not)
# 3) colons are optional after if/elif/else/while/for/def/class statements
#    as well as the new forever/until statements

a = 2
if a == 1
    forever
        print("hello")
elif a==2
 until a > 4
   print(a)
   a = a + 1
else
      print(GREEN + "nothing to do!" + RESET)
      
      
b = 1
if b == 1
 print(BLUE + "nothing to do!" + RESET)      
elif b==2
       forever
        print("hello")
else        
    until b == 0
            print(b)
            b = b - 1

c = 20
forever
   print(c)
   c = c + 2
   if c > 30
      break

print("All done!")