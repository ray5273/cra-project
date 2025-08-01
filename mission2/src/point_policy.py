from abc import ABC, abstractmethod

# Policy
LEGACY_POINT_POLICY = "legacy_point_policy"
NEW_POINT_POLICY = "new_point_policy"

# Day Constants
MONDAY=0
TUESDAY=1
WEDNESDAY=2
THURSDAY=3
FRIDAY=4
SATURDAY=5
SUNDAY=6
DAYS=7

class PointPolicy(ABC):
    def __init__(self, attendance):
        self._attendance = attendance

    @abstractmethod
    def get_base_point(self):
        pass
    @abstractmethod
    def get_extra_point(self):
        pass


class LegacyPointPolicy(PointPolicy):
    def __init__(self, attendance):
        super().__init__(attendance)

    def get_base_point(self):
        base_point = 0
        for day in range(DAYS):
            if day == WEDNESDAY:
                base_point += 3 * self._attendance[day]
            elif day == SATURDAY or day == SUNDAY:
                base_point += 2 * self._attendance[day]
            else:
                base_point += self._attendance[day]
        return base_point

    def get_extra_point(self):
        extra_point = 0
        # 추가 점수
        if self._attendance[WEDNESDAY] >= 10:
            extra_point += 10
        if self._attendance[SATURDAY] + self._attendance[SUNDAY] >= 10:
            extra_point += 10
        return extra_point

class NewPointPolicy(PointPolicy):
    def get_base_point(self):
        return 100
    def get_extra_point(self):
        # Not implemented
        return 1000

def point_policy_factory(attendance, point_policy:str) -> PointPolicy:
    if point_policy == LEGACY_POINT_POLICY:
        return LegacyPointPolicy(attendance)
    elif point_policy == NEW_POINT_POLICY:
        return NewPointPolicy(attendance)
    return LegacyPointPolicy(attendance)