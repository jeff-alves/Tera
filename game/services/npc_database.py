from util.util import singleton
import xml.etree.ElementTree as ET


@singleton
class NpcDatabase(dict):

    def __init__(self, loc=None):
        dict.__init__(self)
        if loc: self.read(loc)

    def read(self, loc):
        tree = ET.parse('data/monsters/monsters-' + loc + '.xml')
        zones = tree.getroot()
        for zone in zones:
            for m in zone:
                self.add(zone.attrib['id'], m.attrib['id'], zone.attrib['name'], m.attrib['name'], m.attrib['isBoss'], m.attrib['hp'])

        tree = ET.parse('data/monsters/monsters-override.xml')
        zones = tree.getroot()
        for zone in zones:
            for m in zone.getchildren():
                self.add(zone.attrib['id'], m.attrib['id'], zone.attrib.get('name'), m.attrib.get('name'), m.attrib.get('isBoss'), m.attrib.get('hp'))


    def add(self, zone_id, m_id, zone_name, name, is_boss, hp):
        zone_id = int(zone_id)
        m_id = int(m_id)
        is_boss = (True if is_boss.lower() == 'true' else False) if is_boss != None else None
        tmp = self.pop((zone_id, m_id), None)
        if tmp:
            zone_name = zone_name if zone_name else tmp['zone_name']
            name = name if name else tmp['name']
            is_boss = is_boss if is_boss != None else tmp['is_boss']
            hp = hp if hp else tmp['hp_total']

        self[(zone_id, m_id)] = {'zone_name':zone_name, 'name':name, 'is_boss':is_boss, 'hp_total':float(hp)}
