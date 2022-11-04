# mod1.py

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(__name__)
if __name__ == "__main__":
    #__ __가 있으면 본인의 모듈 이름을 자동적으로 갖게되는 특수변수
    # 파일이 시작파일인지 아닌지 알 수 있음
    print(add(10,4))