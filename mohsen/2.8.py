#اكتب برنامج يحتوي على قاموس لأقسام شركة حيث يحتوي كل قسم على قاموس يمثل الموظفين ورواتبهم ويستخرج اسم القسم الذي يحتوي على أعلى راتب في الشركة
maran={
    "IT":{"ahmed":150000,"ali":135000},
    "Cyber Security":{"Maran":1000000,"sam":900000},
    "Secretary":{"taha":90000,"badr":100000}
}
x=''
sal=0
for k,v in maran.items():
   for k2,v2 in v.items():
      if v2>sal:
         x=k
         sal=v2
print(f"{x} : {sal}")