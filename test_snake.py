import pytest
import main

def test_Snake():
    snake = main.Game()
    assert snake.var1 == "12"
