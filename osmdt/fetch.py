def fetch(sequence, time='hour'):
    import StringIO
    import gzip
    import requests

    try:
        sqn = str(sequence).zfill(9)
        url = "http://planet.osm.org/replication/%s/%s/%s/%s.osc.gz" %\
              (time, sqn[0:3], sqn[3:6], sqn[6:9])

        content = requests.get(url)
        content = StringIO.StringIO(content.content)
        dataStream = gzip.GzipFile(fileobj=content)

        return dataStream
    except:
        return None
