import datetime
import re

class monthYearDate:
    list_chinese = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    list_int = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

    def __init__(self, year, month):
        ###构造函数，year可以是整数或带有“年”的文字。month可以是整数或带有“月”的文字。
        if isinstance(year, int):
            self.year = year
        elif isinstance(year,str):
            y=monthYearDate.find_years(year)
            if y==0:
                raise ValueError("Year must be an integer.")
            else:
                self.year=y
        else:
            raise ValueError("Year must be an integer.")

        if isinstance(month, int):
            if month % 12==0:
                self.month=12
            else:
                self.month=month %12
        elif isinstance(month, str):
            m=monthYearDate.find_month_elements(month)
            self.month = m
        else:
            raise ValueError("Month must be either an integer or a string.")

    def __str__(self):
        return str(self.year) + "年" +str(self.month)+"月"

    def __eq__(self, other):
        #### 重写等于运算符（==），用于判断两个对象是否相等
        if isinstance(other, monthYearDate):
            return self.year == other.year and self.month == other.month
        return False

    def __ne__(self, other):
        ####重写不等于运算符（!=），用于判断两个对象是否不相等。
        return not self.__eq__(other)

    def __lt__(self, other):
        ####重写小于运算符（<），用于判断一个对象是否小于另一个对象。
        if isinstance(other, monthYearDate):
            if self.year < other.year:
                return True
            elif self.year == other.year:
                return self.month < other.month
        return False

    def __gt__(self, other):
        ######重写大于运算符（>），用于判断一个对象是否大于另一个对象。
        if isinstance(other, monthYearDate):
            if self.year > other.year:
                return True
            elif self.year == other.year:
                return self.month > other.month
        return False

    def __le__(self, other):
        #####重写小于等于运算符（<=），用于判断一个对象是否小于等于另一个对象。
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        ####重写大于等于运算符（>=），用于判断一个对象是否大于等于另一个对象。
        return self.__eq__(other) or self.__gt__(other)

    def add_month(self,month_int):
        ####增加月数
        return monthYearDate(self.year + ((self.month+month_int-1) // 12),self.month+month_int)

    def is_cover(self,month_int,other):
        ######判断本对象增加month_int个月后，是否在other范围内
        new_date=self.add_month(month_int)
        print(new_date)
        print(other)
        if isinstance(other, monthYearDate):
            if new_date<=other:
                return True
            return False

    def get_year(self):
        return str(self.year) + "年"
    def get_month(self):
        return monthYearDate.list_int[self.month - 1]
    def get_month_chinese(self):
        return monthYearDate.list_chinese[self.month - 1]






    @staticmethod
    def find_month_elements(str_1):
        #根据字符串查找并返回数字月份
        reversed_list = list(reversed(monthYearDate.list_chinese))
        for element in reversed_list:
            if element in str_1:
                return monthYearDate.list_chinese.index(element)+1
        reversed_list = list(reversed(monthYearDate.list_int))
        for element in reversed_list:
            if element in str_1:
                return monthYearDate.list_int.index(element)+1
        return 0

    @staticmethod
    def find_years(string):
        #根据字符串返回4位数字年份。
        pattern = r"(\d{2}年)"
        matches = re.findall(pattern, string)
        if matches[0]:
            return int(matches[0].strip("年"))+2000
        else:
            return 0

    ##########################
    @staticmethod
    def get_data(offset=0):
        ####引导获得当前年月，offse是时间向前的偏移月份。
        a = datetime.datetime.today()
        text1 = f"按任意键对{a.year}年数据进行操作作或输入4位数字年份回车:"
        text2 = input(text1)

        if text2.isdigit() and len(text2) == 4:
            print("处理", text2, "年数据")
            y = int(text2)
        else:
            print("输入不是4位数字。处理", a.year, "年数据")
            y = a.year

        text3 = f"按任意键对{a.month-offset}月数据进行操作作或输入数字月份回车:"
        text4 = input(text3)

        if text4.isdigit():
            integer_input = int(text4)
            if integer_input < 13:
                print(f"处理：{integer_input}月数据")
                m = integer_input
            else:
                print(f"输入的整数不小于12。处理：{a.month}月数据")
                m = a.month-offset
        else:
            print(f"输入不是整数。处理：{a.month}月数据")
            m = a.month-offset

        return monthYearDate(y, m)


