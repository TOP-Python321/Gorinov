import csv
from pathlib import Path
from sys import path


class CountableNouns:
    """Предоставляет интерфейс для работы с файловой базой существительных"""
    db_path: Path = Path(path[0]) / 'words.csv'
    words: dict[str, tuple[str, str]] = {}
    
    with open(db_path, encoding='utf-8') as csvfile:
        line = csv.reader(csvfile)
        for i in line:
            words |= {i[0]: tuple(i[1:])}       
    
    @classmethod
    def pick(self, number: int, word: str) -> str:
        """
        Принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает
        согласованное с переданным числом существительное. Если существительное отсутствует в базе, вызывает метод
        save_words() и передает существительное в качестве аргумента.
        """
        exception: list = [11, 12, 13, 14]
        last_digit: int = number % 10
        last_two_digits: int = number % 100
        if word in self.words:
            if last_digit == 1 and last_two_digits not in exception:
                return word
            elif last_digit in [2, 3, 4] and last_two_digits not in exception:
                return self.words[word][0]
            return self.words[word][1]
        self.save_words(word)   
        
    @classmethod
    def save_words(self, word1: str = None) -> None:
        """
        Запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные
        значения в поле класса words и дописывает их в файл с базой существительных.
        """
        if not word1 is None:
            print(f'существительное {word1} отсутствует в базе')        
        if word1 is None:
            word1 = input('\tвведите слово, согласующееся с числительным "один": ')        
        word2: str = input('\tвведите слово, согласующееся с числительным "два": ')
        word5: str = input('\tвведите слово, согласующееся с числительным "пять": ')
        self.words[word1] = tuple([word2, word5])  

        # пока толком не разобрался с записью и чтением csv файлов, такой способ работает.
        with open(self.db_path, 'w', encoding='utf-8') as csvfile:
            line = csv.writer(csvfile, lineterminator='\n')
            line.writerows([k, *(self.words[k])] for k in self.words)

# >> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(21, 'год')
# 'год'
# >>> CountableNouns.pick(360, 'день')
# 'дней'
# >>> CountableNouns.pick(21, 'машина')
# существительное машина отсутствует в базе
        # введите слово, согласующееся с числительным "два": машины
        # введите слово, согласующееся с числительным "пять": машин
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'машина': ('машины', 'машин')}
# >>> CountableNouns.save_words()
        # введите слово, согласующееся с числительным "один": этаж
        # введите слово, согласующееся с числительным "два": этажа
        # введите слово, согласующееся с числительным "пять": этажей
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# машина,машины,машин
# этаж,этажа,этажей