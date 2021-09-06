#会员购物金额>=200,八折;大于100，九折；小于100，不打折
#非会员购物金额大于等于200，九五折；小于200，不打折

answer = input('您是会员吗？')
if answer == '是':
    amount = float(input('请输入购物金额：'))
    if amount >= 200:
        print('可以打八折，付款金额为：', amount*0.8)
    elif (amount < 200) and (amount >= 100):
        print('可以打九折，付款金额为：', amount*0.9)
    else:
        print('不打折')
else:
    amount=int(float(input('请输入购物金额：')))
    if amount >= 200:
        print('可以打九五折，付款金额为：', amount*0.95)
    else:
        print('不打折')


