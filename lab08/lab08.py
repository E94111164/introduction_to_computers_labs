import os
#�����|�����r��
a = os.path.abspath(os.getcwd())
#�N���split���}��list
b = a.split("/")
#��@�}�l���Ů�delete��
del b[0]
#��Xlist
print(b)
#Ū�� ��/home/�Ǹ��� �ؿ��U�Ҧ��ɮשM��Ƨ�
c = os.listdir("/home/e94111164")
print(c)

#���o���C����
ran1 = len(b)
ran2 = len(c)

path = 'e94111164.txt'

#�}�ɡB�g��
lab08 = open(path, 'w')
#��for�j��@��@��g�J
for i in range (ran1):
    lab08.write(b[i]+os.linesep)
#��linesep����
lab08.write(os.linesep)
#��for�j��@��@��g�J
for i in range (ran2):
    lab08.write(c[i]+os.linesep)
#�����ɮ�
lab08.close()
#Ū��
f = open(path, 'r')
fi = f.readlines()
#�@��@��Ū�ɨÿ�X
for line in fi:
  print(line.strip())
#�����ɮ�
f.close()

