shopping_bag ={}

print("[구입]")

while True:
  item = input("상품명?")
  if (item == ''):
    break
  quantity = input("수량은?")
  print("장바구니에",item,quantity,"개가 담겼습니다.\n")
  shopping_bag[item] = quantity

print("장바구니 보기 :",shopping_bag,"\n")

print("[검색]")
finding_item = input("장바구니에서 확인하고자 하는 상품은?")
print(finding_item,"은(는)",shopping_bag[finding_item],"개 담겨 있습니다.")
