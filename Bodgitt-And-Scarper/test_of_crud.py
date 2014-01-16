import unittest
import crud
from my_exceptions import RecordNotFoundException


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.crud = crud.CRUD()

    def test_find_return_type(self):
        self.assertIsInstance(self.crud.find({'name': '', 'location': '', 'search_and': False}), list)

    def test_find_location(self):
        create_record = self.crud.create(['Teste 123', 'Teste 321'])
        self.assertEqual(self.crud.find({'name': '', 'location': 'Teste 321', 'search_and': False}), [create_record])
        self.crud.delete(create_record)

    def test_find_name(self):
        create_record = self.crud.create(['Teste 321', 'Teste 311'])
        self.assertEqual(self.crud.find({'name': 'Teste 321', 'location': '', 'search_and': False}), [create_record])
        self.crud.delete(create_record)

    def test_find_record_with_name_and_location(self):
        create_record = self.crud.create(['Teste name', 'Teste location'])
        self.assertEqual(self.crud.find({'name': 'Teste name', 'location': 'Teste location', 'search_and': True}), [create_record])
        self.crud.delete(create_record)

    def test_read_return_type(self):
        self.assertIsInstance(self.crud.read(0), list)

    def test_read(self):
        create_record = self.crud.create(['Teste read', 'Teste read'])
        self.assertEqual(self.crud.read(create_record), ['Teste read                      ', 'Teste read                                                      ', ' ' * 64, ' ' * 6, ' ' * 8, ' ' * 8, 0])
        self.crud.delete(create_record)

    def test_read_error(self):
        self.assertRaises(RecordNotFoundException, self.crud.read, 999)

    def test_create(self):
        create_record = self.crud.create(['Teste', 'Teste'])
        self.assertRaises(self.crud.read(create_record))
        self.crud.delete(create_record)

    def test_create_return_type(self):
        create_record = self.crud.create(['Teste', 'Teste'])
        self.assertIsInstance(create_record, int)
        self.crud.delete(create_record)

    def test_delete(self):
        create_record = self.crud.create(['Teste', 'Teste'])
        self.crud.delete(create_record)

    def test_delete_error(self):
        self.assertRaises(RecordNotFoundException, self.crud.delete, 99999)

        create_record = self.crud.create(['Teste', 'Teste'])
        self.crud.delete(create_record)

        self.assertRaises(RecordNotFoundException, self.crud.delete, create_record)

    def test_update(self):
        record = ['Teste', 'Teste']
        create_record = self.crud.create(record)

        self.crud.update(create_record, {'name': '1Teste', 'location': '2Teste', 'owner': '123'})
        bco = self.crud.read(create_record)
        del bco[0]
        del bco[-1]
        self.assertNotEqual(list(record), bco)

        self.crud.delete(create_record)

    def test_format_for_necessary_size(self):
        self.assertEqual(self.crud.format_for_necessary_size('123456789', 5), '12345')
        self.assertEqual(self.crud.format_for_necessary_size('1234', 5), '1234 ')
        self.assertEqual(self.crud.format_for_necessary_size('12345', 5), '12345')

    def test_verify_entry_type(self):
        self.assertFalse(self.crud.verify_entry_type(['Texto', 'Texto', 'Texto', '123', '123', '123']))


if __name__ == '__main__':
    unittest.main()
