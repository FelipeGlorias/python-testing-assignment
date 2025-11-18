tests/unit/test_pricing.py:71: AssertionError
================================ tests coverage ================================
_______________ coverage: platform darwin, python 3.10.6-final-0 _______________

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/order_io.py      20      2    90%   12, 15
src/pricing.py       24      0   100%
-----------------------------------------------
TOTAL                44      2    95%
=========================== short test summary info ============================
FAILED tests/unit/test_pricing.py::TestParsePrice::test_parse_price_valid[$12,345,678.90-12345678.9] - ValueError: Invalid price format: $12,345,678.90
FAILED tests/unit/test_pricing.py::TestApplyDiscount::test_apply_discount_large_percentage - assert 1.0000000000000009 == 1.0
FAILED tests/unit/test_pricing.py::TestAddTax::test_add_tax_custom_rates[100.0-0.1-110.0] - assert 110.00000000000001 == 110.0
========================= 3 failed, 35 passed in 0.29s =========================
felipes-MacBook-Air:python-testing-assignment felipeglorias$ 

