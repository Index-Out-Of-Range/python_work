# from docx import Document
#
#
# document = Document('参考答案.docx')
#
# for paragraph in document.paragraphs:
#     print(paragraph.text)
#
# tables = document.tables
#
# for table in tables:
#     for i in range(len(table.rows)):
#         if i % 2 == 1:
#             for j in range(len(table.columns)):
#                 print(table.cell(i, j).text, end=', ')
#         print()
#
# document.add_paragraph(u'第一段',style=None)
#
# document.save(r'D:\pycharm\python_work\dp3\answer.docx')

# article = 'Youth comes only once in a lifetime, therefore, it is important ' \
#           'that we should not waste those years in idleness and bad living.' \
#           'This is also the time when our memories are best.We are able to ' \
#           'learn more during this time than when we become older. ' \
#           'During our younger years, we have the enthusiasm to set high goals ' \
#           'for ourselves. We also try to overcome obstacles which are placed in our way.' \
#           'If we realize how precious youth is, ' \
#           'we will be fulfilled when we are young as well as ' \
#           'when we are older. If we waste our youth, ' \
#           'we will spend the rest of our lives wishing we could be young again.'
#
# word_list = len(article.split())
# print(word_list)


# import xlrd
# import xlwt
# from xlutils.copy import copy
#
# excel = xlrd.open_workbook('成绩单.xls')
# table = excel.sheets()[0]
#
# wb = copy(excel)
# ws = wb.get_sheet(0)
# print(table.cell_value(1, 2))
# ws.write(1, 2, 69)
# wb.save('成绩单.xls')
# print(table.cell_value(1, 2))
#
# print(table.nrows)
#
# for row in range(table.nrows):
#     print(row)

import difflib

sentence = 'I used to be a criminal but now I want to be a good man.'
stu = 'I used to be a bad men but now I have to be a good man.'
print(difflib.SequenceMatcher(None,sentence,stu).ratio())

