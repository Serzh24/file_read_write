list_text = ['1.txt', '2.txt', '3.txt']
dict = {}
for el in list_text:
    with open(el, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count_lines = str(len(lines))
        dict[el] = int(count_lines)
print(dict)
sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
print(sorted_dict)

for element in sorted_dict:
    for el in element:
        if isinstance(el, str):
            with open(el, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                file_name = el
        else:
            count_str = str(el)
    with open('data.txt', "a") as file:
        file.write(file_name)
        file.write('\n')
        file.write(count_str)
        file.write('\n')
        for i in lines:
            file.write(i.strip() + '\n')
