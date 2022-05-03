class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, u_date: str) -> 'Date':
        date_list = u_date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        date_obj = cls(day, month, year)
        return date_obj

    @classmethod
    def is_date_valid(cls, u_date: str) -> bool:
        date_list = u_date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        if 31 >= day >= 0 and 12 >= month >= 0 and year >= 0:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'День: {self.day}    Месяц: {self.month}   Год: {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
