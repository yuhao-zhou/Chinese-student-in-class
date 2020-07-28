from wikiScrap import get_surname
from bs4 import BeautifulSoup

chinese_surname = get_surname()

with open("Subject Roster_ Database Systems & Information Modelling (INFO90002_2020_SM2).html", "r", encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

student_name = []
for tag in soup():
    if "data-student_id" in tag.attrs:
        name = tag.string[:-1] # name is just the text component
        student_name.append(name.split())

# if we want to add some extra (check from student surname)
chinese_surname.extend(["qi","you","xuan","xi","yong","weng","si","qu","quan","pu","miao","hui","jing","ji","geng","bian", "dou"])

chinese_number = 0
for name in student_name:
    if str.lower(name[-1]) in chinese_surname:
        chinese_number+=1

# 77% from the class have a Chinese surname!
print(chinese_number/len(student_name))
