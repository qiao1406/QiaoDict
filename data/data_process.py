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

    con, cur = initial()

    try:
        cur.execute('select name from sqlite_master where type = \'table\' and name = \'words\'')
    except sqlite3.Error as e:
        print(e)
    finally:
        temp = cur.fetchall()
        ans = False if not temp else 'words' == temp[0][0]
        cur.close()
        con.commit()
        con.close()
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
    :return bool, 插入成功返回 True 否则返回 False
    """
    if not is_table_exist():
        create_words_table()

    success = False
    con, cur = initial()
    try:
        cur.execute('select count(*) from words where name = ?', (w.name,))

        # 如果单词已经在列表里面了就不用添加了
        if cur.fetchall()[0][0] == 0:
            cur.execute('insert into words(name, mean, sentences) values (?,?,?)',
                        (w.name, pickle.dumps(w.meanings), pickle.dumps(w.example_sentences)))
            success = True
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()
        return success


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


def look_for_dict(name):
    """
    查找并返回单词
    :param name: string, 要查找的单词名字
    :return: string, 查找结果
    """
    con, cur = initial()
    ans = ''
    try:
        cur.execute('select * from words where name = ?', (name,))
        temp = cur.fetchall()[0]
        ans = str(word.Word(temp[0], pickle.loads(temp[1]), pickle.loads(temp[2])))
    except sqlite3.Error as e:
        print(e)
    finally:
        ans = '未找到单词：' + name + '\n=============================\n' if not ans else ans
        cur.close()
        con.commit()
        con.close()
        return ans


def clear_word_table():
    """
    清空单词表
    """
    con, cur = initial()
    try:
        cur.execute('delete from words')
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()


# print(len(get_all_words()))
# for w in get_all_words():
#
#     print(w)