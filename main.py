import csv
import requests
import civi_base
import url_writer

class JustGivingUpload():
    protocol_s = 'http://';

    def ensure_contacts_exist(self, csv_filename):
        # Currently uploading all contacts.
        # TODO: Don't upload duplicates. Fill in JGIDs where appropriate.
        # Alert user if can't (because there is not exactly one candidate).
        # Communicate server errors to user.
        with open(csv_filename, 'rt') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contact = row
                upload_result = requests.post(
                    self.protocol_s + civi_base.base_URL, 
                    params = url_writer.get_contact_upload_params(contact)
                )
                print("URL: "+upload_result.url)
                print("RESULT: "+upload_result.text)


def main():
    c = JustGivingUpload()
    c.ensure_contacts_exist("sample.csv")


if __name__ == '__main__':
    main()
