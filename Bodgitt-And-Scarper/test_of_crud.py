import unittest
import crud
from my_exceptions import RecordNotFoundException


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.crud = crud.CRUD()


    def test_find_return_type(self):
        self.assertIsInstance(self.crud.find(**{'name': None, 'location': None, 'search_and': False}), list)

    def test_find_location(self):
        self.assertEqual(self.crud.find(**{'name': None, 'location': 'X', 'search_and': False}), [19, 20, 21])

    def test_find_name(self):
        self.assertEqual(self.crud.find(**{'name': 'Buon', 'location': None, 'search_and': False}), [0, 5, 18, 25])

    def test_find_all(self):
        self.assertEqual(self.crud.find(**{'name': None, 'location': None, 'search_and': False}), range(29))

    def test_find_record_with_name_and_location(self):
        self.assertEqual(self.crud.find(**{'name': 'B', 'location': 'x', 'search_and': True}), [19])


    def test_read_return_type(self):
        self.assertIsInstance(self.crud.read(0), list)

    def test_read(self):
        self.assertEqual(self.crud.read(0), [0, 'Buonarotti & Company            ', 'Smallville                                                      ', 'Air Conditioning, Painting, Painting                            ', '10    ', '$40.00  ', '        ', 0])

    def test_read_error(self):
        self.assertRaises(RecordNotFoundException, self.crud.read, 999)


    def test_create(self):
        create_record = self.crud.create(*('Teste', 'Teste', '', '', '', ''))
        self.assertEqual(create_record, 29)
        self.crud.delete(create_record)

    def test_create_return_type(self):
        create_record = self.crud.create(*('Teste', 'Teste', '', '', '', ''))
        self.assertIsInstance(create_record, int)
        self.crud.delete(create_record)


    def test_delete(self):
        total_before_create = len(self.crud.find(**{'name': None, 'location': None, 'search_and': False}))
        create_record = self.crud.create(*('Teste', 'Teste', '', '', '', ''))

        self.crud.delete(create_record)
        total_after_delete = len(self.crud.find(**{'name': None, 'location': None, 'search_and': False}))

        self.assertEqual(total_before_create, total_after_delete)

    def test_delete_error(self):
        self.assertRaises(RecordNotFoundException, self.crud.delete, 999)

    def test_update(self):
        record = ('Teste' + ' ' * 27, 'Teste' + ' ' * 59 , ' ' * 64, ' ' * 6, ' ' * 8 , ' ' * 8)
        create_record = self.crud.create(*record)

        self.crud.update(create_record, **{'name': '1Teste', 'location': '2Teste','owner': '123'})
        bco = self.crud.read(create_record)
        del bco[0]
        del bco[-1]
        self.assertNotEqual(list(record), bco)

        self.crud.delete(create_record)


if __name__ == '__main__':
    unittest.main()
