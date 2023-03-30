def price_A(a):
    print('A 상품의 정가는',get_fixed_price(sale,a),'원')
    
def price_B(b):
    print('B 상품의 정가는',get_fixed_price(sale,b),'원')

def get_fixed_price(P,R):   
    return int(R*100/(100-P))

sale=int(input('할인율은?'))
AA=int(input('A 상품의 할인된 가격은?'))
BB=int(input('B 상품의 할인된 가격은?'))

price_A(AA)
price_B(BB)

