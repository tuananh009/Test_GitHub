#thêm thư viện decimal vào py
from decimal import*
#chữ số thập phân sau dấu chấm
getcontext().prec = 100
f = Decimal(10)/3
print(f)
