import random
from abc import ABCMeta, abstractmethod


class BaseLottery(metaclass=ABCMeta):
    def __init__(self):
        self.lottery1_first_half = []
        self.lottery1_last_half = []
        self.lottery2_first_half = []
        self.lottery2_last_half = []

    @abstractmethod
    def CheckForm(self, lottery_number1, lottery_number2):
        pass

    @abstractmethod
    def GetLevel(self, lottery_number, lottery_number2):
        pass


class Lottery1(BaseLottery):
    def __init__(self):
        super().__init__()
        while True:
            number = random.randint(1, 33)
            if number not in self.lottery1_first_half:
                self.lottery1_first_half.append(number)
            if len(self.lottery1_first_half) == 6:
                break
        self.lottery1_last_half.append(random.randint(1, 16))
        self.award_dict = {'一等奖': [(6, 1)],
                           '二等奖': [(6, 0)],
                           '三等奖': [(5, 1)],
                           '四等奖': [(5, 0), (4, 1)],
                           '五等奖': [(4, 0), (3, 1)],
                           '六等奖': [(2, 1), (1, 1), (0, 1)]}

    def CheckForm(self, lottery_number1, lottery_number2):
        flag = True
        if len(set(lottery_number1)) < 6:
            flag = False
            return flag
        for i in lottery_number1:
            if not 1 <= int(i) <= 33:
                flag = False
                return flag
        if not 1 <= int(lottery_number2[0]) <= 16:
            flag = False
            return flag
        return flag

    def GetLevel(self, lottery_number1, lottery_number2):
        first_half = 0
        last_half = 0
        for i in lottery_number1:
            if int(i) in self.lottery1_first_half:
                first_half += 1
        if int(lottery_number2[0]) == int(self.lottery1_last_half[0]):
            last_half += 1
        for key, value in self.award_dict.items():
            if (first_half, last_half) in value:
                return key
        return 0


class Lottery2(BaseLottery):
    def __init__(self):
        super().__init__()
        while True:
            number = random.randint(1, 35)
            if number not in self.lottery2_first_half:
                self.lottery2_first_half.append(number)
            if len(self.lottery2_first_half) == 5:
                break
        while True:
            number = random.randint(1, 12)
            if number not in self.lottery2_last_half:
                self.lottery2_last_half.append(number)
            if len(self.lottery2_last_half) == 2:
                break
        self.award_dict = {'一等奖': [(5, 2)],
                           '二等奖': [(5, 1)],
                           '三等奖': [(5, 0), (4, 2)],
                           '四等奖': [(3, 2), (4, 1)],
                           '五等奖': [(4, 0), (3, 1), (2, 2)],
                           '六等奖': [(2, 1), (1, 2), (3, 0), (2, 0)]}

    def CheckForm(self, lottery_number1, lottery_number2):
        flag = True
        if len(set(lottery_number1)) < 5 or len(set(lottery_number2)) < 2:
            flag = False
            return flag
        for i in lottery_number1:
            if not 1 <= int(i) <= 35:
                flag = False
                return flag
        for i in lottery_number2:
            if not 1 <= int(i) <= 12:
                flag = False
                return flag
        return flag

    def GetLevel(self, lottery_number1, lottery_number2):
        first_half = 0
        last_half = 0
        for i in lottery_number1:
            if int(i) in self.lottery2_first_half:
                first_half += 1
        for i in lottery_number2:
            if int(i) in self.lottery2_last_half:
                last_half += 1
        for key, value in self.award_dict.items():
            if (first_half, last_half) in value:
                return key
        return 0


if __name__ == "__main__":
    lottery_number1 = []
    lottery_number2 = []
    choice = input("请选择玩法 输入数字：1.双色球，2.大乐透\n")
    if choice == "1":
        print("请输入前6个中奖号码，范围为1-33")
        for i in range(6):
            lottery_number1.append(input())
        print("请输入最后一位中奖号码，范围为1-16")
        lottery_number2.append(input())
        lottery = Lottery1()
        if not lottery.CheckForm(lottery_number1, lottery_number2):
            print("您的输入格式错误")
        else:
            print("中奖号码是：",
                  lottery.lottery1_first_half, lottery.lottery1_last_half)
            result = lottery.GetLevel(lottery_number1, lottery_number2)
            if not result:
                print("您没有中奖")
            else:
                print("您中了{}".format(result))
    elif choice == "2":
        print("请输入前5个中奖号码，范围为1-35")
        for i in range(5):
            lottery_number1.append(input())
        print("请输入后2位中奖号码，范围为1-12")
        for i in range(2):
            lottery_number2.append(input())
        print(lottery_number1, lottery_number2)
        lottery = Lottery2()
        if not lottery.CheckForm(lottery_number1, lottery_number2):
            print("您的输入格式错误")
        else:
            print("中奖号码是：",
                  lottery.lottery2_first_half, lottery.lottery2_last_half)
            result = lottery.GetLevel(lottery_number1, lottery_number2)
            if not result:
                print("您没有中奖")
            else:
                print("您中了{}".format(result))