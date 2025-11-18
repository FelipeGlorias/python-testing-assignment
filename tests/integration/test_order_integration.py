import pytest
from src.order_io import load_order, write_receipt
from src.pricing import bulk_total

def test_order_integration_basic(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,$5.50\n", encoding="utf-8")

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent=10, tax_rate=0.1)

    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL:" in output_text

def test_order_integration_with_discount(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("item1,$100.00\n", encoding="utf-8")

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent=20, tax_rate=0.07)

    text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "item1: $100.00" in text
    assert "TOTAL:" in text

def test_order_integration_multiple_items(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("apple,$1.50\nbanana,$0.75\norange,$2.00\n", encoding="utf-8")

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent=0, tax_rate=0.07)

    text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "apple: $1.50" in text
    assert "banana: $0.75" in text
    assert "orange: $2.00" in text
    assert "TOTAL:" in text

def test_order_integration_empty_file(tmp_path):
    input_file = tmp_path / "empty.csv"
    input_file.write_text("", encoding="utf-8")

    items = load_order(input_file)
    assert items == [] or len(items) == 0
