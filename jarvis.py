import csv
import operator
import os


class Jarvis(object):
    def __init__(self):
        self.check = os.path.exists('ranking.csv')
        self.fieldnames = ('NAME', 'COUNT')
        if self.check is True:
            with open('ranking.csv', 'r') as rank_csv:
                ranking = csv.DictReader(rank_csv)
                result = sorted(ranking, key=operator.itemgetter('COUNT'), reverse=True)
                self.recommend = (i['NAME'] for i in result)

    def say_hello(self):
        name = input('こんにちは。わたしはジャービスです。あなたの名前を教えてください。\n')
        self.c_name = name.title()
        return self.c_name

    def y_or_n(self):
        r_sport = next(self.recommend)
        while True:
            try:
                y_n = input('\nわたしのおすすめのスポーツは{}です。\nあなたはこのスポーツが好きですか？ [Yes/No]\n'.format(r_sport))
                if 'Y' in str.upper(y_n):
                    break
                elif 'N' in str.upper(y_n):
                    r_sport = next(self.recommend)
                    continue
                else:
                    print('\nYes か No で答えてください。')
            except:
                break

    def ask_main(self):
        like_sports = input('\n{}さん、あなたの好きなスポーツは何ですか？\n英語で答えてください\n'.format(self.c_name))
        self.c_like_sports = like_sports.title()
        return self.c_like_sports

    def write_csv(self):
        if self.check is True:
            with open('ranking.csv', 'r') as rank_c:
                ranking = csv.DictReader(rank_c)

                refresh_csv = []
                for i in ranking:
                    if i['NAME'] == self.c_like_sports:
                        num = i['COUNT']
                        a_num = int(num) + 1
                        i['COUNT'] = a_num
                    refresh_csv.append(i)
                rank_c.seek(0)
                check_sports = []
                for j in ranking:
                    check_sports.append(j['NAME'])

            if self.c_like_sports in check_sports:
                with open('ranking.csv', 'w') as rank_csv:
                    writer = csv.DictWriter(rank_csv, fieldnames=self.fieldnames)
                    writer.writeheader()
                    writer.writerows(refresh_csv)
            else:
                with open('ranking.csv', 'a') as rank_csv:
                    writer = csv.DictWriter(rank_csv, fieldnames=self.fieldnames)
                    writer.writerow({'NAME': self.c_like_sports, 'COUNT': 1})
        else:
            with open('ranking.csv', 'w', encoding='UTF-8') as rank_csv:
                writer = csv.DictWriter(rank_csv, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerow({'NAME': self.c_like_sports, 'COUNT': 1})

    def __del__(self):
        print('\n{}さん、回答ありがとうございました。\n良い1日をお過ごし下さい！'.format(self.c_name))


if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.say_hello()
    if jarvis.check is True:
        jarvis.y_or_n()
    jarvis.ask_main()
    jarvis.write_csv()
    del jarvis
