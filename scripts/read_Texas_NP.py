import csv
with open("TDNP.txt") as f:
    read = f.read()
    input = ""
    for i in read:
        count = 0
        i = i.strip('\n') #在这里先把换行符和空格去掉，免得错误太多
        i = i.strip(' ')
        i = i.strip('"')
        input = input + i


def read(input): #the function is used for reading the dataset as text and clean it (去掉其中的括号以便于之后的进一步读取）
    Final_output = []
    output = []
    word = ""
    count = 0
    for item in input:
        if item == '{':
            count = count + 1

        if item == '}':
            count = count - 1
            if count == 0:
                output.append(word)
                word = ""
                Final_output.append(output)
                output = []

        if count > 0:
            if item != ":" and item != "," :
                word = word + item
            else:
                output.append(word)
                word = ""

    return Final_output

output = read(input)

data = []
countyresult = {}
for county in output:
    countyresult['field'] = county[1] #exmaple for country result: {'field': 'str_location_county', 'county_name': 'AndrewsCounty', 'state': 'TX', 'count': '10', 'pivot': [['field', 'untl_decade', 'value', '1900-1909', 'count', '10']]}
    countyresult['county_name'] = county[3]
    countyresult['state'] = county[4]
    countyresult['count'] = county[6]
    countyresult['pivot'] = []
    is_pivot = 0
    count = 0
    pivot_item = []
    for line in county:


        if is_pivot == 1:
            this = ""
            for i in line:
                if i != "[" and i != "]" and i != "{" and i != "}":
                    this = this + i
            pivot_item.append(this)
            count = count + 1

        if line == "pivot":
            is_pivot = 1

        if count == 6: #6是因为每一组pivot里面其实只包含6个值，field,value,count三个变量和对应的数值
            count = 0
            countyresult['pivot'].append(pivot_item)
            pivot_item = []
    data.append(countyresult)
    print (countyresult)
    countyresult = {}

#print(data[0])
#print(data[1])


f = open('texas_np.csv','w', newline= "", encoding="utf-8")
csv_writer = csv.writer(f)
csv_writer.writerow(['field','county','state','subfeild','year','count'])
for i in data:
    for j in i['pivot']:
        csv_writer.writerow([i['field'],i['county_name'],i['state'],j[1],j[3],j[5]])

f.close()


#print(data[0]['pivot'][2])


