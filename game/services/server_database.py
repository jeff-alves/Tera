class ServerDatabase(dict):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not ServerDatabase.__instance:
            ServerDatabase.__instance = dict.__new__(self, *args, **kwargs)
        return ServerDatabase.__instance

    def __init__(self):
        self.selected = None
        with open('data/servers.txt') as f:
            for line in f:
                l = line.split(None, 3)
                if len(l) == 4:
                    self.add(l[0], l[1], l[2], l[3].strip())
        self.add('127.0.0.1', "Unknow", "-1", "VPN")

    def add(self, ip, loc, id, name):
        id = int(id)
        self[ip] = (ip, loc, id, name.strip())
        self[id] = (ip, loc, id, name.strip())
