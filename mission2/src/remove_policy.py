from abc import ABC, abstractmethod
from .grade_policy import LEGACY_GRADE_POLICY, FOUR_GRADE_POLICY, FourGradePolicy

# Day Constants
MONDAY=0
TUESDAY=1
WEDNESDAY=2
THURSDAY=3
FRIDAY=4
SATURDAY=5
SUNDAY=6
DAYS=7

class RemovePolicy(ABC):
    def __init__(self, grade_policy, attendance):
        self._grade_policy = grade_policy
        self._attendance = attendance

    @abstractmethod
    def is_remove_candidate(self):
        pass


class LegacyRemovePolicy(RemovePolicy):
    def __init__(self, _grade_policy, attendance):
        super().__init__(_grade_policy, attendance)

    def is_remove_candidate(self):
        if (self._grade_policy.determine_grade() == "NORMAL" and
                (self._attendance[SUNDAY] == 0 and self._attendance[SATURDAY] == 0 and self._attendance[WEDNESDAY] == 0)):
            return True
        return False


class FourGradeRemovePolicy(RemovePolicy):
    # example
    def __init__(self, _grade_policy, attendance):
        super().__init__(_grade_policy, attendance)

    def is_remove_candidate(self):
        return True

def remove_policy_factory(grade_policy, attendance)-> RemovePolicy:
    if grade_policy.get_policy_name() == FOUR_GRADE_POLICY:
        return FourGradeRemovePolicy(grade_policy, attendance)
    else:
        return LegacyRemovePolicy(grade_policy, attendance)