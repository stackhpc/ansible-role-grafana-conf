# Copyright (c) 2017 StackHPC Ltd.
import json


def extract_new_datasources(available_datasources, existing_datasources):
    """ Extract new datasources

    Args:
        available_datasources: List of enabled datasources
        existing_datasources: List of existing datasources as from
                              querying the Grafana API for datasources

    Returns:
         A list of datasources in JSON format which do not appear
         in the specified list of existing datasources.
    """
    existing_datasource_names = {d['name'] for d in json.loads(
                                                       existing_datasources)}
    new_datasources = [d for d in available_datasources if d[
                                    'name'] not in existing_datasource_names]
    return new_datasources


class FilterModule(object):

    def filters(self):
        return {
            'extract_new_datasources': extract_new_datasources,
        }
