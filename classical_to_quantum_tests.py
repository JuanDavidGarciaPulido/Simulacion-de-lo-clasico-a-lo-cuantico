import unittest
import classical_to_quantum as c_a_q


class test_simulacion(unittest.TestCase):

    def test_canicas(self):
        matriz = [[False, False, False, False, False, False],
                       [False, False, False, False, False, False],
                       [False, True, False, False, False, True],
                       [False, False, False, True, False, False],
                       [False, False, True, False, False, False],
                       [True, False, False, False, True, False]]
        self.assertEqual(c_a_q.problem_canicas(matriz,
                      [[6], [2], [1], [5], [3], [10]], 1), [[0], [0], [12], [5], [1], [9]])

    def test_rendijas_real(self):
        rendijas = 2
        self.assertEqual(c_a_q.vector_final_real(rendijas), [[(0.0, 0.0),
                                                       (0.0, 0.0),
                                                       (0.0, 0.0),
                                                       (0.16666666666666666, 0.0),
                                                       (0.16666666666666666, 0.0),
                                                       (0.3333333333333333, 0.0),
                                                       (0.16666666666666666, 0.0),
                                                       (0.16666666666666666, 0.0)]])

    def test_rendijas_complejo(self):
        rendijas = 2
        self.assertEqual(c_a_q.vector_final_imaginario(2), [[(0.0, 0.0),
                                                             (0.0, 0.0),
                                                             (0.0, 0.0),
                                                             (-0.2886751345948129, 0.2886751345948129),
                                                             (-0.2886751345948129, -0.2886751345948129),
                                                             (0.0, 0.0),
                                                             (-0.2886751345948129, -0.2886751345948129),
                                                             (0.2886751345948129, -0.2886751345948129)]])


if __name__ == '__main__':
    unittest.main()