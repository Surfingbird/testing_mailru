import pytest


class TestListClass:
    @pytest.mark.parametrize(
        "input, output", [({1}, [1]), ("str", ["s", "t", "r"]), ({"a": 5}, ["a"]),]
    )
    def test_success_cast(self, input, output):
        assert output == list(input)

    def test_invalid_cast_int(self):
        try:
            list(1)
        except TypeError:
            pass

    def test_sum(self):
        a = [5, 6, 7]
        assert sum(a) == 18


class TestIntClass:
    @pytest.mark.parametrize("input, output", [(True, 1), (False, 0), ("5", 5)])
    def test_success_cast(self, input, output):
        assert output == int(input)

    def test_invalid_cast_int(self):
        try:
            int("a")
        except ValueError:
            pass

    def test_sum(self):
        assert 5 + 5 == 10
