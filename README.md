OpenStreetMap Diff Tool
==========================

This module is an analysis tool for use with [OpenStreetMap diff files (`*.osc`)](http://wiki.openstreetmap.org/wiki/Planet.osm/diffs).

Diff are available at http://planet.openstreetmap.org/replication for anyone to download in minutely, hourly, or daily segments.

Installation
============

* Download the zip.
* Unpack the zip somewhere
* Navigate to somewhere
* `$python setup.py install`

Usage
=====

To use, call `import osmdt`.

Calls right now include:
* `osmdt.fetch` to fetch a diff file. Input: file number, time type (optional--defaults to 'hour'). Output: datastream instance.
* `osmdt.process` to ingest and process the datastream from fetching. Input: instance from fetch call. Output: parsed instance of data.
* `osmdt.extract_changesets` to extract changesets and their properties from the processed data. Input: parsed data. Output: dictionary of changesets.
* `osmdt.extract_objects` to extract objects and their properties from the processed data. Input: parsed data. Output: dictionary of objects.
* `osmdt.extract_users` to extract users and their properties from the process data. Input: parsed data. Output: dictionary of users.
* `osmdt.changeset_lookup` to look up more information about a changeset from the OSM API. Input: changeset number. Output: instance of changeset data.
* `osmdt.user_lookup` to look up more information about a user from the OSM API. Input: user id number. Output: instance of user data.

Example call sequence:

```
import osmdt

data_stream = osmdt.fetch('25866')  # Retrieves the 000/025/866 diff
data_object = osmdt.process(data_stream)  # Parse the data stream
changesets = osmdt.extract_changesets(data_object) # Extract changeset information
users = osmdt.extract_users(data_object) # Extract user information
objects = osmdt.extract_objects(data_object) # Extract object information

user_info = {}
for user in users.iteritems():
    user_info[user] = osmdt.user_lookup(user['uid'])  # Retrieves user information 
```

License
=======
unlicense.org

Based on [osm-stream-process](http://github.com/iandees/osm-stream-process). See also [osm-stream](http://github.com/osmlab/osm-stream).
