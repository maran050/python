#اكتب برنامج ينشاء قاموس يحتوي على اسماء موظفين ورواتبهم ثم يضيف موظف جديد مع راتبه ويطبع محتوى القاموس كاملاً بعد التعديل
emp={
    "maran":900000.0,
    "sam":880000.50,
    "yosef":830000.0,
    "ans":800000.,
    "amer":800000.,
    }
name=input("Enter new name: ")
sal=float(input("Enter the salary"))
emp[name]=sal
print(emp)