from util.util import singleton

@singleton
class ServerDatabase(dict):

    def __init__(self):
        dict.__init__(self)
        self.selected = None
        with open('data/servers.txt') as f:
            for line in f:
                l = line.split(None, 3)
                if len(l) == 4:
                    self.add(l[0], l[1], l[2], l[3].strip())
        self.add('127.0.0.1', "Unknow", "-1", "VPN")

    def add(self, ip, loc, id, name):
        id = int(id)
        self[ip] = {'ip':ip, 'location':loc, 'id':id, 'name':name.strip()}
        self[id] = {'ip':ip, 'location':loc, 'id':id, 'name':name.strip()}
