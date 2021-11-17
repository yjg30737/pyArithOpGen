from abc import ABCMeta


class AbstractExpStruct(metaclass=ABCMeta):
    PLUS = 0
    MINUS = 1
    MULTIPLY = 2
    DIVIDE = 3

    oper_min_cnt = 2
    oper_max_cnt = 8
    oper_cnt = 2

    min = 1
    max = 10

    op_dict = {PLUS: '+', MINUS: '-', MULTIPLY: '*', DIVIDE: '/'}

    def __init__(self):
        raise NotImplementedError('abstract base class')