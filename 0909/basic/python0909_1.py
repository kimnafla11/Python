#현재 5000원 사탕이 120원 최대한 살수있는 사탕 수 나머지 돈?
myMoney = 5000
candyPrice = 120
numCandies = myMoney//candyPrice
#몫만 구하는 연산자
change = myMoney % candyPrice
#change = 5000-numCandies*candyPrice (내가 작성한건데 ㅄ같은듯.)

print("살수있는 사탕 개수 = ",numCandies,"개")
print("거스름돈 = ",change,"원")
