# -*- coding: utf-8 -*-
#
# Singleton Pattern
# get_instance メソッドで生成することで、単一オブジェクトを保持する。
# 通常の new でインスタンス生成することはできない。
#
# Original:
# Pythonでデザインパターンを学ぼう[Singleton]
# https://note.com/shimakaze_soft/n/ne7c8740b9975

class Singleton:

    _unique_instance = None

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()
        
        return cls._unique_instance
