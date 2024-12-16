import unittest
from RK2 import Orchestra, Conductor, first_task, second_task, third_task

class TestOrchestraFunctions(unittest.TestCase):
    
    def setUp(self):
        self.orchestras = [
            Orchestra(1, "Symphony"),
            Orchestra(2, "Chamber"),
            Orchestra(3, "String"),
        ]
        
        self.conductors = [
            Conductor(1, "Ivanov", 43, 1),
            Conductor(2, "Achapkin", 45, 2),
            Conductor(3, "Fundukov", 61, 3),
            Conductor(4, "Shishkin", 38, 3),
            Conductor(5, "Pushkin", 47, 1),
            Conductor(6, "Levitan", 42, 1)
        ]

    def test_first_task(self):
        cond_list = [(cond.fio, cond.salary, orch.name)
                     for orch in self.orchestras
                     for cond in self.conductors
                     if cond.orchestra_id == orch.id]
        result = first_task(cond_list)
        expected = sorted(cond_list)
        self.assertEqual(result, expected)

    def test_second_task(self):
        cond_list = [(cond.fio, cond.salary, orch.name)
                     for orch in self.orchestras
                     for cond in self.conductors
                     if cond.orchestra_id == orch.id]
        result = second_task(cond_list)
        expected = [('Symphony', 3), ('Chamber', 1), ('String', 2)]
        self.assertCountEqual(result, expected)

    def test_third_task(self):
        cond_list = [(cond.fio, cond.salary, orch.name)
                     for orch in self.orchestras
                     for cond in self.conductors
                     if cond.orchestra_id == orch.id]
        result = third_task(cond_list, 'ov')
        expected = [('Ivanov', 'Symphony'), ('Fundukov', 'String')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
