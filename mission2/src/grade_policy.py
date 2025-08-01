from abc import ABC, abstractmethod

LEGACY_GRADE_POLICY = "legacy_grade_policy"
FOUR_GRADE_POLICY = "four_grade_policy"

class GradePolicy(ABC):
    def __init__(self, point):
        self._point = point

    @abstractmethod
    def determine_grade(self):
        pass

    @abstractmethod
    def get_policy_name(self):
        pass

class LegacyGradePolicy(GradePolicy):
    # Three Grades Constants
    GOLD = "GOLD"
    SILVER = "SILVER"
    NORMAL = "NORMAL"
    def __init__(self, point):
        super().__init__(point)

    def determine_grade(self):
        if self._point >= 50:
            return self.GOLD
        elif self._point >= 30:
            return self.SILVER
        else:
            return self.NORMAL

    def get_policy_name(self):
        return LEGACY_GRADE_POLICY

# Example class
class FourGradePolicy(GradePolicy):
    # Four Grades Constants
    PLATINUM = "PLATINUM"
    GOLD = "GOLD"
    SILVER = "SILVER"
    NORMAL = "NORMAL"
    def __init__(self, point):
        super().__init__(point)

    def determine_grade(self):
        if self._point >= 70:
            return self.PLATINUM
        if self._point >= 50:
            return self.GOLD
        elif self._point >= 30:
            return self.SILVER
        else:
            return self.NORMAL

    def get_policy_name(self):
        return FOUR_GRADE_POLICY


def grade_policy_factory(point, policy_name) -> GradePolicy:
    if policy_name == LEGACY_GRADE_POLICY:
        return LegacyGradePolicy(point)
    elif policy_name == FOUR_GRADE_POLICY:
        return FourGradePolicy(point)
    return LegacyGradePolicy(point)