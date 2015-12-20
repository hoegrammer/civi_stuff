import unittest
import url_writer
import json
import civi_base


class TestMethods(unittest.TestCase):

    maxDiff = None # provides more info on failure

    contactInput =  {
        'contact_type': 'Individual', 'supplemental_address_1': 'Bar',
        'street_address': '2 foo st', 'city': 'Sheffield', 'first_name': 'John',
        'email': 'jsmith@example.org', 'postal_code': 's3 9dn', 'last_name': 'Smith'
    }

    contactOutput = {
        "sequential": 1, "contact_type": "Individual", "first_name": "John", "last_name": "Smith", 
        "api.Email.create": {
            "email": "jsmith@example.org"
        }, 
        "api.Address.create": {
            "location_type_id": "Home", "street_address": "2 foo st", 
            "supplemental_address_1": "Bar", "city": "Sheffield", "postal_code": "s3 9dn"
         }
    }

    def test_get_contact_upload_params(self): 

       output = {
           'entity': 'Contact', 'action': 'create', 'api_key': civi_base.api_key, 
           'site_key': civi_base.site_key, 'json': json.dumps(self.contactOutput)
       }

       self.assertEqual(url_writer.get_contact_upload_params(self.contactInput), output)




if __name__ == '__main__':
    unittest.main()
