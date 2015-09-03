def changeset_lookup(changeset_id):
    """
    """
    import requests
    import StringIO
    import xml.etree.cElementTree as ElementTree

    def parse_user(source, handle):
        for event, elem in ElementTree.iterparse(source,
                                                 events=('start','end')):
            if event == 'start':
                handle.start_element(elem.tag, elem.attrib)
            elem.clear()

    class user_decoder():
        def __init__(self):
            self.creation = ""
            self.changesets = 0
            self.blocks = 0
            self.active = 0

        def start_element(self, name, attributes):
            if name == 'tag':
                for attribute in attributes:
                    if attribute == 'comment':
                        self.comment = attributes[attribute]
            elif name == 'changesets':
                self.changesets = int(attributes['count'])
            elif name == 'received':
                self.blocks = int(attributes['count'])
                self.active = int(attributes['active'])

    url = 'http://www.osm.org/api/0.6/changeset/' + str(changeset_id)

    content = requests.get(url)
    if content.status_code == 404:
        raise EnvironmentError('Changeset cannot be found.')

    content = StringIO.StringIO(content.content)

    data_object = user_decoder()
    parse_user(content, data_object)
    return data_object
