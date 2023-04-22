def print_gugudan():
    for i in range(2):
        for k in range(1,10):
            for j in range(2,6):
                print_gugudan_row(j+i*4,k,'\t')
            print()
        print()
                
def print_gugudan_row(dan,num,end):
    return print(f"{dan} x {num} = {end:2d}")
            
print_gugudan() 