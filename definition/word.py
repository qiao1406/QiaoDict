class Meaning(object):
    """
        the word's Chinese meaning
    """

    def __init__(self, m, p='n'):
        """

        :param m: string, 中文意思
        :param p: string, 词性
        """

        self.chinese_mean = m
        self.property = p

    def __str__(self):
        return self.property + '. ' + self.chinese_mean


class Sentence(object):
    """
        Example Sentence
    """

    def __init__(self, s='', cm=''):
        """

        :param s: string, 英文例句
        :param cm: string, 英文例句的中文释义
        """
        self.eng_sentence = s
        self.chn_sentence = cm

    def __str__(self):
        return self.eng_sentence + ' ' + self.chn_sentence


class Word(object):
    """
        A definition of word
    """

    def __init__(self, name, meanings, example_sentences=[]):
        """

        :param name: string, 单词名
        :param meanings: List[Meaning], 中文意思，可能有多个
        :param example_sentence: List[string], 例句，可以为空，可以有很多个
        """

        self.name = name
        self.meanings = meanings
        self.example_sentences = example_sentences

    def __str__(self):
        s = '[' + self.name + ']\n'

        for m in self.meanings:
            s += str(m) + '\n'

        if self.example_sentences:
            s += '\ne.g.\n'

            for es in self.example_sentences:
                s += str(es) + '\n'

        return s + '=============================\n'

    def add_example_sentence(self, s):
        """
        给该单词增加一条例句
        :param s: Sentence, 要添加的例句
        :return null
        """

        self.example_sentences.append(s)

    def update_meanings(self, m):
        """

        :param m: Meaning，要添加的中文意思
        :return boolean, 判断意思是否存在，若不存在则添加成功返回 True，否则失败返回 False
        """

        for x in self.meanings:
            if x == m:
                return False

        self.meanings.append(m)
        return True
