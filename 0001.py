import random

squ='qwertyuiopasdfghjklzxcvbnml234S67890'

for i in range(200):
	codes = []
	for i in range(5):
		code = ''.join(random.sample(squ.upper(), 5))
		codes.append(code)
	print('-'.join(codes))