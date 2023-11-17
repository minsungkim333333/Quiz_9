class beverage:
    def __init__(self, name, price,number):
        self.name = name
        self.price= price
        self.number = number
    def calculate(self):
        result=self.price*self.number
        return print(str(result)+ '원 입니다.')
while True:
    selected_beverage=input('음료를 선택해주세요.(coffee, greentea, icetea)')
    n=int(input('개수를 입력해주세요.'))
    name_coffee=beverage('coffee', 3000,n)
    name_greentea=beverage('greentea', 2500,n)
    name_icetea=beverage('icetea', 3000,n)
    if selected_beverage == 'coffee':
        name_coffee.calculate()
    elif selected_beverage == 'greentea':
        name_greentea.calculate()
    elif selected_beverage == 'icetea':
        name_icetea.calculate()
    else:
        print('알맞은 정보를 입력해주세요.')
