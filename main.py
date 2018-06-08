import json
import chardet
from chardet.universaldetector import UniversalDetector


def top_words_json(filename):

    detector = UniversalDetector()
    # filename = input('Введите название файла в формате "name.txt": ')
    # n = int(input('Укажите, какое число наиболее часто встречающихся слов Вы хотите найти: '))
    n = 10
    # word_l = int(input('Укажите минимальную длину слов, участвующих в "рейтинге" наиболее часто встречающихся: '))
    word_l = 6

    with open(filename, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        code_type = detector.result['encoding']
        print('Файл {} выполнен в кодировке {}' .format(filename, code_type))

    with open(filename, 'r', encoding=code_type) as f:

        text = []
        data = json.load(f)

        for i in range(len(data['rss']['channel']['items'])-1):
            text.append(data['rss']['channel']['items'][i]['description'])

        pure_text = ''.join(text)
        s = pure_text.lower()
        s = s.replace('.', '')
        s = s.replace(',', '')
        s = s.replace('!', '')
        s = s.replace(':', '')
        s = s.replace(';', '')
        s = s.replace('?', '')

        all_words = s.split(' ')
        dic = {}

        for x in all_words:
            if (len(x) >= word_l):
                k = s.count(x)
                dic[x] = k
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        #
        print('{} слов длиннее {} букв, наиболее часто встречающихся в {}: '.format(n, word_l, filename))
        q = 1
        for z in dic:
            if (q > n):
                break
            q = q + 1
            print(str(z))
        print('\n')


json_file_1 = top_words_json('newsafr.json')

json_file_2 = top_words_json('newscy.json')

json_file_3 = top_words_json('newsfr.json')

json_file_4 = top_words_json('newsit.json')

print(json_file_1)

print(json_file_2)

print(json_file_3)

print(json_file_4)
