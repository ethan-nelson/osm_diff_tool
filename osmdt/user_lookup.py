def user_lookup(user_id):
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
            self.username = ""
            self.creation_date = ""
            self.changesets = 0
            self.blocks = 0
            self.active = 0

        def start_element(self, name, attributes):
            if name == 'user':
                self.username = attributes['display_name']
                self.creation_date = attributes['account_created']
            elif name == 'changesets':
                self.changesets = int(attributes['count'])
            elif name == 'received':
                self.blocks = int(attributes['count'])
                self.active = int(attributes['active'])

    uid = str(user_id)
    if uid.isalpha():
        raise ValueError('Input must be an OSM user id number, not a username.')
    url = 'http://www.osm.org/api/0.6/user/' + uid

    content = requests.get(url)
    if content.status_code == 404:
        raise EnvironmentError('User cannot be found') 

    content = StringIO.StringIO(content.content)

    data_object = user_decoder()
    parse_user(content, data_object)
    return data_object
