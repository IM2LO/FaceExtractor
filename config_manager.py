def read_config():
    config = {}
    with open('config.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
    return config