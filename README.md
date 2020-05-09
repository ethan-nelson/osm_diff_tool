OpenStreetMap Diff Tool
==========================

This module is a tool to download and extract data from [OpenStreetMap diff files (`*.osc`)](https://wiki.openstreetmap.org/wiki/Planet.osm/diffs).

Diff are available at https://planet.openstreetmap.org/replication for anyone to download in minutely, hourly, or daily segments.

Installation
============

Releases
--------
Versioned releases are available from [PyPI](https://pypi.org/project/osm_diff_tool/) for use with Python pip:

* `$pip install osm_diff_tool`

Bleeding Edge
-------------
You can also install the bleeding edge version of the tool:

### Method 1
* Download the zip.
* Unpack the zip to $somewhere.
* Navigate to $somewhere.
* `$python setup.py install`.

### Method 2
`$pip install git+https://github.com/ethan-nelson/osm_diff_tool.git`

Usage
=====

To use the tool, call `import osmdt`.

Calls right now include:

* `osmdt.fetch` to fetch a diff file. Input: file number, time type (optional--defaults to 'hour'). Output: datastream instance.
* `osmdt.process` to ingest and process the datastream from fetching. Input: datastream instance. Output: parsed instance of data.
* `osmdt.extract_changesets` to extract changesets and their properties from the processed data. Input: parsed data instance. Output: dictionary of changesets.
* `osmdt.extract_objects` to extract objects and their properties from the processed data. Input: parsed data. Output: dictionary of objects.
* `osmdt.extract_users` to extract users and their properties from the process data. Input: parsed data. Output: dictionary of users.

Example call sequence:

```
import osmdt

data_stream = osmdt.fetch('25866')  # Retrieves the 000/025/866 diff
data_object = osmdt.process(data_stream)  # Parse the data stream
changesets = osmdt.extract_changesets(data_object) # Extract changeset information
users = osmdt.extract_users(data_object) # Extract user information
objects = osmdt.extract_objects(data_object) # Extract object information
```

Alternatively, you can use `osmdt.run` to run all the commands with one call:

```
import osmdt

changesets, objects, users = osmdt.run('25866')
```

Related Projects
================

This tool is used in the [OSM Hall Monitor](https://github.com/ethan-nelson/osm_hall_monitor) project.
