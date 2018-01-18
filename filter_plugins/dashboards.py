# Copyright (c) 2017-2018 StackHPC Ltd.
import base64
import json


def extract_new_dashboards(dashboards, existing_dashboard_meta):
    """ Extract new dashboards

    Args:
        dashboards: List of available dashboards (b64 encoded JSON).
        existing_dashboard_meta: List of dashboard metadata returned from
                                 querying api/search for Grafana.

    Returns:
         A list of dashboards in JSON format whose titles do not appear
         in the existing dashboard metadata.
    """
    existing_dashboard_titles = {d['title'] for d in json.loads(
                                          existing_dashboard_meta['content'])}
    available_dashboards = [json.loads(
                       base64.b64decode(db['content'])) for db in dashboards]
    new_dashboards = [d for d in available_dashboards if d[
                       'dashboard']['title'] not in existing_dashboard_titles]
    return new_dashboards

class FilterModule(object):

    def filters(self):
        return {
            'extract_new_dashboards': extract_new_dashboards,
        }
