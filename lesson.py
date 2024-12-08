import random
try:
    f = open("test.txt",'r')
    f.write('23')
except Exception as e:
    print("", e)
finally: f.close()
print("nice")
