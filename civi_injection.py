import csv
import requests
#import json  # Possible TODO: Start using this library instead of just manually building up string as at present
import civi_base

def csv_line_to_json_URL_part(csv_line_dict):
    return '{"sequential":1,"contact_type":"Individual",' \
           '"first_name":"'+csv_line_dict["first_name"]+'",' \
           '"last_name":"'+csv_line_dict["last_name"]+'",' \
           '"api.Email.create":{"email":"'+csv_line_dict["email"]+'"},' \
           '"api.Address.create":{"location_type_id":"Home",' \
           '"street_address":"'+csv_line_dict["street_address"]+'",' \
           '"supplemental_address_1":"'+csv_line_dict["supplemental_address_1"]+'",'\
           ' "city": "'+csv_line_dict["city"]+'"}}'
    # + postcode?? (JG: postal_code)


class CiviContactInject(civi_base.CiviBase):
    action = "create"
    entity = "Contact"


    def upload_CSV(self, csv_filename):
        with open(csv_filename, 'rt') as f:
            reader = csv.DictReader(f)
            # Sample data from csv.DictReader()
            # {'contact_type': 'Individual', 'supplemental_address_1': '', 'street_address': '1 Church lane', 'city': 'Manchester', 'first_name': 'Sarah', 'email': 'sarah@jones.com', 'postal_code': 'm1 8HH', 'last_name': 'Jones'}
            # {'contact_type': 'Individual', 'supplemental_address_1': '', 'street_address': '', 'city': '', 'first_name': 'Harry', 'email': '', 'postal_code': '', 'last_name': 'Brown-no-email-address-so-should-be-rejected'}
            for row in reader:
                # Sample upload URL:
                # ...rest.php?entity=Contact&action=create&api_key=userkey&key=sitekey
                #    &json={"sequential":1,"contact_type":"Individual","first_name":"John","formal_title":"Mr","last_name":"Smith","api.Email.create":{"email":"jsmith@example.org"},"api.Address.create":{"location_type_id":"Home","street_address":"2 foo st","supplemental_address_1":"Bar", "city": "Sheffield"}}
                url_parameters = {}
                url_parameters['action'] = self.action
                url_parameters['entity'] = self.entity
                url_parameters['key'] = self.key
                url_parameters['api_key'] = self.api_key
                url_parameters['json'] = csv_line_to_json_URL_part(row)
                #print(url_parameters)
                # upload_result is a 'requests' object so can review various attributes afterwards,
                # Note: .post method has a 'json' argument, may be able to use that, see
                #   http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests
                upload_result = requests.post(self.protocol_s + self.base_URL, params=url_parameters)
                print("URL: "+upload_result.url)
                print("RESULT: "+upload_result.text)


def main():
    c = CiviContactInject()
    c.upload_CSV("sample.csv")


if __name__ == '__main__':
    main()