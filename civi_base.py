with open("../civi_base_URL",mode='r') as f:
    base_URL = f.readline().rstrip()
with open("../civi_site_key",mode='r') as f:
    site_key = f.readline().rstrip()
with open("../civi_api_key",mode='r') as f:
    api_key = f.readline().rstrip()
