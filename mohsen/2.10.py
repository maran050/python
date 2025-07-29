#اكتب برنامج يحتوي على قاموسين كل منهما يحتوي على منتجات واسعارها ثم ينشئ قاموس جديد يحتوي جميع المنتجات مع اسعارها واذا تكرر اسم المنتج في القاموسين يجمع السعرين معا ثم يطبع القاموس الجديد
pro ={
    "milk":250,
    "rany":300,
    "jous":200,
    "floor":350,
     "water":100,
}
pro1 ={
    "milk":500,
    "rany":300,
    "jous":200,
    "floor":350,
    "papsy":200,
    "kake":100,
}
maran=pro
x=0
for i in pro1:
    if i in maran:
         maran[i]+=pro1.get(i)
    else:
         maran[i] =pro1.get(i)
print(maran)