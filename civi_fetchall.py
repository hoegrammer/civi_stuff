import requests
import civi_base


class CiviContactFetch(civi_base.CiviBase):
    action = "get"
    entity = "Contact"

    def fetch_all(self):
        url_parameters = {}
        url_parameters['action'] = self.action
        url_parameters['entity'] = self.entity
        url_parameters['key'] = self.key
        url_parameters['api_key'] = self.api_key
        url_parameters['json'] = "1"
        return requests.get(self.protocol_s + self.base_URL, params=url_parameters)


def main():
    c = CiviContactFetch()
    print(str(c.fetch_all().json()))


if __name__ == '__main__':
    main()
