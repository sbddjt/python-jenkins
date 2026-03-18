"""간단한 계산기 클래스"""

class Calculator:
    """사칙연산을 수행하는 계산기"""
    
    def sum(self, a, b):
        """두 숫자를 더합니다"""
        return a + b
    
    def subtract(self, a, b):
        """두 숫자를 뺍니다"""
        return a - b
    
    def multiply(self, a, b):
        """두 숫자를 곱합니다"""
        return a * b
    
    def divide(self, a, b):
        """두 숫자를 나눕니다"""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return a / b
    
    def power(self, base, exponent):
        """거듭제곱 계산"""
        return base ** exponent