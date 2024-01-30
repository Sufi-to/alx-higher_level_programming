#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    print(m_a)
    print("-----------")
    print(m_b)
    print("===================")
    print(m_a.shape)
    print("*****************")
    print(m_b.shape)
    print("===================")
    print(m_a @ m_b)
    print("the first one ------------")
    print(m_a.shape[1] == m_b.shape[0])


lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
