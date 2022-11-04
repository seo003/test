# main5.py
import mod2 as m
from mod2 import Math
from mod2 import add

print(m.PI, m.add(1,2), add(1,2))

a=Math() #math생성자 호출
b=list([1,2,3]) #클래스->리스트 생성자로 [1,2,3]리스트 생성
c=dict() #클래스
d=int(1) #클래스 -> int생성자로 1 생성

print(a.solv(2))
print(b.pop(-1)) #리스트만을 불러오는 메소드
print(c.get(1,"없다"))
