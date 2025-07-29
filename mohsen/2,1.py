#اكتب برنامج ينشاء قاموس يحتوي على اسماء طلاب كمفاتيح ودرجاتهم كقيم ثم يستقبل اسم الطالب ويطبع  درجته اذا وجد او يطبع رساله تفيد بعدم وجود
std={
    "maran":87.78,
    "sam":88.50,
    "yosef":83,
    "ans":80,
    "amer":80
    }
x=input("enetr your name :")
if std.get(x):
    print(std.get(x))
else:
    print('no name')