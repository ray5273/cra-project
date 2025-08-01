from mission2.src.point_policy import LEGACY_POINT_POLICY, point_policy_factory, PointPolicy, NewPointPolicy, \
    LegacyPointPolicy, NEW_POINT_POLICY


def test_point_policy_factory_legacy():
    # Given : attendance and legacy point policy constant.
    attendance = []
    # When : point_policy_factory() is called
    policy = point_policy_factory(attendance,LEGACY_POINT_POLICY)
    # Then : instance is LegacyPointPolicy
    assert isinstance(policy, LegacyPointPolicy)


def test_point_policy_factory_default():
    # Given : attendance without constant
    attendance = []
    # When : point_policy_factory() is called
    policy = point_policy_factory(attendance,"")
    # Then : instance is LegacyPointPolicy
    assert isinstance(policy, LegacyPointPolicy)

def test_point_policy_factory_four():
    # Given : attendance with NEW_POINT_POLICY constant
    attendance = []
    # When : point_policy_factory() is called
    policy = point_policy_factory(attendance,NEW_POINT_POLICY)
    # Then : instance is NEW_POINT_POLICY
    assert isinstance(policy, NewPointPolicy)

def test_point_policy_new_point_policy():
    # Given : attendance with NEW_POINT_POLICY constant
    attendance = []
    # When : point_policy_factory() is called
    policy = point_policy_factory(attendance,NEW_POINT_POLICY)
    # Then : instance is NEW_POINT_POLICY
    assert isinstance(policy, NewPointPolicy)

    # Then : base_point and extra_point must be 100, 1000
    assert policy.get_base_point() == 100
    assert policy.get_extra_point() == 1000