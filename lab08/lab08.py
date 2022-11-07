import os
a = os.path.abspath(os.getcwd())
b = a.split("/")
del b[0]
print(b)
c = os.listdir("/home/e94111164")
print(c)

ran1 = len(b)
ran2 = len(c)

path = 'e94111164.txt'

lab08 = open(path, 'w')
for i in range (ran1):
    lab08.write(b[i]+os.linesep)
lab08.write(os.linesep)
for i in range (ran2):
    lab08.write(c[i]+os.linesep)
lab08.close()
f = open(path, 'r')
fi = f.readlines()
for line in fi:
  print(line.strip())
f.close()

