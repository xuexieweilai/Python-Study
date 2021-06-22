'''
找出字符串中第一个只出现一次的单词
例如： abcdbacd  => b
'''

def test(astr):
    for i in astr:
        if astr.count(str(i)) == 1:
            print(i)


if __name__ == "__main__":
    test("abcdbac")
