# Given a pair of dates in some recognizable standard format such as

# MM/DD/YY or DD/MM/YY, determine the total number of days that fall

# between both dates


def day_calculator(num):
    months = [
        (1, 31),
        # feb will be inserted dynamically depending upon leap year
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31)
    ]

    def days_between(self):
        days = DateConvertor.days_upto_year_end(*self.d1)
        days += sum((366 if leap_year(y) else 365)
                    for y in range(self.d1[2] + 1, self.d2[2]))
        days += DateConvertor.days_from_year_start(*self.d2)
        return days

print(day_calculator('2/3/4'))
