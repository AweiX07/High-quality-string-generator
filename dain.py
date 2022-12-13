# coding=utf-8
#random的极致运用
#适用于Windows系统


import time
import os
import random

os.system('title 高质量字符串生成器')
os.system('color 7')
print('\033[35m高质量字符串生成器\033[0m','\n','\033[30m作者：AweiX07\033[0m')
print('\n','\033[33m#'*10,'\n','\n',"\033[31m友情提示：如果运行时出现乱码，请尝试使用Thonny或其他方式运行。若仍然无法解决乱码问题，请运行该程序的稳定版本！\nThonny官网：thonny.org\n作者邮箱：AweiX07@163.com\033[0m",'\n')
print('\033[33m#'*10,'\n')
time.sleep(0.475)
print('\n','\033[33m正在启动,请稍等\033[0m')
for i in range(100):
    print('\033[32m',"="*(i//10), i, "%\r", end = '\033[0m')
    time.sleep(0.01)
time.sleep(0.2)
i=i+1
print('\033[32m',"="*(i//10),i,'%',end = '\033[0m')
time.sleep(1)

fir=random.randint(0,1)+random.randint(1,2)+random.randint(2,3)
st=random.randint(3,4)+random.randint(4,5)
first=fir+st
f=['`','~','!','@','#','$','%','^','&','*','(',')','_','+','|','?','.','/','*','-','+']
body=str(random.random())+random.choice(f)*int(random.randint(1,10))+random.choice(f)*int(random.randint(0,12))
strs=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','&','^','%','@','#']
Words=['3315','AweiX07','AweiXFUCK','xcfhjdfhj','awrhiwey','AKLSsdjyuSSYHJ','djcefhskl','LZHSDYCBSZJSBSJA']
last=random.choice(strs)*3+random.choice(strs)*2+random.choice(Words)*int(random.randint(1,2))+random.choice(Words)*2+random.choice(Words)*2+str(random.random()*int(random.randint(3,9))+int(random.randint(0,666)))
passwd=str(first)+body+last

print('')
print('\n\033[36m为您生成的高质量字符串：\033[0m\n')
print('\033[34m',passwd)
time.sleep(0.15)
print('\033[0m','\n\n\033[33m制作不易，请笑纳:)\033[0m\n')
time.sleep(1)
os.system('pause')

