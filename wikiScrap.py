from bs4 import BeautifulSoup
import re

def get_surname():
    with open("List of common Chinese surnames - Wikipedia.html", "r", encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    surname_list = []


    # l = soup.find_all(title=re.compile(r'\(surname\)'))
    # for tag in l:
    #     surname_list.append(tag.get("title").split()[0])
    #
    # surname_list.sort()
    # print(surname_list)

    table_body = soup.find_all("table",class_= "wikitable sortable jquery-tablesorter")[0]  # there is only one table tag os this class
    table_t_body = table_body("tbody")[0] # there is only one tbody tag below. This is the root we tend to work on

    # The difficulty here is table cell are not labelled with either row number or column number
    # we want to select the column with pinyin (and use its attribute), but we can only check number of column passed to acheived this
    # we want to select every row, but sometimes multiple row belongs to the same surname. We need to use row span given by the table to check it.

    table_row = table_t_body.find_all("tr") # get all rows
    for row in table_row:
        columns = row.find_all("td")
        column_0 = columns[0]  # the first column must contain an integer to be valid. (otherwise is sub row)
        # index = column_0.string
        # if index and str.isdigit(index[:-1]): # if the index is not null, and eliminated the \n returns an integer, row is valid

        if column_0.get("rowspan"): # if the row span is set, its likely a multi row that contains a new surname
            pinyin_index = 3 # if first column span 1, then pinyin at 3.
            column_1= columns[1] # This is the first column. It might  span 2 (to have only 1 chinese character), this pull pinyin to column 2
            if column_1.get("colspan") == "2":
                pinyin_index = 2
            pinyin_column = columns[pinyin_index] # get the pinyin column

            if pinyin_column():
                surname = str(pinyin_column()[0].get("title").split()[0])
            else:
                surname = str(pinyin_column.string[:-1])  # there is also this low chance, no hyper link of surname. plain text in column
            surname_list.append(surname)


    # convert pinyin to unicode
    clean_surname = []
    for s in surname_list:
        s = s.replace("ò", "o")
        s = s.replace("á", "a").replace("ā","a")
        s = s.replace("ǐ", "i")
        s = s.replace("ě", "e")
        s = s.replace("ǔ", "u").replace("ú", "u").replace("ū","u")
        clean_surname.append(str.lower(s))

    return clean_surname

# print((get_surname()))
#
# print(sorted(get_surname()))
