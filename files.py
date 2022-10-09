var = input('Write something:')
# a - это запись новых данных в файлв и помещение их в конец файла
fa = open('Doc/file.txt', 'a', encoding='utf-8')  # encoding='utf-8' для записи русского текста
fa.write(f'{var}\n')
fa.close()

# w - запись новых данных, но с удалением старых данных
fw = open('Doc/file2.txt', 'w')
fw.write(f'{var}\n')
fw.close()

# r - считывание текста из файла
fr = open('Doc/file2.txt', 'r')
text = fr.read()
fr.close()
print(text)

# r+ - для чтения и записи
var1 = input('Write something:')
fr = open('Doc/file.txt', 'r+')
text = fr.read()
fr.write(f'{var1}\n')
fr.close()
print(text)
