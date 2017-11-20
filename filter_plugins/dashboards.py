# Copyright (c) 2017 StackHPC Ltd.
import json


def extract_new_dashboards(dashboard_meta, existing_dashboard_meta):
    """ Extract new dashboard

    Args:
        dashboard_meta: List of available dashboard files as obtained with
                        the Ansible find module.
        existing_dashboard_meta: List of dashboard metadata returned from
                                 querying api/search for Grafana.

    Returns:
         A list of dashboards in JSON format whose titles do not appear
         in the existing dashboard metadata.
    """
    existing_dashboard_titles = {d['title'] for d in json.loads(
                                          existing_dashboard_meta['content'])}
    available_dashboards = _load_dashboards(dashboard_meta)
    new_dashboards = [d for d in available_dashboards if d[
                       'dashboard']['title'] not in existing_dashboard_titles]
    return new_dashboards


def _load_dashboards(dashboard_meta):
    dashboards = []
    for dashboard in dashboard_meta:
        with open(dashboard['path']) as json_data:
            dashboards.append(json.load(json_data))
    return dashboards


class FilterModule(object):

    def filters(self):
        return {
            'extract_new_dashboards': extract_new_dashboards,
        }
