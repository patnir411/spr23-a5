#!/usr/bin/env python3
from calculator_adapter import run

# Test addition
assert run("4 + 7").output.strip() == "11", "Addition test failed"

# Test subtraction
assert run("12 - 3").output.strip() == "9", "Subtraction test failed"

print("All tests passed!")


###

print("All tests passed!")