def print_coin(coin,charge):
    count=charge//coin
    print(str(coin)+"원 동전의 개수:",count)
    return charge%coin

def exchange(price):
    s=price
    price = print_coin(500,price)
    price = print_coin(100,price)
    price = print_coin(50,price)
    print_coin(10,price)
    
def get_integer(prompt):
    res=int(input(prompt))
    return res

price=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(price)