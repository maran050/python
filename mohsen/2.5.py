#اكتب برنامج ينشئ قاموس يحتوي على معلومات شخص (الاسم والعمروالمدينة) ثم يحذف عنصر المدينه من القاموس ويطبع البيانات المتبقية
maran={
    "Name":"maran",
    "age":21,
    "City":"Taiz",
}
maran.popitem()
print(maran)
#   OR
#maran.pop("City")
#print(maran)