Ansible module for configuring Grafana datasources and dashboards
=================================================================

A simple role for loading dashboards and datasources for
Grafana. If follows the rule that if a dashboard or datasource
with the same name already exists, then it is not updated. 

It currently works at the organisation level.

Usage
-----

Unless your distro supports a recent version of Ansible, it is
recommended to run Ansible from a venv:

1. Create venv: ```$ virtualenv ansible```
2. Activate venv: ```$ source ansible/bin/activate```
3. Update pip (optional): ```$ pip install -U pip```
4. Install Ansible: ```$ pip install ansible```

An example of how to use the role is included in ```example/```.
