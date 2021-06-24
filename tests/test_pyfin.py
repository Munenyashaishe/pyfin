import pytest

from pyfin import cogs, break_even


def test_cogs():
    beg_inv = 100.00
    pur_inv = 400.00
    end_inv = 50.00

    assert cogs(beg_inv, pur_inv, end_inv) == 450.00


def test_break_even():
    fixed_cost = 1000
    sales_price = 50
    variable_cost = 10

    assert break_even(fixed_cost, sales_price, variable_cost) == 2
