# "abc"    "cba"   ture
# "abcd"  "abdc"   ture

def str_test(a_str, b_str):
    if a_str == b_str or len(a_str) != len(b_str):
        print("两字符串相同或两字符串长度相同，返回false")
        return False
    dif_list = []
    for i in range(0, len(a_str)):
        if a_str[i] != b_str[i]:
            dif_list.append(a_str[i])

    if len(dif_list) > 2:
        print("两字符串不是只交换一次，返回false")
        return False
    else:
        print("两字符串有且仅有一次交换，返回ture")
        return True


'''
题目2：给定一个32位有符号整数，将整数中的数字进行翻转
例如：
输入：12345
输出：54321
输入：-12345
输出：-54321
假如我们的环境只能存储32位有符号整数，取值范围是[-231, 231-1]
。根据这个假设，如果翻转后的整数溢出，则返回0
'''
import math
def test2(a_int):
    if str(a_int)[0] == "-":
        new_a = str(a_int)[1::]
        res = new_a[::-1]
        if math.pow(-2, 31)-1 <= int(res) <= math.pow(2, 31):
            print("负数的时候返回的结果是==" ,int(res) )
            return int(res)
        else:
            print("负数超出范围，返回false")
            return False
    else:
        res = str(a_int)[::-1]
        if math.pow(-2, 31) - 1 <= int(res) <= math.pow(2, 31):
            print("正数的时候返回的结果是==", int(res))
            return int(res)
        else:
            print("正数超出范围，返回false")
            return False

'''
题目3：
    a = [1, 10, 9, 8]
    target = 19
    找出列表a中两个相加等于19的元素
'''

def test3(a_list, target):
    if not a_list:
        print("给的列表是空，返回false")
        return False
    else:
        for i in a_list:
            for j in range(a_list.index(i)+1, len(a_list)):
                if i + a_list[j] == target:
                    print("找到两个元素，两个元素是{}和{}".format(i, a_list[j]))
                    return True


def Single_zhan(alist):
    stack = []
    n = len(alist)
    for i in range(n-1, -1, -1):
        while stack and stack[-1]  > alist[i]:
            stack.pop()
        stack.append(alist[i])


'''
题目四： 单调栈
    有两个数组num1 和 num2 其中num1是num2的子集，找出num1中每个元素在num2中下一个比其大的值。没有则返回-1
    例如：
        输入：num1 = [4, 1, 2]  num2 = [1, 3, 4, 2]
        输出：[-1, 3, -1]
        
        输入：num1 = [2, 4]    num2 = [1, 2, 3, 4]
        输出：[3, -1]
        
    解析：
        1）stack = [2]
        2) 4 > 2 => [4]
        3) 3 < 4 => [4, 3]
        4) 1 < 3 => [4, 3, 1]
'''
def test4(num1, num2):
    dic = {}
    n = len(num2)
    stack = []
    for i in range(n-1, -1, -1):
        x = num2[i]
        if not stack:
            dic[x] =  -1
        while stack and stack[-1] < x:
            stack.pop()
        dic[x] = stack[-1] if stack else -1
        stack.append(num2[i])

    print(dic)
    for j in range(len(num1)):
        num1[j] = dic[num1[j]]
    print(num1)
    return num1


'''
题目5：最大宽度坡
    给定一个整数数组A，坡是[i, j],其中i<j,且A[i] <= A[j]。这样坡的宽度j-i
    找出A的最大宽度坡，不存在返回 0
    示例1： 
        输入：[6, 0, 8, 2, 1, 5]
        输出：4
    示例2：
        输入：[9, 8, 1, 0, 1, 9, 4, 0, 4]
        输出：7
        
def test5(alist):
    n = len(alist)
    stack = []
    # stack中添加的是元素的下标，使用单调栈找到有定增关系的元素
    for i in range(n):
        if not stack or alist[stack[-1]] > alist[i]:
            stack.append(i)
    j = n - 1
    res = 0
    while j > res:
        while stack and alist[stack[-1]] <= alist[j]:
            res = max(res, j - stack[-1])
            stack.pop()
        j -= 1
    print(res)
    return res
'''

'''
题目六：
    给一个工作时间表hours，记录着每天每个员工的工作时间。一个员工一天的工作时间大于8小时则是劳累的一天
    所谓表现良好的时间段意味着劳累天数严格大于不劳累天数
    返回表现良好时间段的最大长度
    示例一：
        输入：hours = [9, 9, 6, 0, 6, 6, 9]
        输出：3
        解释：最长的表现良好时间段是[9, 9, 6]
'''

def test6(hours):
    # values = [1, 1, -1, -1, -1, -1, 1]
    # sum_pre= [0, 0, 0, 0, 0, 0, 0, 0]
    values = list(map(lambda x:1 if x > 8 else -1, hours))
    sum_pre = [0] * (len(values)+ 1)
    for i in range(1, len(values)+1):
        # values[i] = sum_pre[i] - sum_pre[i-1]
        sum_pre[i] = sum_pre[i-1] + values[i-1]
    # 此时的sum_pre = [0, 1, 2, 1, 0, -1, -2, -1]
    res = 0
    stack = []
    for i in range(len(values)+ 1):
        if not stack or sum_pre[stack[-1]] > sum_pre[i]:
            stack.append(i)



'''
题目七：前缀和数组
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数
    示例 1 :
        输入:nums = [1,1,1], k = 2
        输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
'''
def test7(num, k):
    sum_pre = [0] * (len(num)+1)
    for i in range(1, len(num)+1):
        sum_pre[i] = sum_pre[i-1] + num[i-1]
    print(sum_pre)
    for i in sum_pre:
        if i == k:
            res = sum_pre.index(k)
            print(res)


'''
题目八：快速排序
'''
def qiuck_sort(alist, i, j):
    if i >= j:
        return alist
    low = i
    high = j
    standar = alist[i]
    while i < j:
        while i < j and alist[j] >= standar:
            j -= 1
        alist[i] = alist[j]
        while i < j and alist[i] <= standar:
            i += 1
        alist[j] = alist[i]
    alist[j] = standar
    qiuck_sort(alist, low, j-1)
    qiuck_sort(alist,j+1, high)
    print(alist)



'''
题目九：统计1出现最多的个数[0,1,1,0,0,1,1,1,1,1,0]
'''
def test9(alist):
    count = 0
    max_count = 1
    for i in alist:
        if i == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    print(max_count)

'''
题目十：找出列表中连续的元素[3,4,5,6,7,10,1,2,3,7,3,7,2,8]
'''
def test10(alist):
    list1 = []
    n = len(alist)
    for i in range(n-1):
        if alist[i+1] == alist[i] + 1:
            list1.append(alist[i])
    print(list1)








if __name__ == "__main__":
    # num1 = [4, 1, 2]
    # num2 = [1, 3, 4, 2]
    # nums = [0,1,1,0,0,1,1,1,1,1,0]
    # test9(nums)
    # test2(a_int=-1234)
    # test3([1, 10, 9, 8], target=9)
    # Single_zhan()
    # num1 = [9, 9, 6, 0, 6, 6, 9]
    # test6(num1)
    # num = [1, 1, 1, 1,2]
    # test7(num, 4)
    # def subarraySum(nums, k):
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     sum = 0  # 前缀和
    #     sum_dict = {0: 1}  # 记录前缀和数量
    #     count = 0
    #     for i in range(n):
    #         sum += nums[i]
    #         if sum_dict.get(sum - k):
    #             count += sum_dict.get(sum - k)  # +前缀数量
    #         sum_dict[sum] = sum_dict.get(sum, 0) + 1
    #     print(count)
    #     return count
    # subarraySum(num, 4)
    # nums = [3,4,5,6,7,10,1,2,3,7,3,7,2,8]
    # test10(nums)