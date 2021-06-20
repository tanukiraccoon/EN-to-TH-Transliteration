from word_alignment import alignment_en as en #import ตัวตัดคำภาษาอังกฤษ

def str2lst(string): 
    li = list(string.split(" "))
    return li 

def reverseChar(words):
    char = words
    char.remove('<EOS>')
    print(char)
#     char = str2lst(char)
    length = len(char)
    for i in range(length):
        if(char[i]) in {'เ.','แ.','ไ.','โ.'}:
            temp = char[i]
            if len(char[i-1]) == 2:
                char[i] = char[i-1][1]
                char[i-1] = char[i-1][0] + temp.replace('.','')
            else:
                char[i] = char[i-1]
                char[i-1] = temp.replace('.','')    
        elif (char[i]) in {'เ..','แ..','ไ..','โ..'}:
            temp = char[i]
            char[i] = char[i-1]
            char[i-1] = char[i-2]
            char[i-2] = temp.replace('..','')
        elif char[i] in {'เ.า','เ.อ','เ.็','แ.็','เ.ิ','เ.ีย','.ิว','.็อ'}:
            if len(char[i-1]) ==2:
                char[i] = char[i-1][0] + char[i].replace('.',char[i-1][1])
                char[i-1] = '-'
            else:
                char[i] = char[i].replace('.', char[i-1])
                char[i-1] = '-'
        elif char[i] in {'เ.า.','เ.อ.','เ.็.','แ.็.','เ.ิ.','เ.ีย.','.ิว.'}:
            char[i] = char[i][:-1]
            if char[-1] == 'เ.ิ':
                 char[i] = char[i].replace('.ิ', char[i-2]+ 'ิ' + char[i-1])
            else:
                char[i] = char[i].replace('.', char[i-2]+char[i-1])
            char[i-1] = '-'
            char[i-2] = '-'

    words = ''
    for char in char:
        if char != '-':
            words += char
    return words
