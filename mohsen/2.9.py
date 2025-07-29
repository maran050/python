#اكتب برنامج يطلب من المستخدم ادخال جملة نصية ثم ينشئ قاموس يكون فية كل حرف مفتاح وقيمة المفتاح هي عدد تكرار هذا الحرف مع تجاهل الفراغات في الجملة
text=input("Enter the text")
let={}
for i in text:
   if i in let:
      let[i] +=1
   else:
      let[i] =1
print(let)     
