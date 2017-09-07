#-*- coding: utf-8 -*-

"""
my module

"""

class Math(object):
    """두개의 int값을 입력 받아서 다양한 연사을 하게 하는 클라스 
    
    param int a: a값을 입력
    param int b: b값을 입력
    """

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        """ 미리 입력받은 a와 b값을 더한 결과를 반환


        예제:
           다음과 같이 쓰세요:

           >>> Math(1,2).add()
           3


        :returns int: a + b에 대한 결과
        """

        return self._a + self._b



