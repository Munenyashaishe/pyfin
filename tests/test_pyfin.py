import pytest

from pyfin import cogs


def test_cogs():
    beg_inv = 100.00
    pur_inv = 400.00
    end_inv = 50.00

    assert cogs(beg_inv, pur_inv, end_inv) == 450.00
