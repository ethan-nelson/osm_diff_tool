def fetch(sequence, time='hour'):
    """
    Fetch an OpenStreetMap diff file.

    Parameters
    ----------
    sequence : string or integer
        Diff file sequence desired. Maximum of 9 characters allowed. The value
        should follow the two directory and file name structure from the site,
        e.g. https://planet.osm.org/replication/hour/NNN/NNN/NNN.osc.gz (with
        leading zeros optional).

    time : {'minute', 'hour', or 'day'}, optional
        Denotes the diff file time granulation to be downloaded. The value
        must be a valid directory at https://planet.osm.org/replication/.

    Returns
    -------
    data_stream : class
        A file-like class containing a decompressed data stream from the
        fetched diff file in string format.

    """
    import gzip
    from io import BytesIO
    import requests

    if time not in ['minute', 'hour', 'day']:
        raise ValueError('Supplied replication file time type does not exist.')

    sqn = str(sequence).zfill(9)
    url = "https://planet.osm.org/replication/%s/%s/%s/%s.osc.gz" %\
          (time, sqn[0:3], sqn[3:6], sqn[6:9])
    response = requests.get(url)

    if response.status_code == 404:
        raise EnvironmentError('Diff file cannot be found.')
    elif response.status_code == 403:
        raise EnvironmentError('Access forbidden. You may be rate limited.')
    elif response.status_code != 200:
        raise EnvironmentError('HTTP error: %i' % (response.status_code,))

    content = BytesIO(response.content)
    data_stream = gzip.GzipFile(fileobj=content)

    return data_stream
