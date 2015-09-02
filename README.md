OpenStreetMap Diff Tool
==========================

This module is an analysis tool for use with OpenStreetMap diff files (`*.osc`). These files are available at http://planet.openstreetmap.org/replication for anyone to download either in real time or after thef act.

To begin use, simply call `import osmdt` after installation.

Sample calls available for now:

```
import osmdt

data = osmdt.fetch('25866')  # Retrieves the 000/025/866 diff
differenceObject = osmdt.process(data)  # Parse the data stream
changesets = osmdt.extract_changesets(differenceObject) # Extract changeset information
users = osmdt.extract_users(differenceObject) # Extract user information
objects = osmdt.extract_objects(differenceObject) # Extract object information

userInfo = {}
for changeset in changesets.iteritems():
    userInfo[changeset] = osmdt.userUtil(changeset['uid'])  # Retrieves user information 

```

