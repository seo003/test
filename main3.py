# main3.py
import mod1 as m #mod1를 m으로
from mod1 import add #mod1에서 add함수 사용
# from mod1 import add, sub
# from mod1 import *

def sub(a,b): #sub가 새로 한번 더 정의해줬기 때문에 위에 from mod import sub는 활성화되지 않음
    return b-a

print(add(1,2)) #mod1의 add사용
print(sub(1,3)) #새로 정의한 sub사용
print(m.sub(1,3)) #m의 sub사용(mod1의 sub사용)

