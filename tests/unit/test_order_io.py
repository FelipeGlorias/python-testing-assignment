import pytest
from src.order_io import load_order, write_receipt

def test_load_order_valid(tmp_path):
    
    input_file = tmp_path / "order.csv"
    input_file.write_text("apple,$1.50\nbanana,$2.00\n", encoding="utf-8")

    items = load_order(input_file)
    assert isinstance(items, list)
    assert len(items) == 2
    assert items[0] == ("apple", 1.50)
    assert items[1] == ("banana", 2.00)

def test_write_receipt(tmp_path):
    
    items = [("apple", 1.50), ("banana", 2.00)]
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent=0, tax_rate=0.0)
    
    text = output_file.read_text(encoding="utf-8")
    
    assert "apple: $1.50" in text
    assert "banana: $2.00" in text
    
    assert "TOTAL" in text
