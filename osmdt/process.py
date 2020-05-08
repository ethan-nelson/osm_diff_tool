def process(data_stream):
    """
    Process a diff file stream into a class with objects separated.

    Parameters
    ----------
    data_stream : class
        A file-like class containing a decompressed diff file data stream.

    Returns
    -------
    data_object : osc_decoder class
        A class containing attribute dictionaries for each OpenStreetMap
        object type, namely .nodes, .relations, and .ways. Relations
        that contain nodes not modified and therefore not included in
        the diff file are listed in .missingNds.
    """
    import xml.etree.cElementTree as ElementTree

    def parse_diff(source, handle):
        for event, elem in ElementTree.iterparse(source,
                                                 events=('start', 'end')):
            if event == 'start':
                handle.start_element(elem.tag, elem.attrib)
            elif event == 'end':
                handle.end_element(elem.tag)
            elem.clear()

    class osc_decoder():
        def __init__(self):
            self.changes = {}
            self.nodes = {}
            self.ways = {}
            self.relations = {}
            self.action = ""
            self.primitive = {}
            self.missingNds = set()

        def start_element(self, name, attributes):
            if name in ('modify', 'delete', 'create'):
                self.action = name
            if name in ('node', 'way', 'relation'):
                self.primitive['id'] = int(attributes['id'])
                self.primitive['version'] = int(attributes['version'])
                self.primitive['changeset'] = int(attributes['changeset'])
                self.primitive['username'] = attributes['user']
                self.primitive['uid'] = attributes['uid']
                self.primitive['timestamp'] = attributes['timestamp']
                self.primitive['tags'] = {}
                self.primitive['action'] = self.action
            if name == 'node':
                self.primitive['lat'] = float(attributes['lat'])
                self.primitive['lon'] = float(attributes['lon'])
            elif name == 'tag':
                key = attributes['k']
                val = attributes['v']
                self.primitive['tags'][key] = val
            elif name == 'way':
                self.primitive['nodes'] = []
            elif name == 'relation':
                self.primitive['members'] = []
            elif name == 'nd':
                ref = int(attributes['ref'])
                self.primitive['nodes'].append(ref)
                if ref not in self.nodes:
                    self.missingNds.add(ref)
            elif name == 'member':
                self.primitive['members'].append({
                    'type': attributes['type'],
                    'role': attributes['role'],
                    'ref': attributes['ref']
                })

        def end_element(self, name):
            if name == 'node':
                self.nodes[self.primitive['id']] = self.primitive
            elif name == 'way':
                self.ways[self.primitive['id']] = self.primitive
            elif name == 'relation':
                self.relations[self.primitive['id']] = self.primitive
            if name in ('node', 'way', 'relation'):
                self.primitive = {}

    data_object = osc_decoder()
    parse_diff(data_stream, data_object)

    return data_object
