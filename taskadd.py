"""*****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами
Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь"""

dictionaryMillions = {1: 'один миллион', 2: 'два миллиона', 3: 'три миллиона', 4: 'четыре миллиона', 5: 'пять миллионов',
               6: 'шесть миллионов', 7: 'семь миллионов', 8: 'восемь миллионов', 9: 'девять миллионов'}
dictionaryThousands = {1: 'одна тысяча', 2: 'две тысячи', 3: 'три тысячи', 4: 'четыре тысячи', 5: 'пять тысяч',
                      6: 'шесть тысяч', 7: 'семь тысяч', 8: 'восемь тысяч', 9: 'девять тысяч', 10: 'тысяч'}
dictionaryHundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот',
                      7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
dictionaryTenth = {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят',
                   7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
dictionaryOnes = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
                  9: 'девять'}
n = input('Введите желаемое число: ')
list = []
if int(n) >= 1000000:
    for j in dictionaryMillions:
        if int(n[0]) == j:
            list.append(dictionaryMillions[j])
            break
    for i in dictionaryHundreds:
        if int(n[1]) == i:
            list.append(dictionaryHundreds[i])
            break
    for i in dictionaryTenth:
        if int(n[2]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryThousands:
        if int(n[3]) == i:
            list.append(dictionaryThousands[i])
            break
    for i in dictionaryHundreds:
        if int(n[4]) == i:
            list.append(dictionaryHundreds[i])
            break
    for i in dictionaryTenth:
        if int(n[5]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryOnes:
        if int(n[6]) == i:
            list.append(dictionaryOnes[i])
            break
elif int(n) < 1000000 and int(n) >= 100000:
    for i in dictionaryHundreds:
        if int(n[0]) == i:
            list.append(dictionaryHundreds[i])
            break
    for i in dictionaryTenth:
        if int(n[1]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryThousands:
        if int(n[2]) == i:
            list.append(dictionaryThousands[i])
            break
    for i in dictionaryHundreds:
        if int(n[3]) == i:
            list.append(dictionaryHundreds[i])
            break
    for i in dictionaryTenth:
        if int(n[4]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryOnes:
        if int(n[5]) == i:
            list.append(dictionaryOnes[i])
            break
elif int(n) < 100000 and int(n) > 1000:
    for i in dictionaryTenth:
        if int(n[0]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryThousands:
        if int(n[1]) == i:
            list.append(dictionaryThousands[i])
            break
    for i in dictionaryHundreds:
        if int(n[2]) == i:
            list.append(dictionaryHundreds[i])
            break
    for i in dictionaryTenth:
        if int(n[3]) == i:
            list.append(dictionaryTenth[i])
            break
    for i in dictionaryOnes:
        if int(n[4]) == i:
            list.append(dictionaryOnes[i])
            break
elif int(n) == 1000:
    for i in dictionaryThousands:
        if int(n[0]) == i:
            list.append(dictionaryThousands[i])
            break
print(*list)
    
