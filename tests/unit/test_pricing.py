import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

class TestParsePrice:
    @pytest.mark.parametrize("input_text, expected", [
        ("$1,234.50", 1234.50),
        ("12.5", 12.5),
        ("$0.99", 0.99),
        ("1234.50", 1234.50),
        ("$12,345,678.90", 12345678.90),
    ])
    def test_parse_price_valid(self, input_text, expected):
        assert parse_price(input_text) == expected

    @pytest.mark.parametrize("invalid_input", [
        "",
        "abc",
        "$12,34,56",
    ])
    def test_parse_price_invalid(self, invalid_input):
        with pytest.raises(ValueError):
            parse_price(invalid_input)

class TestFormatCurrency:
    @pytest.mark.parametrize("value, expected", [
        (1234.5, "$1234.50"),
        (0.99, "$0.99"),
        (1000000, "$1000000.00"),
        (0, "$0.00"),
    ])
    def test_format_currency_rounding(self, value, expected):
        assert format_currency(value) == expected

    def test_format_currency_rounds_up(self):
        assert format_currency(1.996) == "$2.00"

    def test_format_currency_rounds_down(self):
        assert format_currency(1.994) == "$1.99"

class TestApplyDiscount:
    def test_apply_discount_zero_percent(self):
        assert apply_discount(100.0, 0) == 100.0

    @pytest.mark.parametrize("price, percent, expected", [
        (100.0, 10, 90.0),
        (50.0, 50, 25.0),
        (200.0, 25, 150.0),
    ])
    def test_apply_discount_valid(self, price, percent, expected):
        assert apply_discount(price, percent) == expected

    def test_apply_discount_large_percentage(self):
        assert apply_discount(100.0, 99) == 1.0

    def test_apply_discount_negative_raises_error(self):
        with pytest.raises(ValueError, match="percent must be >= 0"):
            apply_discount(100.0, -10)

class TestAddTax:
    def test_add_tax_default_rate(self):
        result = add_tax(100.0)
        
        assert result == 100.0 * 1.07

    @pytest.mark.parametrize("price, rate, expected", [
        (100.0, 0.10, 110.0),
        (50.0, 0.05, 52.5),
        (200.0, 0.0, 200.0),
    ])
    def test_add_tax_custom_rates(self, price, rate, expected):
        assert add_tax(price, rate) == expected

    def test_add_tax_negative_rate_raises_error(self):
        with pytest.raises(ValueError, match="rate must be >= 0"):
            add_tax(100.0, -0.05)

class TestBulkTotal:
    def test_bulk_total_simple_list(self):
        prices = [10.0, 20.0, 30.0]
        result = bulk_total(prices)
        
        assert result == pytest.approx(64.2)

    def test_bulk_total_empty_list(self):
        result = bulk_total([])
        assert result == 0.0

    def test_bulk_total_with_discount(self):
        prices = [100.0]
        result = bulk_total(prices, discount_percent=10)
        
        assert result == pytest.approx(96.3)

    def test_bulk_total_with_custom_tax(self):
        prices = [100.0]
        result = bulk_total(prices, discount_percent=0, tax_rate=0.10)
        
        assert result == pytest.approx(110.0)
