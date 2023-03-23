def exchange(price):
    s=price
    w500=s//500
    s%=500
    w100=s//100
    s%=100
    w50=s//50
    s%=50
    w10=s//10
    s%=10
    print('500원 동전의 개수:',w500)
    print('100원 동전의 개수:',w100)
    print('50원 동전의 개수:',w50)
    print('10원 동전의 개수:',w10)

def get_integer(prompt):
    res=int(input(prompt))
    return res

price=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(price)
