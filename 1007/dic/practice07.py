#사용자가 지정하는 파일을 읽어 파일에 저장된 각각의 단어가 몇번 나오는지 계산하는 프로그램

def process(w):
    output =""
    for ch in w:
         if(ch.isalpha()):#알파벳을 검증
                output+=ch#알파벳이면 output에 저장
    return output.lower()#output을 소문자로 바꾸기
words = {}#딕셔너리 하나 만듦


fileName = input(("파일 명을 입력하세요 : "))#파일명을 받음
file = open(fileName,'r')#읽기 전용으로 파일 엶
for line in file: 
    linewords = line.split() #공백으로 단어 분리후 리스트 저장
    for word in linewords: #파일의 모든 줄에 대하여 반복
       word = process(word) #word를 process함수를 이용하여 알파벳 소문자로 넣음
       if word in words: #word가 words딕셔너리에 이미 존재하면,
            words[word] +=1 #value값 +1함
       else:
            words[word] =1
            
print("파일 이름 : ", fileName)
print(words)
