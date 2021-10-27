#TASK 1
import requests
import re

text_pull = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt')
text = str(text_pull.text.lower())
text = re.sub(r'[^\w]+',' ', text)
print(text.replace(' ', '\n'))
file = open(r"D:\moby_clean.txt", "w")
file.write(text.replace(' ', '\n'))
file.close()


#TASK 2
s = "D:\moby_clean.txt"
file = open(s)
lst = list((file.read().split('\n')))
d = dict.fromkeys(lst, 0)
for i in lst:
    d[i] += 1
print('The most frequent 5:')
for num, i in enumerate(sorted(d.items(), key=lambda x:(x[1]),reverse=True)):
    if num > 4:
        break
    print(f'{num+1}. {i[0]}')
print('The least frequent 5:')
for num, i in enumerate(sorted(d.items(), key=lambda x: (x[1]), reverse=False)):
    if num > 4:
         break
    print(f'{num + 1}. {i[0]}')

#TASK 3
file = open("D:\moby_clean.txt")
lst = list((file.read().split('\n')))
max = 1;
for i in lst:
    if len(i) > max:
        max=len(i)
print(max)
for i in lst:
    if len(i) == max:
        print(i)


#TASK 4
def count_range(filee, min, max):
    file = open(filee)
    lst = list(map(float, file.read().split()))
    count = 0
    for i in lst:
        if i < max and i > min:
            k += 1
    return k


