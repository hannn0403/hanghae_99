## 제목: 99클럽 코테 스터디 16일차 TIL + 오늘의 학습 키워드

- **오늘의 학습 키워드:** String

- **공부한 내용 본인의 언어로 정리하기:** 문제를 읽을 때에 제한 조건 및 문제의 조건을 먼저 명확하게 파악을 하고 문제 풀이에 들어가야 불필요한 시간 낭비를 줄일 수 있다.  
- **오늘의 회고**
  - **어떤 문제가 있었고, 나는 어떤 시도를 했는지:** 첫 시도는 s.split()을 활용하였는데, 이는 문제의 조건 중 공백이 연속으로 입력될 수 있다는 내용을 제대로 숙지하지 못했다.  
  - **어떻게 해결했는지:** 입력받은 s로부터 공백인지를 먼저 확인하고, 공백이 아니라면 첫 문자의 경우 숫자인지 알파벳인지에 따라서 별도로 코드를 작성하였고, 그 이후에는 알파벳만 올 수 있으므로 소문자로 만드는 과정을 거쳤다. 
  - **무엇을 새롭게 알았는지:**  해당 문제에서 s.title() 함수를 사용하면 바로 문제가 풀린다는 것을 알았다. 
  - **내일 학습할 것은 무엇인지**
 
  
필수 해시태그: #99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL

---
## 코드
```def solution(s):
    answer = ''
    shouldBeUpper = True 
    for i in range(len(s)): 
        # 공백문자인 경우에는 공백하나 추가하고 바로 
        if s[i] == ' ': 
            answer = answer +' '
            shouldBeUpper = True 
            continue 
        
        # 만약 첫 문자인 경우 
        # 숫자라면 바로 추가하고 소문자라면 
        else: 
            if shouldBeUpper: 
                if s[i].isdigit(): 
                    answer = answer + s[i]
                    shouldBeUpper = False 
                
                else: 
                    answer = answer + s[i].upper() 
                    shouldBeUpper = False 
            
            else: # 공백 이후에 첫 문자가 아닌 경우에는 알파벳만 올 수 있다. 따라서 isdigit()을 굳이 함으로써 체크를 할 필요가 없다.  
                answer = answer + s[i].lower() 
    
    return answer
