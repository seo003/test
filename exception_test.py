# exception_test.py

while True:
    try:
        data1 = int(input("정수:"))
        data2 = 10 / data1
        data3 = [1,2,3]
        print(data3[-1])
    except ValueError:
        print("정수 좀 넣어! XXX")
    except ZeroDivisionError:
        print("0 좀 넣지 말라고!")
    except Exception as e: #exception의 값(오류정보)을 e에 저장
        #except: 와 동일-> exception은 모든 에러의 조상->제일 윗대가리
        print(e) #-> e의 에러 종류를 알 수 있음
    finally: #항상 실행
        print("안녕히 계세요 여러분~! 저는 이 세상의 모든 굴레와 속박을 벗어 던지고 제 행복을 찾아 떠납니다~ 여러분도~ 행복하세요~~!!")



try: #try는 단독으로 쓸 수 없음 -> except 등 함께 써야 함
    filename="c:/test/abc.txt" #c드라이브에 test파일 안에 abc.txt
    f = open(filename, "r")
    #open:파일관련함수->읽기용도로 파일 열기->파일 열리면 f에 저장? 뭔소리야
    print("file open:",filename)
    f.close()
except: #3~6이 실행되면 except 실행 X, 3~6에서 에러가나면 except 실행 o
    print("file open error:", filename)