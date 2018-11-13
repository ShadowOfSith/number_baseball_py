dojeansoo=1
ball=0
strike=0
from random import *
randomgabs1=randrange(1,10)
randomgabs2=randrange(1,10)
randomgabs3=randrange(1,10)
while randomgabs1==randomgabs2:
	randomgabs2=randrange(1,10)
	while randomgabs2==randomgabs3:
		randomgabs3=randrange(1,10)
		while randomgabs1==randomgabs3:
			randomgabs3=randrange(1,10)
while randomgabs2==randomgabs3:
	randomgabs3=randrange(1,10)
	while randomgabs1==randomgabs3:
		randomgabs3=randrange(1,10)
		while randomgabs1==randomgabs2:
			randomgabs2=randrange(1,10)
while randomgabs1==randomgabs3:
	randomgabs3=randrange(1,10)
	while randomgabs2==randomgabs3:
		randomgabs3=randrange(1,10)
		while randomgabs1==randomgabs2:
			randomgabs2=randrange(1,10)
while strike<3:
	try:
		import math
		gabs=int(input('3자리 값을 입력하세요(게임나가기: 0을 3번 입력하세요.): '))
		if gabs==000:
			print('===========================================================================')
			samjin='취소.......'
			break
		gabs1=gabs%10
		gabs=math.floor(gabs/10)
		gabs2=gabs%10
		gabs=math.floor(gabs/10)
		gabs3=gabs%10
		print('===========================================================================')
		if gabs1>0:
			if randomgabs1==gabs1:
				strike+=1
			elif randomgabs1==gabs3:
				ball+=1
			elif randomgabs1==gabs2:
				ball+=1
		if gabs2>0:
			if randomgabs2==gabs2:
				strike+=1
			elif randomgabs2==gabs3:
				ball+=1
			elif randomgabs2==gabs1:
				ball+=1
		if gabs3>0:
			if randomgabs3==gabs3:
				strike+=1
			elif randomgabs3==gabs2:
				ball+=1
			elif randomgabs3==gabs1:
				ball+=1
		if strike<3:
			print('%d볼         |'%ball)
			print('%d스트라이크 |'%strike)
			print('===========================================================================')
		if strike==3:
			samjin='삼진아웃! %d번 도전 했습니다.'%dojeansoo
			break
		dojeansoo+=1
		ball=0
		strike=0
	except:
		print('숫자를 입력하세요!!!!!!!!!')
print(samjin)