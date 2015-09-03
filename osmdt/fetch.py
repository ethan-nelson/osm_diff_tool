def fetch(sequence, time='hour'):
    """
    """
    import StringIO
    import gzip
    import requests

    if time not in ['minute','hour','day']:
        raise ValueError('The supplied type of replication file does not exist.')

    sqn = str(sequence).zfill(9)
    url = "http://planet.osm.org/replication/%s/%s/%s/%s.osc.gz" %\
          (time, sqn[0:3], sqn[3:6], sqn[6:9])
    content = requests.get(url)

    if content.status_code == 404:
        raise EnvironmentError('Diff file cannot be found.')
    
    content = StringIO.StringIO(content.content)
    data_stream = gzip.GzipFile(fileobj=content)

    return data_stream
