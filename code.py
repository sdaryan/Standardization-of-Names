#استانداردسازی اسامی

#"Standardization of Names"

name=[]

for i in range(0, 10):  
    name.append(input())

capitalized = [item.title() for item in name]

for i in capitalized:
    print(i)