class CiviBase():
    protocol_s = "http://"  ## https:// for production site...


    def __init__(self):
        # TODO: ENOENT or other read problem handling
        # "../~" filenames to keep sensitive data outside of source code
        with open("../civi_base_URL",mode='r') as f:
            self.base_URL = f.readline().rstrip()
        with open("../civi_site_key",mode='r') as f:
            self.key = f.readline().rstrip()
        with open("../civi_api_key",mode='r') as f:
            self.api_key = f.readline().rstrip()