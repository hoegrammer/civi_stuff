import csv
import requests
import json 
import civi_base

universal_params = {'api_key': civi_base.api_key, 'key': civi_base.site_key}

def encode_contact_for_upload(contact):
    
    return ({
        'sequential': 1,
        'contact_type': 'Individual',
        'first_name': contact['first_name'],
        'last_name': contact['last_name'],
        'api.Email.create': {
            'email': contact['email']
        },
        'api.Address.create': {
            'location_type_id': "Home", 
            'street_address': contact['street_address'],
            'supplemental_address_1': contact['supplemental_address_1'],
            'city': contact['city'],
            'postal_code': contact['postal_code']
        }
    })

def get_contact_upload_params(contact):
    
    contact_upload_params = universal_params.copy();
    contact_upload_params.update({
        'action': 'create', 'entity': 'Contact', 
        'json': json.dumps(encode_contact_for_upload(contact))
    })
    return contact_upload_params

class CiviContactInject():
    protocol_s = 'http://';

    def upload_CSV(self, csv_filename):
        with open(csv_filename, 'rt') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contact = row
                upload_result = requests.post(
                    self.protocol_s + civi_base.base_URL, 
                    params = get_contact_upload_params(contact)
                )
                print("URL: "+upload_result.url)
                print("RESULT: "+upload_result.text)


def main():
    c = CiviContactInject()
    c.upload_CSV("sample.csv")


if __name__ == '__main__':
    main()
