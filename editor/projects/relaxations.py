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
      
print("All done!")