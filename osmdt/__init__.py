from .extract import (
        extract_changesets,
        extract_objects,
        extract_users,
)
from .fetch import fetch
from .process import process


def run(sequence, time='hour', changesets=True, objects=True, users=True):
    """
    """
    import osmdt

    if not changesets and not objects and not users:
        raise Exception('No output variables are specified')

    data_stream = osmdt.fetch(sequence, time=time)
    data_object = osmdt.process(data_stream)

    if changesets:
        changeset_dict = osmdt.extract_changesets(data_object)
    else:
        changeset_dict = {}
    if objects:
        object_dict = osmdt.extract_objects(data_object)
    else:
        object_dict = {}
    if users:
        user_dict = osmdt.extract_users(data_object)
    else:
        user_dict = {}

    return changeset_dict, object_dict, user_dict
