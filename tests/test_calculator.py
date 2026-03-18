"""Calculator 클래스에 대한 단위 테스트"""
import pytest
import sys
import os

# src 디렉토리를 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator:
    """Calculator 테스트 클래스"""
    
    def setup_method(self):
        """각 테스트 전에 Calculator 객체 생성"""
        self.calculator = Calculator()
        print("테스트 시작: Calculator 객체 생성")
    
    def test_sum_positive_numbers(self):
        """양수 덧셈 테스트"""
        result = self.calculator.sum(10, 20)
        assert result == 30, "10 + 20은 30이어야 합니다"
        print(f"✓ 덧셈 테스트 통과: 10 + 20 = {result}")
    
    def test_sum_negative_numbers(self):
        """음수 덧셈 테스트"""
        result = self.calculator.sum(-5, -3)
        assert result == -8, "-5 + (-3)은 -8이어야 합니다"
        print(f"✓ 음수 덧셈 테스트 통과: -5 + (-3) = {result}")
    
    def test_subtract(self):
        """뺄셈 테스트"""
        result = self.calculator.subtract(20, 10)
        assert result == 10, "20 - 10은 10이어야 합니다"
        print(f"✓ 뺄셈 테스트 통과: 20 - 10 = {result}")
    
    def test_multiply(self):
        """곱셈 테스트"""
        result = self.calculator.multiply(5, 4)
        assert result == 20, "5 * 4는 20이어야 합니다"
        print(f"✓ 곱셈 테스트 통과: 5 * 4 = {result}")
    
    def test_divide(self):
        """나눗셈 테스트"""
        result = self.calculator.divide(20, 4)
        assert result == 5, "20 / 4는 5여야 합니다"
        print(f"✓ 나눗셈 테스트 통과: 20 / 4 = {result}")
    
    def test_divide_by_zero(self):
        """0으로 나누기 테스트"""
        with pytest.raises(ValueError):
            self.calculator.divide(10, 0)
        print("✓ 0으로 나누기 예외 처리 테스트 통과")
    
    def teardown_method(self):
        """각 테스트 후 정리"""
        self.calculator = None
        print("테스트 종료: 객체 정리 완료\n")

    def test_power(self):
        """거듭제곱 테스트"""
        result = self.calculator.power(2, 3)
        assert result == 8, "2^3은 8이어야 합니다"
        print(f"✓ 거듭제곱 테스트 통과: 2^3 = {result}")