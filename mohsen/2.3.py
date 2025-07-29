#اكتب برنامج ينشاء قاموس يحتوي على سلع وأسعارها ثم يحسب مجموع أسعار جميع السلع ويطبع الناتج
pro ={
    "milk":250,
    "rany":300,
    "jous":200,
    "floor":350,
}
sum=0
for k,v in pro.items():
    sum+=v
print(f"Total {sum}")