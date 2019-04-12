import sqlite3
import pickle
from definition import word

db_path = 'C:\\Study and Work\\WorkSpace\\QiaoDict\\db\\'
db_name = 'data.db'


def initial():
    """
    初始化数据库操作的连接和游标
    :return: 连接和游标
    """

    coon = sqlite3.connect(db_path + db_name)
    return coon, coon.cursor()


def is_table_exist():
    """
    判断表是否已经建立
    :rtype: bool
    """

    coon, cur = initial()

    try:
        cur.execute('select name from sqlite_master where type = \'table\' and name = \'words\'')
    except sqlite3.Error as e:
        print(e)
    finally:
        temp = cur.fetchall()
        ans = False if not temp else 'words' == temp[0][0]
        cur.close()
        coon.commit()
        coon.close()

    return ans


def create_words_table():
    """
    创建 words 表
    :return: null
    """
    if is_table_exist():
        return

    coon, cur = initial()
    try:
        cur.execute('create table words(name text primary key, mean blob, sentences blob)')
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
        coon.commit()
        coon.close()


def insert_word(w):
    """
    往表里面添加一个单词
    :param w: Word, 要添加的单词
    """
    if not is_table_exist():
        print('asd')
        create_words_table()

    con, cur = initial()
    try:
        cur.execute('select count(*) from words where name = ?', (w.name,))

        # 如果单词已经在列表里面了就不用添加了
        if cur.fetchall()[0][0] == 0:
            cur.execute('insert into words(name, mean, sentences) values (?,?,?)',
                        (w.name, pickle.dumps(w.meanings), pickle.dumps(w.example_sentences)))
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()


def get_all_words():
    """
    返回所有的单词
    :rtype: List[Word]
    """
    wl = []
    con, cur = initial()
    try:
        cur.execute('select * from words')
        for row in cur:
            wl.append(word.Word(row[0], pickle.loads(row[1]), pickle.loads(row[2])))
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()
        return wl

