import logging

import pytest
import yaml

from HOGWARTS.hogwarts.homework.pythoncode.calculator import Calculator


def get_calc_datas():
    with open('datas/calc.yml') as f:
        totals = yaml.safe_load(f)
        # return (totals["add"]["success"]["datas"], totals["add"]["success"]["ids"])
        return totals


def test_getdatas():
    print(get_calc_datas())


class TestCalculator:

    def setup(self):
        logging.info("开始计算")
        self.calc = Calculator()

    def teardown(self):
        logging.info("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize(
        'a, b, expect',
        get_calc_datas()['add']['success']['datas'],
        ids=get_calc_datas()['add']['success']['ids']
    )
    def test_add_success(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.add
    @pytest.mark.parametrize(
        'a, b, expect',
        get_calc_datas()['add']['faild']['datas'],
        ids=get_calc_datas()['add']['faild']['ids']
    )
    def test_add_faild(self, a, b, expect):
        try:
            self.calc.div(a, b)
        except Exception as e:
            print(e)
        assert expect == self.calc.add(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize(
        'a, b, expect',
        get_calc_datas()['div']['success']['datas'],
        ids=get_calc_datas()['div']['success']['ids']
    )
    def test_div_success(self, a, b, expect):
        assert expect == self.calc.div(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize(
        'a, b, expect',
        get_calc_datas()['div']['faild']['datas'],
        ids=get_calc_datas()['div']['faild']['ids']
    )
    def test_div_faild(self, a, b, expect):
        try:
            self.calc.div(a, b)
        except Exception as e:
            print(e)
        assert expect == self.calc.div(a, b)






