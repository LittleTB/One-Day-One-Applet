import random

squ='qwertyuiopasdfghjklzxcvbnml234S67890'

for i in range(200):
	codes = []
	for i in range(5):
		code = ''.join(random.sample(squ.upper(), 5)) # 从squ字符串中随机取5个字符组成字符串
		codes.append(code)
	print('-'.join(codes))