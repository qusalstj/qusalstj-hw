def get_radius(prompt):
    r=int(input(prompt))
    return r
def get_circle_area(r):
    return r*r*3.14
prompt='넓이를 구하고자 하는 원의 반지름은?'
circle=get_radius(prompt)
print('반지름',circle,'인 원의 넓이 = 3.14 x',circle,'x',circle,'=',get_circle_area(circle))
