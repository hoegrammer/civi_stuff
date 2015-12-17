import unittest
from civi_injection import csv_line_to_json_URL_part


class TestMethods(unittest.TestCase):

    def test_csv_to_URL(self):
        input = {
            'contact_type': 'Individual', 'supplemental_address_1': 'Bar',
            'street_address': '2 foo st', 'city': 'Sheffield', 'first_name': 'John',
            'email': 'jsmith@example.org', 'postal_code': 's3 9dn', 'last_name': 'Smith'
        }

        output = '{"sequential":1,"contact_type":"Individual","first_name":"John",'\
                 '"last_name":"Smith","api.Email.create":{"email":"jsmith@example.org"}' \
                 ',"api.Address.create":{"location_type_id":"Home","street_address":"2 ' \
                 'foo st","supplemental_address_1":"Bar", "city": "Sheffield"}}'
        # NB Postcode appears to have been discarded in output (I think that needs to go in)

        # assert (csv_line_to_json_URL_part(input) == output)
        self.assertEqual(csv_line_to_json_URL_part(input), output)


if __name__ == '__main__':
    unittest.main()