import random

cMai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cMIN = "abcdefghijklmnopqrstuvwxyz"
num = "12345679890"

criar = cMai + cMIN + num
digitos = 16

senha1 = "".join(random.sample(criar,digitos))
print('sua senha é: '+ senha1)