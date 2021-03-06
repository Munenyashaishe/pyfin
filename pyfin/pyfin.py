"""
Pyfin.py

Author: Matthew Sunner, 2021

File Contents: This file contains classes for various business and financial modeling calculations implemented in pure Python. Financial methods are grouped by relative class for the data needed for the calculation. 

Outline: 

"""

# Basic Business Math


def cogs(beg_inv, pur_inv, end_inv):
    """cogs: Cost of Goods Sold - Calculating the cost of goods sold based on Args.

    Args:
        beg_inv (float): Beginning Balance of the Value of Inventory
        pur_inv (float): Value of all Purchased Inventory
        end_inv (float): Ending Balance of the Value of Inventory

    Returns:
        cost (float): Cost of Goods Sold
    """

    cost_of_goods_sold = beg_inv + pur_inv - end_inv

    return cost_of_goods_sold


def break_even(fixed_costs, sales_price, variable_cost_per_unit):
    """break_even: Break Even Point Calculation

    Args:
        fixed_costs (float): Value of all Fixed Costs
        sales_price (float): Sales Price of the Item Being Sold
        variable_cost_per_unit (float): Variable Development Cost Associate with Item Being Sold

    Returns:
        break_even (float): Break Even Point: Number of Units to Sell to Break Even
    """

    break_even = fixed_costs / (sales_price * variable_cost_per_unit)

    return break_even
