# Day Constants
MONDAY=0
TUESDAY=1
WEDNESDAY=2
THURSDAY=3
FRIDAY=4
SATURDAY=5
SUNDAY=6
DAYS=7

# Grades Constants
GOLD = "GOLD"
SILVER = "SILVER"
NORMAL = "NORMAL"
# User class
class User:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self._attendance = [0 for _ in range(DAYS)] # 월요일 ~ 일요일 데이터
        self._points = 0
        self._grade = None

    def get_grade(self):
        if self._points >= 50:
            self._grade = GOLD
        elif self._points >= 30:
            self._grade = SILVER
        else:
            self._grade = NORMAL
        return self._grade

    def get_points(self):
        # 기본 점수
        for day in range(7):
            if day == WEDNESDAY:
                self._points += 3 * self._attendance[day]
            elif day == SATURDAY or day == SUNDAY:
                self._points += 2 * self._attendance[day]
            else:
                self._points += self._attendance[day]
        # 추가 점수
        if self._attendance[WEDNESDAY] >= 10:
            self._points += 10
        if self._attendance[SATURDAY] + self._attendance[SUNDAY] >= 10:
            self._points += 10
        return self._points

    def add_attendance_data(self, day:str):
        if day == "monday":
            self._attendance[MONDAY] += 1
        elif day == "tuesday":
            self._attendance[TUESDAY] += 1
        elif day == "wednesday":
            self._attendance[WEDNESDAY] += 1
        elif day == "thursday":
            self._attendance[THURSDAY] += 1
        elif day == "friday":
            self._attendance[FRIDAY] += 1
        elif day == "saturday":
            self._attendance[SATURDAY] += 1
        elif day == "sunday":
            self._attendance[SUNDAY] += 1

    def is_remove_candidate(self)-> bool:
        if (self.get_grade() == "NORMAL" and
                (self._attendance[SUNDAY] == 0 and self._attendance[SATURDAY] == 0 and self._attendance[WEDNESDAY] == 0)):
            return True
        return False

    def print_user_info(self):
        print(f"NAME : {self.name}, POINT : {self.get_points()}, GRADE : {self.get_grade()}", end="\n")